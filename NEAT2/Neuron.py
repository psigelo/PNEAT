import random

class Neuron :
	''' Neuron es una clase abstracta que representa una neurona. '''
	def __init__(self):
		super().__init__()
		self.output = float(0.0)
		self.inputVoltageAccum = float(0.0)
		self.inwardConnections = []
		self.outwardConnections = []

	def SumIncomingVoltage(self, voltage):
		self.inputVoltageAccum += voltage

	def GetOutput(self):
		return self.output

	def CrossOver(self, other):
		if(random.random() < 0.5):
			return (self.Clone())
		else:
			return (other.Clone())

	def AddInwardConnection(self, SynapticWeight):
		self.inwardConnections.append(SynapticWeight)

	def AddOutwardConnection(self, SynapticWeight):
		self.outwardConnections.append(SynapticWeight)


