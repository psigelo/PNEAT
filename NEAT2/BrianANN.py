from brian2 import *
import numpy as np
import random
import matplotlib.pyplot as plt

def getLayerKey(layer):
	return layer['id']

class BrianANN():
	def __init__(self, equation=None, inputsAmount=None, outputsAmount=None, threshold=None, otherBrianANN=None, newSynapseRate=0.1, newUniqueSynapseRate=0.1, newLayerRate=0.01, useBackwardConnections=False, minNeuronsInHiddenLayer=5, maxNeuronsInHiddenLayer=20, hiddenSynapsesRate=0.5, probabilityOfChangeSynapticWeight=0.2 ):
		if(otherBrianANN is not None):
			#Primero los parametros.
			self.newSynapseRate = otherBrianANN.newSynapseRate
			self.newUniqueSynapseRate = otherBrianANN.newUniqueSynapseRate
			self.newLayerRate = otherBrianANN.newLayerRate
			self.minNeuronsInHiddenLayer = otherBrianANN.minNeuronsInHiddenLayer
			self.maxNeuronsInHiddenLayer = otherBrianANN.maxNeuronsInHiddenLayer
			self.hiddenSynapsesRate = otherBrianANN.hiddenSynapsesRate
			self.__maxWeight__ = otherBrianANN.__maxWeight__
			self.__minWeight__ = otherBrianANN.__minWeight__
			self.inputsAmount = otherBrianANN.inputsAmount
			self.outputsAmount = otherBrianANN.outputsAmount
			self.equation = otherBrianANN.equation
			self.threshold = otherBrianANN.threshold
			self.useBackwardConnections = otherBrianANN.useBackwardConnections
			self.probabilityOfChangeSynapticWeight = otherBrianANN.probabilityOfChangeSynapticWeight
			
			self.layerOfNeurons = []
			self.synapses = []
			self.isNewSpecie = False

			# Las capas de neuronas.
			for it in range(len(otherBrianANN.layerOfNeurons)):
				self.layerOfNeurons.append( {'layer':NeuronGroup(otherBrianANN.layerOfNeurons[it]['layer'].N, self.equation, threshold=self.threshold, reset='v=0', method='linear' ), 'id': otherBrianANN.layerOfNeurons[it]['id']})
			# Ahora las conexiones synapticas
			currentLayer = 0
			for it in range(len(otherBrianANN.synapses)):
				if(it%2 == 0):
					synapse = Synapses(self.layerOfNeurons[currentLayer]['layer'],self.layerOfNeurons[len(self.layerOfNeurons)-1]['layer'], 'w : 1', on_pre='v_post += w')
					synapse.connect(i=np.array(otherBrianANN.synapses[it].i), j=np.array(otherBrianANN.synapses[it].j))
					synapse.w = otherBrianANN.synapses[it].w
					self.synapses.append(synapse)
				else:
					synapse = Synapses(self.layerOfNeurons[currentLayer]['layer'],self.layerOfNeurons[currentLayer+1]['layer'], 'w : 1', on_pre='v_post += w')
					synapse.connect(i=np.array(otherBrianANN.synapses[it].i), j=np.array(otherBrianANN.synapses[it].j))
					synapse.w = otherBrianANN.synapses[it].w
					self.synapses.append(synapse)
					currentLayer = currentLayer + 1

			# Se crea la red
			self.network = Network()
			for it in range(len(self.layerOfNeurons)):
				self.network.add(self.layerOfNeurons[it]['layer'])
			for it in range(len(self.synapses)):
				self.network.add(self.synapses[it])
			
		else:
			#Crear una red neuronal vacia de dos capas, la primera es la de entrada la segunda la de salida.
			#Se supone que equation, inpustAmount, threshold y outputsAmount estan bien creadas.
			self.newSynapseRate = newSynapseRate
			self.newUniqueSynapseRate = newUniqueSynapseRate
			self.newLayerRate = newLayerRate
			self.minNeuronsInHiddenLayer = minNeuronsInHiddenLayer
			self.maxNeuronsInHiddenLayer = maxNeuronsInHiddenLayer
			self.hiddenSynapsesRate = hiddenSynapsesRate
			self.__maxWeight__ = 1.0 
			self.__minWeight__ = -1.0
			self.inputsAmount = inputsAmount
			self.outputsAmount = outputsAmount
			self.equation = equation
			self.threshold = threshold
			self.layerOfNeurons = []
			self.synapses = []
			self.useBackwardConnections = useBackwardConnections
			self.probabilityOfChangeSynapticWeight = probabilityOfChangeSynapticWeight

			#Primero las neuronas 
			layerNeuronInput = NeuronGroup(inputsAmount, equation, threshold=self.threshold, reset='v=0', method='linear' )
			#layerNeuronInput.layerId=0
			layerNeuronOutput = NeuronGroup(outputsAmount, equation, threshold=self.threshold, reset='v=0', method='linear' )
			
			#segundo las conexiones synapticas
			feedForwardSynapses = Synapses(layerNeuronInput,layerNeuronOutput, 'w : 1', on_pre='v_post += w')

			#Creando las conexiones full conectadas.
			inputsOfSynapses = np.array([ i for i in range(inputsAmount) for j in range(outputsAmount) ])
			outputsOfSynapses = np.array([ j for i in range(inputsAmount) for j in range(outputsAmount) ])
			#Creando los pesos aleatorios.
			feedForwardSynapses.connect(i=inputsOfSynapses, j=outputsOfSynapses)
			feedForwardSynapses.w = np.array([ random.uniform(self.__minWeight__,self.__maxWeight__) for i in range(inputsAmount) for j in range(outputsAmount) ])

			self.synapses.append(feedForwardSynapses)
			self.layerOfNeurons.append({'layer': layerNeuronInput, 'id' : 0})
			self.layerOfNeurons.append({'layer':layerNeuronOutput, 'id': 10000})
			self.network = Network()
			self.network.add(feedForwardSynapses) 
			self.network.add(layerNeuronInput)
			self.network.add(layerNeuronOutput)

	def run(self, timeInMs):
		self.network.run(timeInMs*ms)

	def MightMutate(self):
		if( random.random() < self.newLayerRate ): 
			self.NewLayer()
		self.MightMutateSynapticWeightsValues()

	def CrossOver(self, otherBrianANN):
		result = BrianANN(otherBrianANN=self) # cloning this
		for it_1 in range(len(result.synapses)) :
			for it_2 in range(len(result.synapses[it_1].w)):
				if(random.random() < 0.5):
					result.synapses[it_1].w[it_2] = otherBrianANN.synapses[it_1].w[it_2]	
		return result	

	def GetDistance(self, otherBrianANN):
		distance = 0.0
		for it in range(len(self.synapses)) :
				distance = distance + dot(otherBrianANN.synapses[it].w - self.synapses[it].w,otherBrianANN.synapses[it].w - self.synapses[it].w) #euclidean vectorial distance.
		if(distance == 0):
			print('BrianANN::GetDistance::Warning::distance is 0.')
		return distance 
		
	def visualise_connectivity(self):
		#Se imprimen las neuronas
		for it in range(len(self.layerOfNeurons)):
			plt.plot(ones(self.layerOfNeurons[it]['layer'].N)*it, arange(self.layerOfNeurons[it]['layer'].N), 'ok', ms=5)
		#Se imprimen las conexiones synapticas
		self.currentLayer = 0
		for it in range(len(self.synapses)):
			for i, j in zip(self.synapses[it].i, self.synapses[it].j):
				if(it%2 == 0):
					plt.plot([self.currentLayer,len(self.layerOfNeurons)-1 ], [i, j], ':r')
				else:
					plt.plot([self.currentLayer, self.currentLayer+1 ], [i, j], ':g')
			if(it%2 != 0):
				self.currentLayer = self.currentLayer + 1
		plt.xlim(-0.1, len(self.layerOfNeurons)-0.9)
		max_val = 0
		for it in range(len(self.layerOfNeurons)):
			max_val = max(max_val,self.layerOfNeurons[it]['layer'].N)
		plt.ylim(-1, max_val)
		plt.show()
	def NewSynapse(self):
		'''
 			Se crea una conexion synaptica entre dos neuronas sin importar si existe una previamente. 

 			Procedimiento: 
 				1: Se encuentran las neuronas aleatoreamente.
 				2: Se crea la nueva conexion synaptica
 				3: Se asigna un peso aleatorio a la conexion synaptica nueva
 		'''
		# pre_randomLayer = random.randint(0,len(self.layerOfNeurons)-1)
		# post_randomLayer = random.randint(0,len(self.layerOfNeurons)-1)
		# pre_neuron = random.randint(0,self.layerOfNeurons[pre_randomLayer].N -1)
		# post_neuron = random.randint(0,self.layerOfNeurons[post_randomLayer].N -1)
		pass


	def NewUniqueSynapse(self):
		pass

	def NewLayer(self):
		self.isNewSpecie = True
		#primero creamos el layer, luego las conexiones sinapticas.
		numNeurons = random.randint(self.minNeuronsInHiddenLayer, self.maxNeuronsInHiddenLayer)
		newHiddenLayer = NeuronGroup(numNeurons, self.equation, threshold=self.threshold, reset='v=0', method='linear' )
		self.layerOfNeurons.append( {'layer': newHiddenLayer, 'id' : len(self.layerOfNeurons)-1 } )
		self.layerOfNeurons = sorted(self.layerOfNeurons, key=getLayerKey) # se ordenan los layer segun su id

		# ahora se crean las conexiones synapticas por lo pronto sera solo una capa con otra para evitar complicaciones.  Luego se habilitara todas con todas.
		
		synapses_pre = Synapses(self.layerOfNeurons[len(self.layerOfNeurons)-3]['layer'],self.layerOfNeurons[len(self.layerOfNeurons)-2]['layer'], 'w : 1', on_pre='v_post += w')
		synapses_post = Synapses(self.layerOfNeurons[len(self.layerOfNeurons)-2]['layer'],self.layerOfNeurons[len(self.layerOfNeurons)-1]['layer'], 'w : 1', on_pre='v_post += w')

		syn_pre_pre_amount = self.layerOfNeurons[len(self.layerOfNeurons)-3]['layer'].N
		syn_pre_post_amount = self.layerOfNeurons[len(self.layerOfNeurons)-2]['layer'].N
		syn_post_pre_amount = syn_pre_post_amount
		syn_post_post_amount = self.layerOfNeurons[len(self.layerOfNeurons)-1]['layer'].N

		# Se crean pares (i,j) de todas las posibles conexiones pero bajo la probabilidad definida por hiddenSynapsesRate
		syn_pre_connect = np.array([ (i,j) for i in range(syn_pre_pre_amount) for j in range(syn_pre_post_amount) if random.random() < self.hiddenSynapsesRate ])
		syn_post_connect = np.array([ (i,j) for i in range(syn_post_pre_amount) for j in range(syn_post_post_amount) if random.random() < self.hiddenSynapsesRate ])

		synapses_pre.connect(i=syn_pre_connect[:,0], j=syn_pre_connect[:,1])
		synapses_post.connect(i=syn_post_connect[:,0], j=syn_post_connect[:,1])

		synapses_pre.w = np.array([ random.uniform(self.__minWeight__,self.__maxWeight__) for i in range(len(syn_pre_connect[:,0]))])
		synapses_post.w = np.array([ random.uniform(self.__minWeight__,self.__maxWeight__) for i in range(len(syn_post_connect[:,0]))])

		self.synapses.append(synapses_pre)
		self.synapses.append(synapses_post)

		self.network.add( newHiddenLayer )
		self.network.add( synapses_pre )
		self.network.add( synapses_post )

	def MightMutateSynapticWeightsValues(self):
		for synapse in self.synapses :
			for it in range(len(synapse.w)):
				if(random.random() < self.probabilityOfChangeSynapticWeight):
					synapse.w[it] = random.uniform(self.__minWeight__,self.__maxWeight__)

	def CreateNew(self):
		result = BrianANN(otherBrianANN=self)
		result.MightMutateSynapticWeightsValues()
		result.MightMutateSynapticWeightsValues()
		return result

	def Clone(self):
		return BrianANN(otherBrianANN=self)