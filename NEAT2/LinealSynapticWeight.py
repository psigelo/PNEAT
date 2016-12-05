from .__abstract__SynapticWeight import __abstract__SynapticWeight
from .Parameter import Parameter
import copy
import random

class LinealSynapticWeight (__abstract__SynapticWeight):
	def __init__(self, other=None):
		super().__init__()
		if(other == None):
			self.weight = Parameter(probabilityOfRandomMutation=0.1, maximumPercentVariation=0.1, maxAdmissibleValue=1.0, minAdmissibleValue=-1.0)
			self.probabilityOfEnableADisabledConnection = float(0)
			self.constantDistanceOfSynapticWeightValue = float(1)
			self.mutationProbability = float(0.2)
		else:
			self.weight = copy.copy(other.weight)
			self.probabilityOfEnableADisabledConnection = other.probabilityOfEnableADisabledConnection 
			self.constantDistanceOfSynapticWeightValue = other.constantDistanceOfSynapticWeightValue 
			self.mutationProbability = other.mutationProbability 

	def Spread(self):
		self.output = self.inputVoltage * self.weight.value

	def MightMutate(self):
		if(random.random() < self.mutationProbability):
			self.weight.Mutate() 

	def PrintInfo(self):
		print ("LinealSynapticWeight Information\n",
				"weight: ", self.weight.value, "\n",
				"constantDistanceOfSynapticWeightValue:", self.constantDistanceOfSynapticWeightValue, "\n",
				"mutationProbability: " , self.mutationProbability)

	def Clone(self):
		return LinealSynapticWeight(self)

	def CreateNew(self):
		result = LinealSynapticWeight(self)
		result.weight.Random()
		return result