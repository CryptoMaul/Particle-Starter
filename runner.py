import re
import math
from scipy.constants import c


class Muon:
    def __init__(self):
        self.pt = 0
        self.p = 0
        self.eta = 0
        self.phi = 0
        self.m = 0
        self.fV = []  # simply uses E in four vector to make other functions easier
        self.ofV = []  # Uses E/c in four vector

    def setData(self, mLine):
        pattern = re.findall("^m[12]:", mLine)
        if pattern:
            # m1: pt,eta,phi,m= 228.457 -0.705201 2.45147 0.1 dptinv: 0.00037528
            # objective: split line via spaces, get data from known indices and assign to muon object
            # trim off the unnecessary words to get the raw numbers
            mLine = mLine.split(':')[1].split('=')[1].strip().split()[0:3]
            self.pt = float(mLine[0])
            self.eta = float(mLine[1])
            self.phi = float(mLine[2])
            self.m = 0.1

    def calcFourVector(self):
        px = self.pt * math.cos(self.phi)
        py = self.pt * math.sin(self.phi)
        pz = self.pt * math.sin(self.eta)

        self.p = (px ** 2 + py ** 2 + pz ** 2) ** 0.5
        energy = (0.1 ** 2 + self.p ** 2) ** 0.5
        self.fV = [energy, px, py, pz]
        self.ofV = [energy / c, px, py, pz]


class SimCol:
    def __init__(self):
        self.run = 0
        self.event = 0
        self.m1 = Muon()
        self.m2 = Muon()
        self.invMass = 0

    def setID(self, ln):
        pattern = re.findall("^Run", ln)
        if pattern:
            # Run 141544 event 5
            ln = ln.split()
            self.run = ln[1]
            self.event = ln[3]

    def setMuon1(self, mLine):
        self.m1.setData(mLine)

    def setMuon2(self, mLine):
        self.m2.setData(mLine)

    def calcInvMass(self):
        self.m1.calcFourVector()
        self.m2.calcFourVector()
        self.invMass = ((self.m1.fV[0] + self.m2.fV[0]) ** 2 - math.fabs(self.m1.p + self.m2.p) ** 2) ** 0.5

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
            collision.m1.setData(line)
        if line.startswith("m2:"):
            collision.m2.setData(line)
        line = f.readline()
f.close()

f = open('muonResults.txt', 'w')

for col in allCollisions:
    col.calcInvMass()
    f.write(str(col))
f.close()
