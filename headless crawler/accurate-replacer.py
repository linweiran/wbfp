import subprocess
import dpkt
import sys

i=(int)(sys.argv[1])
j=(int)(sys.argv[2])

reader=open("websites.txt",'r')
for k in range(i):
  website=reader.readline().strip()

command1="node ../index.js /home/osboxes/src/out/Headless/headless_shell 9222 "+website
name=str(i)+"-"+str(j)
command2="tcpdump -w trace/pcap/"+name+".pcap"
tcpdump=subprocess.Popen(command2.split())
headless=subprocess.call(command1.split())
tcpdump.terminate()
tcpdump.wait()
with open("trace/batch/"+name,'w') as target:
  pcap_parse("trace/pcap/"+name+".pcap",target)

reader.close()