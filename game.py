# -*- coding:utf-8 -*-
import player
import majiang
import logging
logging.basicConfig(level=logging.INFO)

class Game(object):
  def __init__(self):
    self.now_player = 0
    self.master = 0
    self.all_majiang = majiang.AllMajiang()
    self.player_list = []
    self.check_player = 0
    self.status = "waiting for player ready"
    self.winner = []
    self.Init()

  def Init(self):
    self.now_player = 0
    self.status = "waiting for player ready"
    self.master = 0
    self.check_player = 0
    self.all_majiang = majiang.AllMajiang()
    self.winner = []

  def Master(self):
    return self.player_list[self.master]

  def NowPlayer(self):
    return self.player_list[self.now_player]

  def SetNowPlayer(self, name):
    for i in range(0, len(self.player_list)):
      if self.player_list[i].name == name:
        self.now_player = i
        return

  def Player(self, name):
    for p in self.player_list:
      if p.name == name:
        return p
    return None

  def AddPlayer(self, name):
    if len(self.player_list) >= 4:
      return False
    else:
      self.player_list.append(player.Player(name))

  def AllReady(self):
    for p in self.player_list:
      if not p.ready:
        return False
    return True

  def AllChecked(self):
    for p in self.player_list:
      if not p.checked:
        return False
    return True


  def Start(self):
    if not self.AllReady():
      return False
    for i in range(0, 13):
      x, y = self.all_majiang.Deal()
      self.player_list[self.master].TakePai(x, y)
      logging.info("deal " + str(x) + ',' + str(y) + ' to ' + self.player_list[self.master].name)
      x, y = self.all_majiang.Deal()
      self.player_list[(self.master + 1) % 4].TakePai(x, y)
      logging.info("deal " + str(x) + ',' + str(y) + ' to ' + self.player_list[(self.master + 1) % 4].name)
      x, y = self.all_majiang.Deal()
      self.player_list[(self.master + 2) % 4].TakePai(x, y)
      logging.info("deal " + str(x) + ',' + str(y) + ' to ' + self.player_list[(self.master + 2) % 4].name)
      x, y = self.all_majiang.Deal()
      self.player_list[(self.master + 3) % 4].TakePai(x, y)
      logging.info("deal " + str(x) + ',' + str(y) + ' to ' + self.player_list[(self.master + 3) % 4].name)
    self.now_player = self.master
    self.status = "running"
    return True

  def Deal(self):
    x, y = self.all_majiang.Deal()
    if x == -1 and y == -1:
      return False
    self.player_list[self.now_player].TakePai(x, y)
    return True

  def Throw(self, x, y):
    if self.player_list[self.now_player].ThrowPai(x, y):
      logging.info("Player " + self.NowPlayer().name + " throw " + str(x) + ' ' + str(y) + ' success!')
      if self.all_majiang.Throw(x, y):
        logging.info("all_majiang throw " + str(x) + ' ' + str(y) + ' success!')
        #有人出牌后要把其他人的check状态置为False
        for p in self.player_list:
          if p.name == self.NowPlayer().name:
            continue
          p.checked = False
        self.now_player = (self.now_player + 1) % 4
        logging.info("now_player turn to " + self.player_list[self.now_player].name)
        return True
      else:
        return False
    else:
      return False

  def Info(self, name):
    msg = ""
    msg += "status: " + self.status + "\n"
    msg += "banker: " + self.Master().name + "\n"
    msg += "now_player: " + self.NowPlayer().name + "\n"
    msg += "ready:"
    for p in self.player_list:
      if p.ready:
        msg += " " + p.name
    msg += "\n"

    msg += "checked:"
    for p in self.player_list:
      if p.checked:
        msg += " " + p.name
    msg += "\n"
    msg += "winner: " + str(self.winner) + "\n"
    msg += "throwed_pai: " + str(self.all_majiang.throwed_pai) + "\n"
    msg += "Your now_pai: " + str(self.Player(name).now_pai)
    return msg

if __name__ == '__main__':
  manager = Game()
  manager.AddPlayer("1")
  manager.AddPlayer("2")
  manager.AddPlayer("3")
  manager.AddPlayer("4")
  manager.Start()
  print manager.all_majiang.majiang

  print ""
  for i in range(0, 4):
    print manager.player_list[i].now_pai
