from .Layer import Layer
from .SynapticWeightMark import SynapticWeightMark
from .Neuron import Neuron
import copy

lastLayerId = 1000

class ANN :
	def __init__(self, neuronOrOtherANN, synapticWeight=None, inputAmount=None, outputAmount=None):
		if( synapticWeight == None ): # en este caso suponemos que neuronOrOtherANN es una ANN.
			self.inputAmount = neuronOrOtherANN.inputAmount
			self.outputAmount = neuronOrOtherANN.outputAmount
			self.probabilityNewNeuronInLayer = neuronOrOtherANN.probabilityNewNeuronInLayer
			self.probabilityOfNewSynapticWeight = neuronOrOtherANN.probabilityOfNewSynapticWeight
			self.probabilityOfNewUniqueSynapticWeight = neuronOrOtherANN.probabilityOfNewUniqueSynapticWeight
			self.probabilityOfNewLayer = neuronOrOtherANN.probabilityOfNewLayer
			self.inputsAmount = neuronOrOtherANN.inputsAmount
			self.outputsAmount = neuronOrOtherANN.outputsAmount
			self.useBackwardConnections = neuronOrOtherANN.useBackwardConnections
			self.layer_list = copy.deepcopy(neuronOrOtherANN.layer_list)
			self.synapticWeight_list = copy.deepcopy(neuronOrOtherANN.synapticWeight_list)
		else: # en este caso neuronOrOtherANN es Neurona
			self.inputAmount = inputAmount
			self.outputAmount = outputAmount
			self.probabilityNewNeuronInLayer = 1.0
			self.probabilityOfNewSynapticWeight = 1.0
			self.probabilityOfNewUniqueSynapticWeight = 0.0
			self.probabilityOfNewLayer = 1.0
			self.inputsAmount = 2
			self.outputsAmount = 2
			self.useBackwardConnections = True
			self.layer_list = []
			self.synapticWeight_list = []
			self.CreateInitialStructure(neuronOrOtherANN, synapticWeight)

	def CreateInitialStructure(self, neuron, synapticWeight):
		#Creando la capa de entrada
		self.layer_list.append( Layer(0, neuron) )
		for x in range(1,self.inputAmount):
			self.layer_list[0].AddNewNeuron()
		#Lo mismo pero ahora con la capa final
		self.layer_list.append( Layer(lastLayerId, neuron) )
		for x in range(1,self.outputAmount):
			self.layer_list[1].AddNewNeuron()
		#Ahora hay que conectarlos con conexiones sinapticas
		for x in range(0,self.inputAmount):
			for y in range(0,self.outputAmount):
				new_synapticWeight = synapticWeight.CreateNew()
				new_synapticWeight.SetMark( SynapticWeightMark(layerInitialIn=0, neuronInitialIn=x, layerInitialOut=lastLayerId, neuronInitialOut=y) )
				self.synapticWeight_list.append(new_synapticWeight)
				self.layer_list[0].neuron_list[x].AddOutwardConnection(new_synapticWeight)
				self.layer_list[1].neuron_list[y].AddInwardConnection(new_synapticWeight)

	def PrintInfo(self):
		print("ANN Information:\n")
		for layer in self.layer_list:
			layer.PrintInfo()
		print("\nSynaptics weights:\n")
		for synapticWeight in self.synapticWeight_list:
			synapticWeight.PrintInfo()

	#def CreateNew(self):

	def Clone(self):
		return ANN(self)

	# def CrossOver(self, other):

	# def Spread(self)

	# def GetDistance(self, other):
	
	def GetOutputs(self):
		output = []
		for neuron in layer_list[len(layer_list)-1].neuron_list:
			output.append( neuron.GetOutput() )
		return output
	
	def SetInputs(self, inputVolageList ): 
		if( len(inputVolageList) == len(layer_list[0].neuron_list) ):
			for it in range(0,len(layer_list[0].neuron_list)):
				layer_list[0].neuron_list[it].SumIncomingVoltage(inputVolageList[it])
		else:
			print("ERROR::ANN::SetInputs::InputVoltageList have a diferent size than the ANN inputs neurons. ")
			exit()


	# def MightMutate(self):

