# -*- coding:utf-8 -*-
import zerorpc
import game
import analysis
import copy

class Controller(object):
  def __init__(self):
    self.game = game.Game()

  def Join(self, name):
    self.game.AddPlayer(name)

  def Start(self, name):
    if name != self.game.Master().name:
      return "You don't have permission to start game!"
    self.game.Start()

  def Info(self, name):
    return self.game.Info(name)

  def Throw(self, name, x, y):
    if name != self.game.NowPlayer().name:
      return "not your turn"
    if self.game.Throw(x, y):
      '''
      win_list = []
      for p in self.game.player_list:
        pai = p.now_pai
        pai[x][y] += 1
        pai[x][0] += 1
        if analysis.Win(pai):
          win_list.append(p)
      if len(win_list) > 0:
        msg = ""
        for p in win_list:
          msg += p.name + " "
        msg += " win!"
        #self.game.Init()
        return msg
      '''
      return self.Info(name)
    else:
      return "invalid!"

  def Ready(self, name):
    self.game.Player(name).ready = True

  def Take(self, name):
    # 是否轮到这个玩家
    if name != self.game.NowPlayer().name:
      return "not your turn"
    if not self.game.AllChecked():
      return "some on is not checked"
    # 是否有人碰刚打出去的牌
    #if self.game.AllReady():
    self.game.Deal()
    return self.Info(name)

  def Check(self, name, cmd):
    if self.game.Player(name).checked:
      return "Already Checked"
    if cmd == "hu":
      pai = copy.deepcopy(self.game.Player(name))
      tokens = self.game.all_majiang.throwed_pai[-1].split(',')
      x = int(tokens[0])
      y = int(tokens[1])
      pai[x][y] += 1
      pai[x][0] += 1
      if analysis.Win(pai):
        self.game.status = "end"
        self.game.winner.append(name)
        self.game.Player(name).checked = True
        return self.game.info()


if __name__ == '__main__':
  s = zerorpc.Server(Controller())
  s.bind("tcp://127.0.0.1:1111")
  s.run()
