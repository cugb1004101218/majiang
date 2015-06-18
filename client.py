#!/usr/bin/env python
# encoding: utf-8

import zerorpc
import sys

if __name__ == '__main__':
  print "please input your name: "
  line = sys.stdin.readline()
  name = line.strip()
  c = zerorpc.Client()
  c.connect("tcp://127.0.0.1:1111")
  c.Join(name)
  print c.Info(name)
  while True:
    line = sys.stdin.readline()
    if line.strip() == "exit":
      break
    line = line.strip()
    if line == "start":
      c.Start(name)
    elif line == "ready":
      c.Ready(name)
    elif line == "info":
      print c.Info(name)
    elif line == "take":
      print c.Take(name)
    elif line.strip().split(' ')[0] == "throw":
      tokens = line.strip().split(' ')
      if len(tokens) < 3:
        continue
      x = int(tokens[1])
      y = int(tokens[2])
      print c.Throw(name, x, y)
