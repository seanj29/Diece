import os

def rename(dir, newname):
    for directory in os.listdir(dir):
        count = 1
        for file in os.listdir(dir + "\\" + directory):
            src = dir + "\\" + directory + "\\" + file
            drc = dir + "\\" + directory + "\\" + newname + " " + directory + " " + str(count) + ".png"
            os.rename(src, drc)
            count += 1

rename("The Guy", "The Guy")

