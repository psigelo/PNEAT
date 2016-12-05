class Organism:
	def __init__(self, ANNSeed, crossOver=False):
		if(crossOver):
			self.ann = ANNSeed.Clone()
			self.fitness = 0.0
		else:
			self.ann = ANNSeed.CreateNew()
			self.fitness = 0.0

	def CreateNew(self):
		return Organism(self.ann)

	def MightMutate(self):
		self.ann.MightMutate()

	def CrossOver(self, orgm2):
		result = Organism(self.ann, crossOver=True)
		result.ann = result.ann.CrossOver(orgm2.ann)
		result.ann.MightMutate()
		return result