import random, os, shutil, sys

# number of files
filecount = int(sys.argv[1])
maxlinks = int(sys.argv[2])

# create files
currentdir = os.getcwd()
inputdir = os.path.join(currentdir, "input")
shutil.rmtree(inputdir)
os.mkdir(inputdir)
os.chdir(inputdir)
for i in range(1, filecount+1):
    FILE = open('D'+str(i)+'.txt', 'w+')
    linkcount = random.randint(1, maxlinks)
    for j in range(1, linkcount+1):
        linkint = random.randint(1, filecount)
        if i!=linkint:
            FILE.write('D'+str(linkint)+'.txt\n')
    FILE.close()
