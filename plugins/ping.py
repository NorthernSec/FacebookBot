
class Plugin():
  def __init__(self):
    self.reply="pong"

  def loadSettings(self, conf):
    self.reply=conf.read("Ping", "reply", "pong")

  def checkCommand(self, text):
    return self.reply

  def getStatus(self, rType="text"):
    if rType == "json": return "{'reply': %s}"%(self.reply)
    else:               return "Reply status: %s"%(self.reply)
