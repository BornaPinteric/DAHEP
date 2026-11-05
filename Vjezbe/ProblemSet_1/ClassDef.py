import numpy as np
class Boson:
    isFermion=False
    def __init__(self, name, spin, momentum):
        self.name=name
        self.spin=spin
        self.mom=momentum
    def PrintInfo(self):
        print("---INFO ({})---\nSpin: {}\nMomentum: {}MeV\nIs{} a fermion.\n".format(self.name,self.spin,self.mom,"" if self.isFermion else " NOT"))
class Higgs(Boson):
    s_mass=1
    def __init__(self, name, spin, momentum, meanmass):
        Boson.__init__(self, name, spin, momentum)
        self.m_mass=meanmass
        self.__generatemass__()
    def __generatemass__(self):
        self.mass=np.random.normal(self.m_mass, self.s_mass)
        print("From a normal distribution around mean mass {}Mev generated mass of Higgs ({}) of {}Mev.\n".format(self.m_mass,self.name,round(self.mass,2)))
    def Energy(self):
        self.energy=np.sqrt(self.mass**2+self.mom**2)
        print("Energy of Higgs ({}) is E = sqrt({}^2 + {}^2)MeV = {}Mev\n".format(self.name,self.mom,round(self.mass,2),round(self.energy,2)))