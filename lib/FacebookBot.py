#!/usr/bin/env python3.3
# -*- coding: utf8 -*-
#
# Facebook Bot
#   Binds to a Facebook account and listens to private messages until a
#   user sends it a command, and checks if one of the plugins applies,
#   and return the output if it does
#
# Copyright (c) 2015    NorthernSec
# Copyright (c) 2015    Pieter-Jan Moreels
# This software is licensed under the Original BSD License

import os
import sys
import time
runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(runPath, ".."))

try:
  import fbchat
except:
  sys.exit("Please make sure you have all dependencies installed")

import lib.PluginManager as PM

class FBBot():
  def __init__(self, fid, pwd, ua=None):
    self.client = fbchat.Client(fid, pwd, user_agent=ua)
    self.plugins= PM.loadPlugins()
    if self.client:
      self.lastTextId = self.client.getThreadList(0,1)[0].last_message_id
    else:
      sys.exit("Could not log in")

  def checkAndInterprete(self):
    #self.client = fbchat.Client(fid, pwd, user_agent=ua)
    last = self.client.getThreadList(0,1)[0]
    if last.last_message_id != self.lastTextId:
      addr = last.thread_fbid
      text = last.snippet
      reply = self.analyze(text)
      if reply:
        self.client.sendMessage(reply, addr)

  def analyze(self, text):
    #split=text.split(" ")
    #command = split.pop(0).lower()
    #options = split
    for p in self.plugins:
      result = p.checkCommand(text)
      if result: return result
    #if command == "ping":
    #  return "pong"
    return False

  def start(self):
    print("Bot is ready")
    try:
      while True:
        self.checkAndInterprete()
        time.sleep(0.5)
    except KeyboardInterrupt:
      print("Bot stopped")
