from NEAT2.SigmoidNeuron import SigmoidNeuron
from NEAT2.LinealSynapticWeight import LinealSynapticWeight
from NEAT2.ANN import ANN

if __name__ == '__main__':
	sn1 = SigmoidNeuron()
	lsw = LinealSynapticWeight()
	ann = ANN(sn1, lsw, 2,2)
	ann.PrintInfo()
	# bn1 = SigmoidNeuron()

	# bn2 = SigmoidNeuron(bn1)
	# print("bn1.bias.value: ", bn1.bias.value)
	# print("bn2.bias.value: ", bn2.bias.value)

	# print("bn1 change value to 10")
	# bn1.bias.value = 10.0
	# print("AFTER: bn1.bias.value: ", bn1.bias.value)
	# print("AFTER: bn2.bias.value: ", bn2.bias.value)
	# print ("Distance between both: ", bn1.GetDistance(bn2) )
	# bn1.PrintInfo()

	# lsw = LinealSynapticWeight()
	# lsw.PrintInfo()
	# lsw.MightMutate()
	# lsw.PrintInfo()
