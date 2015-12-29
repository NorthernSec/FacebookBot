import os
import sys
_runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(_runPath, ".."))

from lib.Plugin import Plugin

class Plugin(Plugin):
  def __init__(self):
    self.reply="pong"

  def loadSettings(self, conf):
    self.reply=conf.read("Ping", "reply", "pong")

  def checkCommand(self, command, arguments):
    if command.lower() == "ping":
      return self.reply

  def getStatus(self, rType="text"):
    if rType == "json": return "{'reply': %s}"%(self.reply)
    else:               return "Reply status: %s"%(self.reply)
