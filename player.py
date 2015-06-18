# -*- coding:utf-8 -*-
import random
import sys
import analysis

class Player(object):
  def __init__(self, name):
    self.name = name
    self.now_pai = []
    self.ready = False
    self.checked = False
    self.Init()

  def Init(self):
    self.now_pai = [
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    self.now_peng = {}
    self.ready = False
    self.checked = False

  def ThrowPai(self, x, y):
    if self.now_pai[x][y] > 0:
      self.now_pai[x][y] -= 1
      self.now_pai[x][0] -= 1
      return True
    else:
      return False

  def TakePai(self, x, y):
    self.now_pai[x][y] += 1
    self.now_pai[x][0] += 1

  def Peng(self, x, y):
    if self.now_pai[x][y] >= 2:
      self.now_pai[x][y] -= 2
      self.now_pai[x][0] -= 2
      self.now_peng[str(x) + ',' + str(y)] = True
      return True
    else:
      return False

  def Hu(self):
    return analysis.Win(self.now_pai)

  def Check(self):
    self.checked = True

if __name__ == '__main__':
  player = Player("Alan")
  player.TakePai(0, 1)
  player.TakePai(0, 2)
  player.TakePai(0, 2)
  print player.now_pai
  player.ThrowPai(0, 1)
  print player.now_pai
  print player.Hu()
