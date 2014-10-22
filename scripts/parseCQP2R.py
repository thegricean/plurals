import csv
import re

f = open("../results/data/plurals.txt")
lines = [l.strip() for l in f.readlines()]
f.close()

headers = ["ID","Sentence","Match","Noun","Adjective"]
results = []
wresults = []

for l in lines:
	splited = l.split(":  ")
	id = splited[0]
	sentence = re.sub('[<>]','',splited[1])
	match = splited[1][splited[1].find('<')+len('<'):splited[1].rfind('>')]
	noun = match.split()[1]
	adjective = match.split()[-1]	
	results.append([id, sentence, match, noun, adjective])
	

for r in results:
	inner_dict = dict(zip(headers,r))
	wresults.append(inner_dict)
	

oname = '../results/data/results.tsv'	
w = csv.DictWriter(open(oname, 'wb'),fieldnames=headers,restval="NA",delimiter="\t")
w.writeheader()
w.writerows(wresults)
		