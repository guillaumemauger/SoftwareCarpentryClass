
m2str = "mammal_abundance_UW_Feb.txt"
m4str = "mammal_abundance_UW_Apr.txt"

nmax = -9999
namemax = []

#import pdb
#pdb.set_trace()

import csv

print " "
print "reading file: " + m2str
fp = file(m2str, "rb")
rdr2 = csv.reader(fp)
for dt,name,num in rdr2:
	print dt,name,num,nmax
        if int(num) > int(nmax):
                print "num (" + num + ") > nmax (" + nmax ")"
		nmax = num
                namemax = []
                namemax.append(name)
        elif int(num) == int(nmax):
                namemax.append(name)
		print "elif new nmax " + nmax
fp.close()

print " "
print "reading file: " + m4str
fp = file(m4str, "rb")
rdr4 = csv.reader(fp)
for dt,name,num in rdr4:
	print dt,name,num,nmax
	if int(num) > int(nmax):
		print num,nmax
		nmax = num
		namemax = []
		namemax.append(name)
	elif int(num) == int(nmax):
		namemax.append(name)
		print "elif new nmax " + nmax
fp.close()

print "-----"
print "nmax = " + nmax
print "length namemax = "
print len(namemax)
for crap in namemax:
	print "name = " + crap
