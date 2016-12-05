from .Race import Race 
from .Specie import Specie 
import random
def getSpecieKey(specie):
	return specie.GetFitnessMean()

class Life:
	def __init__(self, specie, maxAmountOfSpecies=10, percentOfSpeciesProtected=0.5, worseSpecieElimintaionRate=0.3):
		self.species = []
		self.maxAmountOfSpecies = maxAmountOfSpecies
		self.species.append(specie)
		self.worseSpecieElimintaionRate = worseSpecieElimintaionRate
		self.percentOfSpeciesProtected = percentOfSpeciesProtected

	def Epoch(self):
		self.EraseWorseProcess()
		for specie in self.species:
			specie.Epoch()
		attempts = 5
		while(attempts > 0 and len(self.species) < self.maxAmountOfSpecies):
			randSpecie = random.randint(0,len(self.species)-1)

			randRace = random.randint(0,len(self.species[randSpecie].races)-1) 
			amountCandidates = len( self.species[randSpecie].races[randRace].newSpecieCandidates)
			
			if(amountCandidates>0):
				randomOrgm = random.randint(0,amountCandidates-1)
				orgm = self.species[randSpecie].races[0].newSpecieCandidates[randomOrgm]
				del self.species[randSpecie].races[0].newSpecieCandidates[randomOrgm]
				self.species.append(Specie(Race(orgm)) )
			attempts = attempts -1

	def EraseWorseProcess(self):
		for specie in self.species:
			specie.EraseWorseProcess()
		self.EraseWorseSepcies()

	def EraseWorseSepcies(self):
		if(len(self.species) > self.maxAmountOfSpecies * self.percentOfSpeciesProtected ):
			self.species = sorted(self.species, key=getSpecieKey)
			for it in range(len(self.species)):
				if(self.species[it].isOld):
					if( random.random() < self.worseSpecieElimintaionRate ):
						del self.species[it]
					break # solo se intenta una vez

	def GetAllOrganismsList(self):
		result = []
		for specie in self.species:
			for race in specie.races:
				for orgm in race.organisms:
					result.append(orgm)
		return result