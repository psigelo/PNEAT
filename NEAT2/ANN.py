from .Layer import Layer
from .SynapticWeightMark import SynapticWeightMark
from .Neuron import Neuron
import copy
import random

lastLayerId = 10000

def layerComparison(layer):
	return layer.layerId

class ANN :
	def __init__(self, neuronOrOtherANN, synapticWeight=None, inputAmount=None, outputAmount=None):
		if( synapticWeight is None ): # en este caso suponemos que neuronOrOtherANN es una ANN.
			self.inputAmount = neuronOrOtherANN.inputAmount
			self.outputAmount = neuronOrOtherANN.outputAmount
			self.probabilityNewNeuronInLayer = neuronOrOtherANN.probabilityNewNeuronInLayer
			self.probabilityOfNewSynapticWeight = neuronOrOtherANN.probabilityOfNewSynapticWeight
			self.probabilityOfNewUniqueSynapticWeight = neuronOrOtherANN.probabilityOfNewUniqueSynapticWeight
			self.probabilityOfNewLayer = neuronOrOtherANN.probabilityOfNewLayer
			self.layer_list = copy.deepcopy(neuronOrOtherANN.layer_list)
			self.synapticWeight_list = copy.deepcopy(neuronOrOtherANN.synapticWeight_list)
			self.innovation = '' # No debe ser igual que la copia, este valor solo debe ser asignado en caso de que sea una ANN con innovaciones de topologia.
		else: # en este caso neuronOrOtherANN es Neurona
			self.inputAmount = inputAmount
			self.outputAmount = outputAmount
			self.probabilityNewNeuronInLayer = 0.1
			self.probabilityOfNewSynapticWeight = 0.1
			self.probabilityOfNewUniqueSynapticWeight = 0.1
			self.probabilityOfNewLayer = 0.1
			self.useBackwardConnections = False
			self.layer_list = []
			self.synapticWeight_list = []
			self.innovation=''
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

	def MightMutate(self):
		self.MightMutation_NonTopology()
		self.MightMutate_Topology()

	def MightMutation_NonTopology(self):
		for layer in self.layer_list:
			layer.MightMutate_NonTopology()
		for synapticWeight in self.synapticWeight_list:
			synapticWeight.MightMutate()

	def MightMutation_NonTopology(self):
		if( random.random() < self.probabilityOfNewLayer ):
			self.NewLayer()

		if( random.random() < self.probabilityOfNewSynapticWeight ):
			if (random.random() < probabilityOfNewUniqueSynapticWeight):
				self.CreateNewUniqueSynapticWeight()
			elif(random.random() < probabilityOfNewSynapticWeight)
				self.CreateNewSynapticWeight()

		if( random.random() < self.probabilityNewNeuronInLayer ):
			print("hola")
		if( random.random() < self.probabilityOfNewUniqueSynapticWeight ):
			print("hola")

	def FindRandomNeuronFromLayerBehindAt( self, layerBound ):
		assert layerBound != lastLayerId, "Error::ANN::FindRandomNeuronFromLayerBehindAt::layerBound is lastLayerId and not layer place."
		assert layerBound == 0, "Error::ANN::FindRandomNeuronFromLayerBehindAt::layerBound is 0"
		randomLayerPlace = random.randint(0, layerBound-1)
		randomNeuronPlace = random.randint(0, len(self.layer_list[randomLayerPlace].neuron_list)-1 )
		return {'randomLayerPlace': randomLayerPlace, 'randomNeuronPlace': randomNeuronPlace } 

	def FindRandomNeuronFromLayerAheadAt( self, layerBound ):
		assert layerBound != lastLayerId, "Error::ANN::FindRandomNeuronFromLayerBehindAt::layerBound is lastLayerId and not layer place."
		assert layerBound == len(self.layer_list[randomLayerPlace].neuron_list)-1, "Error::ANN::FindRandomNeuronFromLayerBehindAt::layerBound is the last layer"
		randomLayerPlace = random.randint(layerBound+1, len(self.layer_list[randomLayerPlace].neuron_list)-1)
		randomNeuronPlace = random.randint(0, len(self.layer_list[randomLayerPlace].neuron_list)-1 )
		return {'layer': randomLayerPlace, 'neuron': randomNeuronPlace } 

	def FindRandomNeuron(self):
		randomLayerPlace = random.randint(0, len(self.layer_list)-1)
		randomNeuronPlace = random.randint(0, len(self.layer_list[randomLayerPlace].neuron_list)-1 )
		return {'layer': randomLayerPlace, 'neuron': randomNeuronPlace } 

	def NewLayer(self):
		self.NewLayer()
		newLayerId = len(self.layer_list)-1
		layer_new = Layer(newLayerId, self.layer_list[0].neuron_list[0] )
		self.layer_list.append(layer_new)
		sorted(self.layer_list, key=layerComparison )
		
		neuronIn, neuronOut = self.FindNeuronInputAndOutputOfNewLayer(newLayerId)		
		self.CreateAndConnectANewSynapticWeight( layerInitialIn=neuronIn['layer'], neuronInitialIn=neuronIn['neuron'], layerInitialOut=newLayerId, neuronInitialOut=0 )
		self.CreateAndConnectANewSynapticWeight( layerInitialIn=newLayerId, neuronInitialIn=0, layerInitialOut=neuronOut['layer'], neuronInitialOut=neuronOut['neuron'] )

	def FindNeuronInputAndOutputOfNewLayer(self, newLayerId):
		if( useBackwardConnections ):
			nonlocal neuronIn
			nonlocal neuronOut
			neuronIn = self.FindRandomNeuron()
			neuronOut = self.FindRandomNeuron()				
		else:
			nonlocal neuronIn
			nonlocal neuronOut
			neuronIn = FindRandomNeuronFromLayerBehindAt(newLayerId) #newLayerId es igual a la posicion en el layer
			neuronOut = FindRandomNeuronFromLayerAheadAt(newLayerId)
		return neuronIn, neuronOut

	def CreateAndConnectANewSynapticWeight(self,layerInitialIn, neuronInitialIn, layerInitialOut, neuronInitialOut ):
		new_synapicWeight = synapticWeight_list.CreateNew()
		new_synapicWeight.SetMark(layerInitialIn=layerInitialIn, neuronInitialIn=neuronInitialIn, layerInitialOut=layerInitialOut, neuronInitialOut=neuronInitialOut)
		self.synapticWeight_list.append(new_synapicWeight)
		self.layer_list[layerInitialIn].neuron_list[neuronInitialIn].AddOutwardConnection(new_synapicWeight)
		self.layer_list[layerInitialOut].neuron_list[neuronInitialOut].AddInwardConnection(new_synapicWeight)

	def CreateNewUniqueSynapticWeight(self):
		attempts = 5
		for it in range(0,attempts):
			if(useBackwardConnections):
				nonlocal neuronIn 
				nonlocal neuronOut
				neuronOut = self.FindRandomNeuron()
				neuronIn  = self.FindRandomNeuron()
			else:
				nonlocal neuronIn 
				nonlocal neuronOut
				neuronIn = self.FindRandomNeuron()
				neuronOut = self.FindRandomNeuronFromLayerAheadAt(neuronIn['layer'])

			

			break

	def CreateNewSynapticWeight(self):
		#First at all is find the input and output Neurons
		if(useBackwardConnections):
			nonlocal neuronIn 
			nonlocal neuronOut
			neuronOut = self.FindRandomNeuron()
			neuronIn  = self.FindRandomNeuron()
		else:
			nonlocal neuronIn 
			nonlocal neuronOut
			neuronIn = self.FindRandomNeuron()
			neuronOut = self.FindRandomNeuronFromLayerAheadAt(neuronIn['layer'])

		CreateAndConnectANewSynapticWeight(layerInitialIn=neuronIn['layer'], neuronInitialIn=neuronIn['neuron'], layerInitialOut=neuronOut['layer'], neuronInitialOut=neuronIn['neuron'])

