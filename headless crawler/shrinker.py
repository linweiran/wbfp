import subprocess
import sys

start=(int)(sys.argv[1])
end=(int)(sys.argv[2])
filecounter=start
readername="background.txt"
writername="background-shrinked.txt"
reader=open(readername,'r')
writer=open(writername,'a')
for i in range(start):
  background=reader.readline().strip()
for i in range(start,end,1):
  background=reader.readline().strip()
  checkfilename="trace/batch/"+str(i)
  checkfile=open(checkfilename,'r')
  linecounter=0
  receivecounter=0
  for line in checkfile:
    linecounter+=1
    line=line.split(" ")
    if int(line[1])<0:
      receivecounter+=1
  checkfile.close()
  if linecounter>2 and receivecounter>0:
    if i!=filecounter:
      movecommand1="mv trace/pcap/"+str(i)+".pcap trace/pcap/"+str(filecounter)+".pcap"
      movecommand2="mv trace/batch/"+str(i)+" trace/batch/"+str(filecounter)

      subprocess.call(movecommand1.split())
      subprocess.call(movecommand2.split())

    
    filecounter+=1
    writer.write("{}\n".format(background))
  string="dealing with file "+str(i)+" ("+str(start)+"-"+str(end)+")"
  sys.stdout.write('%s\r' % string)
  sys.stdout.flush()
print "shrink from ",end-start,"files, shrink to ",filecounter-start,"files, delete ",end-filecounter," files"
reader.close()
writer.close()
