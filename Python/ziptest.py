import os


rootdir = r'C:\geodata'


for rootdir, dirs, files in os.walk(rootdir):
    for subdir in dirs:
        #print(os.path.join(rootdir, subdir))
        for file in files:

            print(os.path.join(rootdir, subdir, file))
