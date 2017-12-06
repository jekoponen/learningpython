import datetime
import glob2

files = glob2.glob("data/file*.txt")
filename = datetime.datetime.now()
mergedFile = open(filename.strftime("data/" + "%F-%H-%M-%S-%f") +".txt","w")

for i in files:
    with open(i,"r") as file:
        content = file.read()
        if i == len(files) -1:
            mergedFile.write(content)
        else:
            mergedFile.write(content + "\n")

mergedFile.close()
