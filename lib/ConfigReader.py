#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-
#
# Configuration Reader
#
# Copyright (c) 2015    NorthernSec
# Copyright (c) 2015    Pieter-Jan Moreels
# This software is licensed under the Original BSD License

# Imports
import configparser

class ConfigReader():
  def __init__(self, file):
    self.ConfigParser = configparser.ConfigParser()
    self.ConfigParser.read(file)

  def read(self, section, item, default):
    result = default
    try:
      if type(default) == bool:
        result = self.ConfigParser.getboolean(section, item)
      elif type(default) == int:
        result = self.ConfigParser.getint(section, item)
      else:
        result = self.ConfigParser.get(section, item)
    except:
      pass
    return result






