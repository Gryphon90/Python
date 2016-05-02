##Set variables

bread=0
PB=5
Jelly=5
SandBread = bread/2
SandBread2 = bread/2.0
SandBread3 = bread % 2 == 1

##print bread
##print PB
##print Jelly
##print SandBread
##print SandBread2
##print SandBread3


## First goal - Can you make a PBJ sandwich

print "First goal"


if PB >= 1 and Jelly >= 1 and SandBread >=1:
    print "A sandwich can be made"
else:
    print "No sandwich today"


## Second goal - how many sandwiches can be

print "------------------------"

print "Second goal"


if PB >= 1 and Jelly >= 1 and bread >=1:
    HowMany = SandBread
    if PB < HowMany and PB <= Jelly:
        HowMany = PB
    if Jelly < HowMany and Jelly <= PB:
        HowMany = Jelly
    print "You can make {0} sandwiches.".format(HowMany)
else:
    print "You can not make any sandwiches, You have {0} bread, {1} peanut butter, and {2} jelly".format(bread, PB, Jelly)

print "------------------------"

## Third goal - Can you make an open face sandwich


print "Third goal"


if PB >= 1 and Jelly >= 1 and bread >=1:
    HowMany = SandBread
    if PB < HowMany and PB <= Jelly:
        HowMany = PB
    if Jelly < HowMany and Jelly <= PB:
        HowMany = Jelly
    print "You can make {0} sandwiches.".format(HowMany)
    if bread % 2 == 1 and PB > SandBread:
        print "You can also make an open faced sandwich"
else:
    print "You can not make any sandwiches, You have {0} bread, {1} peanut butter, and {2} jelly".format(bread, PB, Jelly)

print "------------------------"

##Fourth goal






print "------------------------"

## Fifth goal

print "Fifth goal"

if PB >= 1 and Jelly >= 1 and bread >=1:
    HowMany = SandBread
    if PB < HowMany and PB <= Jelly:
        HowMany = PB
    if Jelly < HowMany and Jelly <= PB:
        HowMany = Jelly
    print "You can make {0} sandwiches.".format(HowMany)
    if bread % 2 == 1 and PB > SandBread:
        print "You can also make an open faced sandwich"
elif PB<1 and Jelly >=1 and bread >=1:
        HowMany = Jelly
        print "You can make {0} Jelly sandwiches but you have no Peanut Butter.".format (HowMany)
elif PB>=1 and Jelly <1 and bread >=1:
        HowMany = PB
        if PB<SandBread:
            print "You can make {0} Peanut Butter sandwiches but you have no Jelly.".format (HowMany)
        if bread % 2 == 1 and PB > SandBread:
            print "You can make {0} Peanut Butter sandwiches and 1 open faced, but there will be no Jelly".format(SandBread)
elif PB>=1 and Jelly >=1 and bread <1:
        HowMany = bread
        print "You have {0} slices of bread, you can't make any sandwiches, but you could eat spoonfuls of peanut butter and jelly.".format (HowMany)
elif PB<1 and Jelly <1 and bread >=1:
        print "You can't make any sandwiches, no peanut butter and jelly. Bread and water today."
        

##else:
##    print "You can make jelly sandwiches, but no peanut butter (if you really want to do that). You have {0} bread, {1} peanut butter, and {2} jelly".format(bread, PB, Jelly)


