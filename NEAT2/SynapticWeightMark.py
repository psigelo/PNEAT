class SynapticWeightMark:
	''' Marca de conexion sinaptica, es la marca que identifica a una conexion sinaptica (son las neuronas de entrada y salida en el fondo.) '''
	def __init__(self, layerInitialIn, neuronInitialIn, layerInitialOut, neuronInitialOut):
		self.layerInitialOut = layerInitialOut
		self.layerInitialIn = layerInitialIn
		self.neuronInitialOut = neuronInitialOut
		self.neuronInitialIn = neuronInitialIn
		self.output = 0.0
		self.inputVoltage = 0.0

	def GetMark(self):
		return {'layerInitialIn': layerInitialIn, 'layerInitialOut': layerInitialOut, 'neuronInitialOut':neuronInitialOut, 'neuronInitialIn':neuronInitialIn } 

	def GetOutput(self):
		return self.output

	def SetInputVoltage(self, inputVoltage):
		self.inputVoltage = inputVoltage