contact_dic = {}
with open('contact_list2.txt') as f:
	for i in f.readlines():
	  line = i.strip().split()
	  contact_dic[line[0]] = line[1:]
#print contact_dic.keys()

while True:
	search = raw_input("Search info:").strip()
	if len(search) == 0:continue # not empty input
	if contact_dic.has_key(search):
		print search,contact_dic[search]
	else:   # start to search the info in fuzzy matching mode
		info_counter = 0
		if len(search) < 3:
			print "No valid info ....."
			continue
		for name,value in contact_dic.items():
			if name.count(search) != 0: # search exist
				s_index = name.find(search)
				print name[:s_index] + "\033[32;1m%s\033[0m" %search + name[s_index + len(search):] , '\t'.join(value)
#				print name,'\t'.join(value)
				info_counter += 1
				continue
			for i in value: # second layer loop
				if i.count(search) != 0:
					print name,'\t'.join(value)
					info_counter += 1
		if info_counter == 0:
			print "No valid record...."
		else:
			print "Found %s records...." % info_counter
