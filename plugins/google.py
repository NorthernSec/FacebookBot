import os
import sys
_runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(_runPath, ".."))

from lib.Plugin import Plugin
from lib.Toolkit import google_search

class Plugin(Plugin):
  def __init__(self):
    self.default="No results found"
    self.noID   ="Needs a search result ID"
    self.wrongID="This ID is not in the searchResults"
    self.searchResults={}

  def loadSettings(self, conf):
    self.default=conf.read("Google", "default",  "No results found")
    self.noID   =conf.read("Google", "no id",    "This ID is not in the searchResults")
    self.wrongID=conf.read("Google", "wrong id", "This ID is not in the searchResults")

  def checkCommand(self, command, arguments):
    if command.lower() in ["google", "g"]:
      result=google_search(arguments)
      if not result:
        return self.default
      else:
        reply=""
        self.searchResults={}
        ID=1
        for r in result:
          reply+=("(%s) - %s\n%s\n\n"%(ID, r[0], r[1]))
          self.searchResults[ID]=r
          ID+=1
      return reply
    
    elif command.lower() in ["google-open", "gopen"]:
      if not arguments: return self.noID
      try:
        _id=int(arguments.split())
        return "%s\n%s\n%s"%(self.searchResults[_id])
      except:
        return self.wrongID

  def getStatus(self, rType="text"):
    if rType == "json": return "{'default_reply': %s}"%(self.default)
    else:               return "Default reply: %s"%(self.default)
