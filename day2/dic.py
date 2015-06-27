
contacts = {
	'Alex' : 18911201230,
	'Rachel' : [18101261061,'student',25],
	'Rain' : {'age':28 },
}

contacts['Alex'] = 11102337
del contacts['Alex']
for k,v in contacts.items():
	print k,v
