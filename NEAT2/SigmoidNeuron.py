from .Neuron import Neuron
from .Parameter import Parameter
import math
import copy
import random

def Sigmoid(x):
	return  1.0 / (1.0 + math.exp(-x))


class SigmoidNeuron (Neuron): 
	''' Representa neuronas basicas tipo sigmoidales. '''
	def __init__(self, other = None ):
		super().__init__()
		if ( other == None ) :
			self.constantDistanceOfBias = float (0.2)
			self.constantDistanceOfSigmoidConstant = float (0.2)
			self.lastInputAccum = float (0.0)
			self.mutationProbability = float (0.2)
			self.bias = Parameter( probabilityOfRandomMutation=0.1, maximumPercentVariation=0.1, maxAdmissibleValue=0.1, minAdmissibleValue=-0.1 )
			self.sigmoidConstant = Parameter( probabilityOfRandomMutation=0.1, maximumPercentVariation=0.1, maxAdmissibleValue=6.0, minAdmissibleValue=3.0 )
		else:
			self.constantDistanceOfBias = other.constantDistanceOfBias 
			self.constantDistanceOfSigmoidConstant = other.constantDistanceOfSigmoidConstant 
			self.lastInputAccum = other.lastInputAccum 
			self.mutationProbability = other.mutationProbability
			self.bias = copy.copy(other.bias)
			self.sigmoidConstant = copy.copy(other.sigmoidConstant)

	def GetDistance(self, other):
		return self.constantDistanceOfBias * abs( self.bias.value - other.bias.value ) + self.constantDistanceOfSigmoidConstant * abs( self.sigmoidConstant.value - other.sigmoidConstant.value )

	def Spread(self):
		self.output = sigmoid( self.sigmoidConstant.value * (self.inputVoltageAccum + self.bias.value) )

	def PrintInfo(self):
		print ("SigmoidNeuron information \n",    
			"constantDistanceOfBias: ", self.constantDistanceOfBias , "\n" ,
			"constantDistanceOfSigmoidConstant: ", self.constantDistanceOfSigmoidConstant , "\n" ,
			"lastInputAccum: ", self.lastInputAccum , "\n" ,
			"mutationProbability: ", self.mutationProbability , "\n" ,
			"bias: ", self.bias.value, "\n" ,
			"sigmoidConstant: ", self.sigmoidConstant.value)

	def MightMutate(self):
		if( random.radom() < self.mutationProbability ):
			self.bias.Mutate()
			self.sigmoidConstant.Mutate()

	def CreateNew(self):
		result = SigmoidNeuron(self)
		result.bias.Random()
		result.sigmoidConstant.Random()
		return result

	def Clone(self):
		return SigmoidNeuron(self)