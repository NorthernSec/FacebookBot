#!/usr/bin/env python3.3
# -*- coding: utf8 -*-
#
# Facebook Bot executable
#   Covers the initiation of the Facebook Bot
#
# Copyright (c) 2015    NorthernSec
# Copyright (c) 2015    Pieter-Jan Moreels
# This software is licensed under the Original BSD License

import getpass
import os
import sys
runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(runPath, ".."))

from lib.ConfigReader import ConfigReader as Conf
from lib.FacebookBot import FBBot

if __name__ == '__main__':
  conf=Conf(os.path.join(runPath, "../etc/bot.ini"))
  # First try to read from the config
  fbid=conf.read("Bot", "fbid",       "")
  pwd =conf.read("Bot", "password",   "")
  ua  =conf.read("Bot", "user agent", "")
  # Ask the user if we're missing anything
  if not fbid: fbid=input("Facebook user ID: ")
  if not pwd:  pwd =getpass.getpass("Facebook password: ")
  if not ua:   ua  =input("User Agent (leave blank for random): ")
  # Set user agent to None to allow the bot to choose a random one
  if not ua:   ua = None
  # Start bot
  bot = FBBot(fbid, pwd, user_agent=ua)
  bot.load_plugins()
  bot.listen()
