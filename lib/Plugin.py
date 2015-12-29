class Plugin():
  def __init__(self):
    pass

  def loadSettings(self, conf):
    pass

  def checkCommand(self, command, arguments):
    return

  def getStatus(self, rType="text"):
    if rType == "json": return "{}"
    else:               return ""
