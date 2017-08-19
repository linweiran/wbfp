import subprocess
import dpkt
import sys

mkdir1="mkdir trace"
mkdir2="mkdir trace/pcap"
mkdir3="mkdir trace/batch"
subprocess.call(mkdir1.split())
subprocess.call(mkdir2.split())
subprocess.call(mkdir3.split())


end=(int)(sys.argv[2])
start=(int)(sys.argv[1])

reader=open("background.txt",'r')


for i in range(start):
    website=reader.readline().strip()
for i in range(start,end):
        website=reader.readline().strip()
        error=open("errormessgae.txt",'w')
        error.write("{}\n".format(website))
        error.close()
        command1="node ../index.js /home/osboxes/src/out/Headless/headless_shell 9222 "+website
        name=str(i)
        command2="tcpdump -w trace/pcap/"+name+".pcap"
        tcpdump=subprocess.Popen(command2.split())
        headless=subprocess.call(command1.split())
        tcpdump.terminate()
        tcpdump.wait()
        tcpcounter=0
        incomecounter=0
        pcapfile=open("trace/pcap/"+name+".pcap",'r')
        target=open("trace/batch/"+name,'w')
        for ts, pkt in dpkt.pcap.Reader(pcapfile):
            eth=dpkt.ethernet.Ethernet(pkt)
            if eth.type!=dpkt.ethernet.ETH_TYPE_IP:
                continue
            ip=eth.data
            if ip.p==dpkt.ip.IP_PROTO_TCP: 
                tcp=ip.data
                if tcp.dport == 53 or tcp.sport == 53:
                    continue    # ignore DNS
                if len(tcp.data)>0:
                    if tcpcounter==0:
                        tm=ts
                        threshold=eth.src
                    tcpcounter+=1
                    if threshold==eth.src:
					    target.write("{} {}\n".format(ts-tm, len(tcp.data)))
                    else:
                        target.write("{} {}\n".format(ts-tm, -len(tcp.data)))
                        incomecounter+=1
        target.close()
        pcapfile.close()
        if incomecounter>0:
            i+=1
            writer=open("recovered.txt",'a')
            writer.write("{}\n".format(website))
            writer.close()


reader.close()