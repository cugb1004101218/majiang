# -*- coding:utf-8 -*-
import random
import sys
import logging

class AllMajiang(object):
  def __init__(self):
    self.majiang = []
    self.deal_order = []
    self.using_pai = []
    self.throwed_pai = []
    self.Init()

  def Deal(self):
    if len(self.deal_order) == 0:
      return -1, -1
    pai = self.deal_order[0]
    del self.deal_order[0]
    x = int(pai.strip().split(',')[0])
    y = int(pai.strip().split(',')[1])
    self.majiang[x][y] -= 1
    self.majiang[x][0] -= 1
    self.using_pai[x][y] += 1
    self.using_pai[x][0] += 1
    return x, y

  def Throw(self, x, y):
    if self.using_pai[x][y] > 0:
      self.using_pai[x][y] -= 1
      self.using_pai[x][0] -= 1
      self.throwed_pai.append(str(x) + ',' + str(y))
      return True
    else:
      return False

  def Init(self):
    #初始化剩下牌
    self.majiang = [
      [36, 4, 4, 4, 4, 4, 4, 4, 4, 4 ],  #万
      [36, 4, 4, 4, 4, 4, 4, 4, 4, 4 ],  #筒
      [36, 4, 4, 4, 4, 4, 4, 4, 4, 4 ],  #索
      [28, 4, 4, 4, 4, 4, 4, 4],  #字
    ]

    #洗牌
    self.deal_order = []
    for i in range(0, 3):
      for j in range(1, 10):
        for k in range(1, 5):
          self.deal_order.append(str(i) + ',' + str(j) + ',' + str(k))
    for i in range(1, 8):
      for j in range(1, 5):
        self.deal_order.append('3,' + str(i) + ',' + str(j))
    random.shuffle(self.deal_order)

    self.using_pai = [
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],  #万
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],  #筒
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],  #索
      [0, 0, 0, 0, 0, 0, 0, 0],  #字
    ]
    self.throwed_pai = []

if __name__ == '__main__':
  all_majiang = AllMajiang()
  print all_majiang.deal_order
