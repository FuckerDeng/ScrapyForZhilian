
class SaveLog():
	#def __init__(self):
	#	self.file = open("mysqlError.log","w+")
	file = open("mysqlError.log","w+")

	def saveLog(errStr):
		SaveLog.file.write(errStr+"\n")

	def closeFile():
		SaveLog.file.close()