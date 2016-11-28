import random

class Parameter:
	''' Parameter Class: Clase que representa los parametros internos de la red. '''
	def __init__(self, probabilityOfRandomMutation, maximumPercentVariation, maxAdmissibleValue, minAdmissibleValue):
		self.probabilityOfRandomMutation = probabilityOfRandomMutation;
		self.maximumPercentVariation = maximumPercentVariation;
		self.maxAdmissibleValue = maxAdmissibleValue;
		self.minAdmissibleValue = minAdmissibleValue;		
		self.value = random.uniform(self.minAdmissibleValue, self.maxAdmissibleValue)

	def Random(self):
		self.value = random.uniform(self.minAdmissibleValue, self.maxAdmissibleValue)

	def Mutate(self):
		if random.random() < self.probabilityOfRandomMutation :
			self.value = random.uniform(self.minAdmissibleValue, self.maxAdmissibleValue)
		else:
			self.value = random.uniform(self.minAdmissibleValue, self.maxAdmissibleValue) * self.maximumPercentVariation + self.value * (1.0-self.maximumPercentVariation)