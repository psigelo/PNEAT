class __abstract__SynapticWeight:
	''' SynapticWright es una clase abstracta (en terminos de c++) la cual '''
	def __init__(self, mark = None):
		self.output = 0.0
		self.inputVoltage = 0.0
		if(mark != None):
			self.mark = SynapticWeightMark()

	def SetMark(self, mark):
		self.mark = mark

	def GetMark(self):
		return self.mark

	def GetOutput(self):
		return self.output

	def SetInputVoltage(self, inputVoltage):
		self.inputVoltage = inputVoltage

	def CrossOver(self, other):
		if(random.random() < 0.5):
			return (self.Clone())
		else:
			return (other.Clone())
