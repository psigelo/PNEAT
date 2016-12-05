from brian2 import *
from NEAT2.BrianANN import BrianANN
from NEAT2.Organism import Organism
from NEAT2.Race import Race 
from NEAT2.Specie import Specie 
from NEAT2.Life import Life 
import matplotlib.pyplot as plt


import random
import time
prefs.codegen.target = 'numpy'
#prefs.codegen.target = 'weave'
#codegen.string_expression_target = 'numpy'
def experiment(orgm):
	orgm.ann.layerOfNeurons[0]['layer'].I = [1.0 for it in range(orgm.ann.layerOfNeurons[0]['layer'].N) ]
	orgm.ann.network.run(20*ms)
	orgm.fitness = random.random()


if __name__ == '__main__':
	eqs = '''
	dv/dt = (I-v)/(5*ms) : 1
	I : 1
	'''

	ann = BrianANN(equation=eqs, inputsAmount=10, outputsAmount=20, threshold='v>0.6', newLayerRate=0.08)
	orgm = Organism(ann)
	#ann.visualise_connectivity()
	race = Race(orgm, maxAmountOfOrganismsInRace=5)

	for orgm in race.organisms:
		orgm.fitness = random.random()

	specie = Specie(race)

	life = Life(specie, maxAmountOfSpecies=3)

	for it in range(5):
		allOrgms = life.GetAllOrganismsList()
		for orgm in allOrgms:
			experiment(orgm)
		life.Epoch()
		print('species: ',len(life.species))
	allOrgms = life.GetAllOrganismsList()
	allOrgms[2].ann.visualise_connectivity()
