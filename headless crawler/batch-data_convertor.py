import subprocess
import sys

mkdir1="mkdir data"
mkdir2="mkdir data/Alexa_Monitored"
mkdir3="mkdir data/Unmonitored"
subprocess.call(mkdir1.split())
subprocess.call(mkdir2.split())
subprocess.call(mkdir3.split())

monitoredsitesnum=(int)(sys.argv[1])
monitoredinstancesnum=(int)(sys.argv[2])
unmonitoredsitesnum=(int)(sys.argv[3])

readerpath="batch/"
writerunmonitoredpath="data/Unmonitored/"
writermonitoredpath="data/Alexa_Monitored/"

for i in range(monitoredsitesnum):
  for j in range(monitoredinstancesnum):
    readername=readerpath+str(i)+"-"+str(j)
    writername=writermonitoredpath+str(i)+"_"+str(j)
    reader=open(readername,'r')
    writer=open(writername,'w')
    for x in reader:
      x=x.split(" ")
      time=float(x[0])
      size=int(x[1])
      if size>0:
        direction=1.0
      else:
        direction=-1.0
      writer.write("{} {}\n".format(time,direction))
    writer.close()
    reader.close()
for i in range(unmonitoredsitesnum):
  readername=readerpath+str(i)
  writername=writerunmonitoredpath+str(i)
  reader=open(readername,'r')
  writer=open(writername,'w')
  for x in reader:
    x=x.split(" ")
    time=float(x[0])
    size=int(x[1])
    if size>0:
      direction=1.0
    else:
      direction=-1.0
    writer.write("{} {}\n".format(time,direction))
  writer.close()
  reader.close()
  