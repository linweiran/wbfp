import json
import subprocess
import sys

def json_parse(node):
  if len(node)>3:
	data=node["data"]
	networkData=node["networkData"]
	request=networkData["request"]
	initiator=request["initiator"]
	if initiator["type"] == "parser":
		url=initiator["url"]
		lineNumber=str(initiator["lineNumber"])
		output='"'+url+'"'+" -> "+'"'+data+'"'+" [label="+'"'+lineNumber+'"'+"];"	
		writer.write("{}\n".format(output))
	if initiator["type"] == "script":
		stack=initiator["stack"]
		callFrames=stack["callFrames"]
		for callFrame in callFrames:
			url=callFrame["url"]
#			print callFrame
			label=str(callFrame["lineNumber"])+":"+str(callFrame["columnNumber"])
			output='"'+url+'"'+" -> "+'"'+data+'"'+" [label="+'"'+label+'"'+"];"	
			writer.write("{}\n".format(output))
	children=node["children"]
	for subnode in children:
		json_parse(subnode)
	


filename=sys.argv[1]
writer=open("output.dot",'w')
writer.write("digraph G {\n")
with open(filename,'r') as reader:

	jsdata=json.load(reader)
 	for root in jsdata:
		json_parse(jsdata[root])
writer.write("}\n")
writer.close()
command="dot -Tpdf output.dot -o output.pdf"
subprocess.call(command.split())
