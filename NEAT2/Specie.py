def getKeyRace(race):
	return race.GetFitnessMean()

class Specie:
	def __init__(self, race, maxAmountOfRaces=1, oldSpeciesAge=5, percentOfSpeciesProtected=0.5, worseRaceElimintaionRate=0.3):
		self.maxAmountOfRaces = maxAmountOfRaces
		self.races = []
		self.races.append(race)
		self.years = 0
		self.isOld = False
		self.oldSpeciesAge = oldSpeciesAge
		self.fitnessMean = 0.0


	def Epoch(self):
		self.years = self.years + 1 
		if(self.years >= self.oldSpeciesAge):
			self.isOld = True
		for race in self.races:
			race.Epoch()

	def EraseWorseProcess(self):
		for race in self.races:
			race.EraseWorseProcess()
		self.EraseWorseRace()

	def EraseWorseRace(self):
		self.races = sorted(self.races, key=getKeyRace)
		for it in range(len(self.races)):
			if(self.races[it].isOld):
				if(random.random() < self.worseRaceElimintaionRate ):
					del self.races[it]
				break

	def GetFitnessMean(self):
		fitnessMean = 0.0
		for race in self.races:
			fitnessMean = fitnessMean + race.GetFitnessMean()
		fitnessMean = fitnessMean / float(len(self.races))
		return fitnessMean