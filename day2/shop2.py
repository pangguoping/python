#!/usr/bin/env python
products = ['Car','Iphone','Bike','Coffee','PythonCourse']
prices = [ 500000,4800,800,33,5800 ]

salary = int(raw_input("Your current salary:"))

shopping_list = []
while True:
  print "On sale products:"
  for p in products:
	print p,prices[products.index(p)]
  option = raw_input("what do you want to buy?:").strip()
  if len(option) == 0:continue
  if option in products:
        p_price = prices[ products.index(option) ]
	if salary > p_price :
		print 'Adding %s into shopping list.' % option
		shopping_list.append(option)
		#salary = salary - p_price
		salary -= p_price
		print "Your current balance:%s" % salary
                continue
	else:
		print "Sorry,you cannot afford to buy %s "% option
		if salary < min(prices):
			print "Too poor to buy anything from us,fuck off!"
			break
