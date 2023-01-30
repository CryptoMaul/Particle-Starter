import re
import math
from ROOT import *


class SimCol:
    def __init__(self):
        self.run = 0
        self.event = 0
        self.m1 = TLorentzVector()
        self.m2 = TLorentzVector()
        self.invMass = 0
        self.particle = None

    def setID(self, ln):
        pattern = re.findall("^Run", ln)
        if pattern:
            # Run 141544 event 5
            ln = ln.split()
            self.run = ln[1]
            self.event = ln[3]

    def setMuon1(self, mLine):
        # m1: pt,eta,phi,m= 228.457 -0.705201 2.45147 0.1 dptinv: 0.00037528
        # objective: split line via spaces, get data from known indices and assign to muon object
        # trim off the unnecessary words to get the raw numbers
        mLine = mLine.split(':')[1].split('=')[1].strip().split()[0:3]
        self.m1.SetPtEtaPhiM(float(mLine[0]), float(mLine[1]), float(mLine[2]), 0.1)

    def setMuon2(self, mLine):
        # m2: pt,eta,phi,m= 228.457 -0.705201 2.45147 0.1 dptinv: 0.00037528
        # objective: split line via spaces, get data from known indices and assign to muon object
        # trim off the unnecessary words to get the raw numbers
        mLine = mLine.split(':')[1].split('=')[1].strip().split()[0:3]
        self.m2.SetPtEtaPhiM(float(mLine[0]), float(mLine[1]), float(mLine[2]), 0.1)

    def calcInvMass(self):
        self.particle = self.m1 + self.m2
        self.invMass = self.particle.M()

    def __str__(self):
        return 'Run ' + str(self.run) + ', Event ' + str(self.event) + ', Invariant Mass: ' + str(self.invMass) + '\n'


allCollisions = []
collision = None

with open('muons.txt') as f:
    line = f.readline()
    while line:
        if line.startswith("Run"):
            collision = SimCol()
            allCollisions.append(collision)
            collision.setID(line)
        if line.startswith("m1:"):
            collision.setMuon1(line)
        if line.startswith("m2:"):
            collision.setMuon2(line)
        line = f.readline()
f.close()

f = open('muonResultsROOT.txt', 'w')

for col in allCollisions:
    col.calcInvMass()
    f.write(str(col))
f.close()

print("Done")