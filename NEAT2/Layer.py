class Layer:
	def __init__(self, layerId, neuronExample ):
		self.layerId = layerId
		self.neuron_list = []
		self.neuron_list.append( neuronExample.CreateNew() ) 

	def AddNeuron(self, neuron):
		self.neuron_list.append(neuron)

	def MightMutate(self):
		for neuron in self.neuron_list:
			neuron.MightMutate()

	def GetDistance(self, otherLayer):
		distance = 0.0
		for it in range(0, len(self.neuron_list) ):
			distance += self.neuron_list[it].GetDistance(otherLayer.neuron_list[it])
		return distance

	def AddNewNeuron(self):
		self.neuron_list.append( self.neuron_list[0].CreateNew() )

	def PrintInfo(self):
		print("Layer ID: ", self.layerId , "information \n====================")
		for neuron in self.neuron_list:
			neuron.PrintInfo()

	def CrossOver(self, otherLayer):
		result = Layer(self.layerId, self.neuron_list[0].CrossOver(otherLayer.neuron_list[0]))
		for it in range(1, len(self.neuron_list) ):
			result.AddNeuron( self.neuron_list[it].CrossOver(otherLayer.neuron_list[it]) )
		return result

	def CreateNew(self):
		''' Se crea una capa de neuronas con la misma cantidad de neuronas que esta '''
		result = Layer(self.layerId, self.neuron_list[0].CreateNew())
		for it in range(1, len(self.neuron_list) ):
			result.AddNeuron( self.neuron_list[it].CreateNew() )
		return result

	# def Clone(self)
	# 	result = Layer(self.layerId, self.neuron_list[0].Clone())
	# 	for it in range(1, len(self.neuron_list) ):
	# 		result.AddNeuron( self.neuron_list[it].Clone() )
	# 	return result