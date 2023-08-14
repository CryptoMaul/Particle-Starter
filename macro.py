from ROOT import *

def analyze_delphes_output(input_file):
    file = ROOT.TFile.Open(input_file)
    input_tree = file.Get("Delphes")

    # Create variables to store muon information
    pt = ROOT.std.vector('float')()
    eta = ROOT.std.vector('float')()
    phi = ROOT.std.vector('float')()

    # Connect branches
    input_tree.SetBranchAddress("Particle.PT", pt)
    input_tree.SetBranchAddress("Particle.Eta", eta)
    input_tree.SetBranchAddress("Particle.Phi", phi)

    # Create a new output file
    output_file = ROOT.TFile("output_muon_properties.root", "RECREATE")
    output_tree = ROOT.TTree("MuonTree", "Muon Kinematics")

    # Create branches in the output tree
    pt_branch = output_tree.Branch("MuonPT", pt)
    eta_branch = output_tree.Branch("MuonEta", eta)
    phi_branch = output_tree.Branch("MuonPhi", phi)

    # Loop through events
    for entry in input_tree:
        

    #goofy shit GPT made
    for iEvent in range(input_tree.GetEntries()):
        input_tree.GetEntry(iEvent)

        # Clear vectors before filling new event data
        pt.clear()
        eta.clear()
        phi.clear()

        # Loop through particles and select muons
        for i in range(len(pt)):
            if abs(pt[i]) > 0.1 and abs(eta[i]) < 2.5:  # Example muon selection criteria
                pt.push_back(pt[i])
                eta.push_back(eta[i])
                phi.push_back(phi[i])

        # Fill the output tree with selected muon data
        output_tree.Fill()

    # Write and close the output file
    output_tree.Write()
    output_file.Close()

if __name__ == "__main__":
    input_file = "path_to_your_delphes_output.root"
    analyze_delphes_output(input_file)
