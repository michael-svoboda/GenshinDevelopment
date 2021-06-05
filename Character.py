class Character:

    def __init__(self, elementalType, currentEnergy, formationPositionFactor, UltimateTotal, E_skillParticleGeneration, ER_efficiency):
        self.elementalType = elementalType
        self.currentEnergy = currentEnergy
        self.formationPositionFactor = formationPositionFactor
        self.UltimateTotal = UltimateTotal
        self.E_skillParticleGeneration = E_skillParticleGeneration
        self.ER_efficiency = ER_efficiency

    #def activateULT:

    def gain_Energy(self, numberParticles, energyParticleValue, elementalTypeMultiplier, formationPositionFactor, ER_efficiency):
        self.currentEnergy = self.currentEnergy + numberParticles * energyParticleValue * elementalTypeMultiplier * formationPositionFactor * ER_efficiency

    def display_data(self, currentEnergy, formationPositionFactor, UltimateTotal):
        print("Current Energy = " + str(currentEnergy)) 
        print("Formation Position Factor = " + str(formationPositionFactor)) 
        print("Ultimate Requirement = " + str(UltimateTotal)) 
        print("Elemental Skill Particles Generated = " + str(currentEnergy)) 
        print("ER efficiency = " + str(currentEnergy)) 

kaeya = Character(1,1,1,1,1,1)

kaeya.display_data