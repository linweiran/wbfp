By Weiran Lin
Important: this headless-crawler should be implemented in the js directory of a zbrowser
requirements:subprocess,dpkt,sys
websites.txt:list of monitored websites
tracecollector:collect monitored traces with all monitored sites listed in websites.txt
	inputs:first argument is the starting index of instances, the second argument is the number of sets to be collected
	e.g.:collect 10 instances starting from index 21 (the last set should have index 30): python tracecollector.py 21 10
accurate-replacer:reproduce one of the instances of monitored sites
	inputs:first argument is the site index, the second argument is the instance index
	e.g.:replace instance 94 of site 26(trace/pcap/26-94.pcap,trace/batch/26-94) python accurate-replacer.py 26 94
alex.csv:csv file of a list of candidates for unmonitored sites
csvdealer:collect unmonitored sites based on the csv file, the last website tried will be written to errormessage.txt
	inputs:the first argument is the index of the first unmonitored site in the csv file, the second argument is the starting index of the first legal instance, the third argument is the number of successful instances to be collected
	e.g.:start collecting from websites 1888 of csv file, starting with instance index 998, collect 20 legal instances:python csvdealer.py 1888 998 20
	IMPORTANT:sites with legal traces will be APPENDED to background.txt
pcap-parse.py: produce batchfile of unmonitored instances, result will be in newnatch directory
	inputs:the first is the start index of unmonitored sites, the second argument is the ending index of unmonitored sites
	e.g. :produce batch file with index 18~388: python pcap_parse.py 18 388
errormessage.txt:contains the current(last tried) unmonitored website
background.txt:keep a list of unmonitored websites with legal instances
errortime-reproducer.py: recover unmonitored instances in background.txt
	input:the first argument is the starting index and the second argument is the end index(not included) in background.txt
	e.g.:recover instances with index 18~388: python errortime-reproducer.py 18 388
shrinker.py:eliminate illegal instances in the trace directory and shrink, result will be shown on the console
	input: the first argument is the starting index of instances to be checked, the second argument is the ending(not included) index to be checked
	e.g.: check instances with index 18~388 and shrink: python shrinker.py 18 388
	IMPORTANT:websites with legal instances will be APPENDED to background-shrinked.txt
background-shrinked.txt:list of legal instances after shrinked
batch-data_converter.py: convert batch file from K-NN format to k-FP format data file
	IMPORTANT:first copy this script into trace directory then run it
	input: the first input is the number of monitored sites, the second input is the number of instance per monitored sites, the third input is the number of unmonitored sites
	e.g.:convert 50 monitored sites with 100 instances each and 5000 unmonitored sites to data file python batch-data_convertor.py 50 100 5000