import csv
import sys

# increase field size limit which we have to do because the fields are too big!
csv.field_size_limit(sys.maxsize)

collections = {}
keeper_coll = 'SHANTI PROJECT RECORDS'

with open('NoMoreSilence_ProjectData.csv', newline='') as rfile, open('NoMoreSilence_SampleData.csv', 'w', newline='') as wfile:
	filereader = csv.DictReader(rfile, delimiter=',', quotechar='"')
	filewriter = csv.DictWriter(wfile, filereader.fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL) 
	filewriter.writeheader()
	for row in filereader:
		coll = row['Collection Title'].upper().split(',')[0]
		coll = ' '.join(coll.split())
		# print(coll)
		if coll == keeper_coll:
			add = 'ADD IT'
			filewriter.writerow(row)
		elif coll in collections:
			collections[coll] += 1
			if collections[coll] <= 5:
				add = 'ADD IT'
				filewriter.writerow(row)
			else:
				add = 'DO NOT ADD'
		else:
			add = 'FIRST ITEM'
			collections[coll] = 1
			filewriter.writerow(row)
		# print(f"{coll} ---- {add}")
	# print(filereader.fieldnames)
