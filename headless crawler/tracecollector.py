import subprocess
import dpkt
import sys

mkdir1="mkdir trace"
mkdir2="mkdir trace/pcap"
mkdir3="mkdir trace/batch"
subprocess.call(mkdir1.split())
subprocess.call(mkdir2.split())
subprocess.call(mkdir3.split())

instancenum=(int)(sys.argv[2])

restart=(int)(sys.argv[1])

for j in range(restart,restart+instancenum,1):
    reader=open("websites.txt",'r')
    i=0
    website=reader.readline().strip()
    while website!="":
	command1="node ../index.js /home/osboxes/src/out/Headless/headless_shell 9222 "+website
        name=str(i)+"-"+str(j)
        command2="tcpdump -w trace/pcap/"+name+".pcap"
        tcpdump=subprocess.Popen(command2.split())
        headless=subprocess.call(command1.split())
        tcpdump.terminate()
        tcpdump.wait()
        with open("trace/batch/"+name, 'w') as target:
            pcap_parse("trace/pcap/"+name+".pcap", target)
        i+=1
        website=reader.readline().strip()

    reader.close()
