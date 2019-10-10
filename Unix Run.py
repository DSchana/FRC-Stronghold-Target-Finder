import os

# Make files
os.system("cmake Unix/.")
os.system("make -C Unix/.")
os.system("Unix/StrongholdTracking")
