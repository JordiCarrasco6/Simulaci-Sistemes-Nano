#Import MDAnalysis
import MDAnalysis as mda

#Load trajectory
simulacio = mda.Universe('imdnanotube.psf','autoimd.dcd')

#Loop over frames calculating water inside as a funciton of time
for ts in simulacio.trajectory:
    temps = simulacio.trajectory.time
    aiguadins = len(simulacio.select_atoms('type OT and prop abs z <6.7'))
    print(f"Frame: {ts.frame:3d},Time {temps:4.0f} ps, Water Inside: {aiguadins:4.0f}")
