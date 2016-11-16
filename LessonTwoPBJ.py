##Simple, make sure bread is less than other ingredients. Just check on bread.

bread = 4
PB = 4
jelly = 4
sandw = bread/2
number =1



while bread >= 2:
    print "I'm making sandwich #{0}".format(number)
    bread=bread-2
    number=number+1

print "All done, can't make any more sandwiches, out of bread."

##Vary amounts of all ingredients

##INSTRUCTIONS
# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.



bread2=3
PB2=4
jelly2=3
sandw2=bread2/2
number2=1

while bread2 >=2 and PB2>=1 and jelly2>=1:
    print "I'm making sandwich #{0}".format(number2)
    print """I have enough bread for {0} more sandwiches, enought peanut butter for {1} more
sandwiches, enough jelly for {2} more sandwiches""".format(sandw2-1, PB2-1,jelly2-1)
    bread2=bread2-2
    PB2=PB2-1
    jelly2=jelly2-1
    number2=number2+1
    sandw2=bread2/2


if sandw2 == 0:
    print "No more PBJs, out of bread."
elif PB2==0:
    print "No more PBJs, out of peanut butter."
elif jelly2==0:
    print "No more PBJs, out of jelly."
    
    
    
