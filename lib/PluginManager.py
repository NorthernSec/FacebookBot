#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-
#
# Plugin Manager
#
# Copyright (c) 2015    NorthernSec
# Copyright (c) 2015    Pieter-Jan Moreels
# This software is licensed under the Original BSD License

# Imports
import sys
import os
runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(runPath, ".."))

import importlib

from lib.ConfigReader import ConfigReader

def loadPlugins():
  conf=ConfigReader(os.path.join(runPath, "../etc/plugins.ini"))
  ppath=os.path.join(runPath, "../etc/plugins.txt")
  if not os.path.exists(ppath):
    print("[!] plugins.txt not found!")
    return []
  p=[x.split('\t') for x in open(ppath) if not x.startswith("#")]
  p=[[y.strip() for y in x if y.strip()] for x in p]
  plugins=[]
  for x in [x for x in p if len(x)==2]:
    try:
      if x[1].lower() == "load" or x[1].lower() == "default":
        i=importlib.import_module(x[0].replace("/", "."))
        plugin=i.Plugin()
        if x[1].lower() == "load":
          plugin.loadSettings(conf)
        plugins.append(plugin)
        print("[+] Loaded %s"%x[0])
    except Exception as e:
      print("[!] Failed to load module %s: "%x[0])
      print("[!]  -> %s"%e)
  return plugins
