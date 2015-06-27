
contacts = {
	'Alex' : 18911201230,
	'Rachel' : [18101261061,'student',25],
	'Rain' : {'age':28 },
}
if contacts.has_key('Rain'):print '========='

for i in contacts:
	print i,i.count('R')
contacts['Alex'] = 11102337
del contacts['Alex']
for k in contacts.keys():
	print k
