import os
import sys
_runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(_runPath, ".."))


import requests
import html5lib
from html5lib import treebuilders

from lib.Plugin import Plugin
from lib.Toolkit import google_search

class Plugin(Plugin):
  def __init__(self):
    self.noAnswers  = "No answers found"
    self.parser     = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("lxml"))
    self.answerPath = ('.//{http://www.w3.org/1999/xhtml}div[@class="answer"]//'
                       '{http://www.w3.org/1999/xhtml}div[@class="post-text"]')
    self.query      = 'www.stackoverflow.com '
    self.searchResults = {}

  def loadSettings(self, conf):
    self.noAnswers=conf.read("StackOverflow", "no answers", "No answers found")

  def checkCommand(self, command, arguments):
    if command.lower() in ["stackoverflow", "stack", "so"]:
      self.searchResults = {}
      urls = [ x[2] for x in google_search(self.query + arguments) ]
      if isinstance(urls, str):
        print(urls)
        return self.noAnswers
      if len(urls) == 0: return self.noAnswers # no answers
      else:
        ID=1
        for url in urls:
          answers=[]
          dom = self.parser.parse(requests.get(url).text)
          for answer in dom.findall(self.answerPath):
            answers.append((''.join(["%s\n"%txt.strip() for txt in answer.itertext()])).strip())
          if len(answers) != 0: self.searchResults[ID]={"url": url, "answers":answers}
          ID+=1
        reply=[]
        for r in self.searchResults.keys():
          reply.append("%s\n%s"%(self.searchResults[r]['url'], self.searchResults[r]['answers'][0]))
        return reply

  def getStatus(self, rType="text"):
    if rType == "json": return "{'no answers': %s}"%(self.noAnswers)
    else:               return "No answers: %s"%(self.noAnswers)
