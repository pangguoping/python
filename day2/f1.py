
f = file("f_test.txt",'w')
for i in range(10):
	f.write('the %s loops\n' % i)

f.close()
