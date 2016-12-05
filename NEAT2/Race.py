import numpy as np
def getKeyOrganism(orgm):
	return orgm.fitness

class Race:
	def __init__(self, organismSeed, maxAmountOfOrganismsInRace=20, oldRaceYears=4, percentOfOrgmsProtected=0.6):
		self.maxAmountOfOrganismsInRace = maxAmountOfOrganismsInRace
		self.organisms = []
		self.newSpecieCandidates = []
		self.fitnessMean=0.0
		self.oldRaceYears = oldRaceYears
		self.years = 0
		self.isOld = False
		self.percentOfOrgmsProtected = percentOfOrgmsProtected
		for it in range(maxAmountOfOrganismsInRace):
			self.organisms.append(organismSeed.CreateNew())

	def Epoch(self):
		self.years = self.years + 1
		if(self.years > self.oldRaceYears):
			self.isOld = True
		temporalFathers = self.organisms
		self.organisms = []
		fitnessList = []
		for it in range(len(temporalFathers)):
			fitnessList.append(temporalFathers[it].fitness)

		fitnessList = np.array(fitnessList) / sum(fitnessList) # normalizando
		for it in range(self.maxAmountOfOrganismsInRace):
			fathers = np.random.choice(temporalFathers, size=2, replace=False, p=fitnessList) # se obtiene el padre y la madre
			child = fathers[0].CrossOver(fathers[1])
			if(not child.ann.isNewSpecie):
				self.organisms.append(child)
			else:
				self.newSpecieCandidates.append(child)

	def EraseWorseProcess(self):
		self.organisms = sorted(self.organisms, key=getKeyOrganism)
		amountOfProtectedOrgms = int (self.maxAmountOfOrganismsInRace * self.percentOfOrgmsProtected)
		amountOfOrganisms = len(self.organisms)

		amountOrganismToErase = amountOfOrganisms - amountOfProtectedOrgms
		if(amountOrganismToErase > 0) :
			for it in range(amountOrganismToErase) :
				del self.organisms[0]

	def GetFitnessMean(self):
		fitnessMean = 0.0
		for orgm in self.organisms:
			fitnessMean = fitnessMean + orgm.fitness
		fitnessMean = fitnessMean / float(len(self.organisms))
		return fitnessMean