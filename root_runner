from ROOT import *


class SimCol:
    def __init__(self):
        self.m1 = TLorentzVector()
        self.m2 = TLorentzVector()
        self.invMass = 0
        self.particle = None

    def calcInvMass(self):
        self.particle = self.m1 + self.m2
        self.invMass = self.particle.M()

    def __str__(self):
        return 'Invariant Mass: ' + str(self.invMass) + '\n'


collision = None
histo = TH1F("histo", "Invariant Mass Distribution; Invariant Mass (GeV); Number of Occurrences", 100, 240, 962)

file = TFile("muonsBinary.root", "read")
tree = file.Get("tnt")

for entry in tree:
    collision = SimCol()
    collision.m1.SetPtEtaPhiM(entry.pt1, entry.eta1, entry.phi1, 0.1)
    collision.m2.SetPtEtaPhiM(entry.pt2, entry.eta2, entry.phi2, 0.1)
    collision.calcInvMass()
    histo.Fill(collision.invMass)

file.Close()

tf = TFile("muonsStep4.root", "recreate")
histo.Write()
tf.Close()

print("Done")
