import numpy as np
from ClassDef import Boson,Higgs
a=Boson("Boz",1,34)
a.PrintInfo()
b=Higgs("h",0,100,125)
b.PrintInfo()
b.Energy()