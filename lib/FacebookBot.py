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

if sys.version_info < (3, 0):
  from urllib import quote
else:
  from urllib.parse import quote
    
try:
  import fbchat
except:
  sys.exit("Please make sure you have all dependencies installed")

import lib.PluginManager as PM

class FBBot(fbchat.Client):
  def __init__(self, fbid, pwd, user_agent=None, debug=False):
    super(self.__class__, self).__init__(fbid, pwd, user_agent, debug)
    self.plugins=[]
  
  def load_plugins(self):
    # make plugin manager a class
    self.plugins= PM.loadPlugins()

  def on_message(self, mid, fbid, name, message, meta):
    self.markAsDelivered(fbid, mid) # Mark message as delivered to prevent server from spamming us
    self.markAsRead(fbid)           # Mark as read to have user interactiveness
    if fbid == self.uid: return     # We don't want to deal with our own messages
    message=message.strip()
    if message:
      command, args = message.split(" ", 1) if " " in message else (message, "")
      for p in self.plugins:
        print(p)
        result=p.checkCommand(command, args)
        if result:
          if type(result) is not list: result=[result]
          for message in result:
            self.send(fbid, message)
            print(message)
            return
            time.sleep(0.2)
          return
