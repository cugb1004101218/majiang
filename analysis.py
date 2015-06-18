# -*- coding:utf-8 -*-
import os
import sys

#判断是否胡牌的函数
def Win(allPai):
  jiangPos = 0 #“将”的位置
  yuShu = 0 #余数
  jiangExisted = False
  #是否满足3,3,3,3,2模型
  for i in range(0, 4):
    yuShu= allPai[i][0] % 3
    if yuShu == 1:
      return False
    if yuShu == 2:
      if jiangExisted:
        return False
      jiangPos = i
      jiangExisted = True
  for i in range(0, 4):
    if i != jiangPos:
      if not Analyze(allPai[i],i==3):
        return False

  #该类牌中要包含将,因为要对将进行轮询,效率较低,放在最后
  success = False  #指示除掉“将”后能否通过
  for j in range(1, 10):  #对列进行操作,用j表示
    if allPai[jiangPos][j]>=2:
      #除去这2张将牌
      allPai[jiangPos][j] -= 2
      allPai[jiangPos][0] -= 2
      if Analyze(allPai[jiangPos],jiangPos==3):
        success=True
      #还原这2张将牌
      allPai[jiangPos][j]+=2
      allPai[jiangPos][0]+=2
      if success:
        break
  return success

#分解成“刻”“顺”组合
def Analyze(aKindPai, ziPai):
  if aKindPai[0]==0:
    return True
  #寻找第一张牌
  j = 0
  for i in range(1, 10):
    if aKindPai[i] != 0:
      j = i
      break
  result = False
  if aKindPai[j]>=3:  #作为刻牌
    #除去这3张刻牌
    aKindPai[j] -= 3
    aKindPai[0] -= 3
    result = Analyze(aKindPai,ziPai)
    #还原这3张刻牌
    aKindPai[j] += 3
    aKindPai[0] += 3
    return result
  #作为顺牌
  if (not ziPai) and (j<8) and (aKindPai[j+1]>0) and (aKindPai[j+2]>0):
    #除去这3张顺牌
    aKindPai[j] -= 1
    aKindPai[j+1] -= 1
    aKindPai[j+2] -= 1
    aKindPai[0] -= 3
    result = Analyze(aKindPai,ziPai)
    #还原这3张顺牌
    aKindPai[j] += 1
    aKindPai[j+1] += 1
    aKindPai[j+2] += 1
    aKindPai[0] += 3
    return result
  return False

if __name__ == '__main__':
  #定义手中的牌
  allPai=[
           [6,1,4,1],#万
           [3,1,1,1],#筒
           [0],#索
           [5,2,3]#字
         ]
  if Win(allPai):
    print "HU!"
  else:
    print "Not Hu!"
