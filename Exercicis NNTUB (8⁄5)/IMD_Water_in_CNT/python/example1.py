#Import MDAnalysis
import MDAnalysis as mda

#Load trajectory
simulacio = mda.Universe('imdnanotube.psf','autoimd.dcd')

#Loop shwing frames and time
for ts in simulacio.trajectory:
    temps = simulacio.trajectory.time
    print(f"Frame: {ts.frame:3d},Time {temps:4.0f} ps")
