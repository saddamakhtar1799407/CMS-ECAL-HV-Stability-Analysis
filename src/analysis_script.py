import ROOT
from ROOT import TGraph, TCanvas, TH1F, TH1D, TH2F, TProfile, TFile
from array import array
from ROOT import TDatime
import time
import statistics

# Creating ROOT File
file = TFile.Open("Prototype.root", 'RECREATE')

# Creating TTree In ROOT file
tree = ROOT.TTree("Channel1", "Channel1")

# Creating Branches in TTree
B1 = array('f', [0.])
Voltage = tree.Branch('Voltage', B1, 'Voltage/F')

B2 = array('f', [0.])
Temp = tree.Branch('Temp', B2, 'Temp/F')

B3 = array('f', [0.])
VMon = tree.Branch('Vmon', B3, 'Vmon/F')

B4 = array('f', [0.])
IMon = tree.Branch('Imon', B4, 'Imon/F')

B5 = array('i', [0])
Time = tree.Branch('Time', B5, 'Time/I')

# Reading Data
data = open('prototype.txt')
lines = data.readlines()
for line in lines:
    if 'VmeT' in line:
        VmeT = line.split("VmeT: ")[1]
        V = VmeT.split(' ')[1]
        if float(V) < 379.00:
            continue
        B1[0] = float(V)
        T = VmeT.split(' ')[2]
        B2[0] = float(T)

    if 'VMon' in line:
    	VMon = line.split("VMon: ")[1]
    	B3[0] = float(VMon.split()[0])
    if 'IMon' in line:
    	IMon = line.split("IMon: ")[1]
    	B4[0] = float(IMon.split()[0])
    else:
        dt = line.split(' ')[0]
        if '\n' in dt:
            continue#for one day
        if '25/Apr/2021/23:43:54' in dt:
            break
        parsed_time = time.strptime(dt, '%d/%b/%Y/%H:%M:%S')
        date_time = TDatime(int(time.mktime(parsed_time)))
        B5[0] = date_time.Convert()
        print(dt)
        tree.Fill()



file.Write()
file.Close()

# TGraph- GET TREE-GET Branches
f = TFile.Open("Prototype.root", "read")
tree = f.Get("Channel1")

voltage_branch = tree.GetBranch("Voltage")
time_branch = tree.GetBranch("Time")

voltage_array = []
time_array = []

for i in range(tree.GetEntries()):
	tree.GetEntry(i)
	voltage = voltage_branch.GetLeaf("Voltage").GetValue()
	time = time_branch.GetLeaf("Time").GetValue()
	voltage_array.append(voltage)
	time_array.append(time)

graph = TGraph(len(voltage_array), array('d', time_array), array('d', voltage_array))
graph.SetTitle("Prototype_voltage_vs_time")
graph.SetMarkerStyle(ROOT.kOpenDiamond)

# Min and Max Values
voltage_min = min(voltage_array)
voltage_max = max(voltage_array)
voltage_mean = statistics.mean(voltage_array)
voltage_diff = voltage_max - voltage_min
print("The voltage difference is:", voltage_diff)
print("Mean Voltage:",voltage_mean)
print("Minimum voltage:", voltage_min)
print("Maximum voltage:", voltage_max)

# X and Y axis labels
x_axis = graph.GetXaxis()
x_axis.SetTitle('Time')
x_axis.SetTitleOffset(1.1)
x_axis.SetTitleSize(0.03)
x_axis.SetLabelSize(0.03)

y_axis = graph.GetYaxis()
y_axis.SetTitle('Voltage (V)')
y_axis.SetTitleOffset(1.5)
y_axis.SetTitleSize(0.03)
y_axis.SetLabelSize(0.03)

#Time conversion Unix to human read
graph.GetXaxis().SetNdivisions(-504)
graph.GetXaxis().SetTimeDisplay(1)
graph.GetXaxis().SetTimeFormat("%d/%m")
#graph.GetXaxis().SetTimeFormat("%H:%M")#For day

#Canvas
c1 = ROOT.TCanvas("canvas", "Prototype", 1200, 600)
graph.Draw("AP")
c1.SaveAs("Prototype_voltage_vs_time.png")
c1.SaveAs("Prototype_voltage_vs_time.root")

c1.Update()
ROOT.gPad.WaitPrimitive()
file.Close()

############### Histogram ###############
import ROOT

# Open the input file
file1 = ROOT.TFile("Prototype.root", "READ")

# Get the TTree object from the file
tree = file1.Get("Channel1")

# Get the branch object from the tree
branch = tree.GetBranch("Voltage")
# Create a TH1F histogram
hist = ROOT.TH1F("Prototype", "Voltage Distribution",5,voltage_min,voltage_max )

# Loop over the entries in the TTree and fill the histogram with the values from the branch
for entry in range(tree.GetEntries()):
	tree.GetEntry(entry)
	value = branch.GetLeaf("Voltage").GetValue()
	hist.Fill(value)

# Get the min and max values of the voltage
voltage_min = hist.GetXaxis().GetXmin()
voltage_max = hist.GetXaxis().GetXmax()

# Calculate the RMS value of the voltage
voltage_rms = hist.GetRMS()
print("Standard deviation:", voltage_rms)
# Create a TCanvas and draw the histogram on it
canvas = ROOT.TCanvas("canvas", "Prototype", 1200, 600)
hist.Draw()
# X and Y axis labels

x_axis = hist.GetXaxis()
x_axis.SetTitle('Voltage (V)')
x_axis.SetTitleOffset(1.1)
x_axis.SetTitleSize(0.03)
x_axis.SetLabelSize(0.03)

y_axis = hist.GetYaxis()
y_axis.SetTitle('Counts')
y_axis.SetTitleOffset(1.5)
y_axis.SetTitleSize(0.03)
y_axis.SetLabelSize(0.03)

# set background color
hist.SetFillColor(ROOT.kGray+1)

# set line color
hist.SetLineColor(ROOT.kBlue)


# Set title
hist.SetTitle("Voltage Distribution")

# Show the canvas
canvas.SaveAs("Prototype_voltage_distribution.png")
canvas.SaveAs("Prototype_voltage_distribution.root")

canvas.Modified()
canvas.Update()
canvas.WaitPrimitive()

# Close the input file
file1.Close()




