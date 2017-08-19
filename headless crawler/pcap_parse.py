import dpkt
import sys
import subprocess

def pcap_parse(pcap_name, out_file):
    tcpcounter = 0
    with open(pcap_name, "rb") as pcap_file:
        for ts, pkt in dpkt.pcap.Reader(pcap_file):
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
                        out_file.write("{} {}\n".format(ts-tm, len(tcp.data)))
                    else:
                        out_file.write("{} {}\n".format(ts-tm, -len(tcp.data)))

if __name__ == "__main__":
    mkdir1="mkdir trace/batch"
    subprocess.call(mkdir1.split())    
    start=int(sys.argv[1])
    end=int(sys.argv[2])
    for i in range(start,end):
      string=str(i-start+1)+"/"+str(end-start)
      sys.stdout.write('%s\r' % string)
      sys.stdout.flush()
      with open("trace/batch/"+str(i),'w') as writer:
      	pcap_parse("trace/pcap/"+str(i)+".pcap",writer)
      