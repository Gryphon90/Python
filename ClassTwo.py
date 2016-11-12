###Lists in square brackets, separated by commas
##
##attendees = ['Shannon', 'Jenn', 'Grace']
##
##print attendees [1]
##
###empty list
##people_who_did_pbj = []
##
###how many in list
##
###print len(attendees)
##
##number_attendees = len(attendees)
##
##print number_attendees
##
###append to list - append add 1, extend add multiple
##
##attendees.append('Tyler')
##attendees.extend(['Linda', 'Tess'])
##
##print attendees
##
###create blank list and append
##
##attendees_ages = []
##
##attendees_ages.append (28)
##attendees_ages.append (27)
##
##print attendees_ages
##
###changing values in list
##
##attendees_ages [0] = 29
##
##print attendees_ages
##
###exercise - days of week
##
##days_of_week = ['Monday']
##
##print days_of_week
##
##days_of_week.append('Tuesday')
##
##print days_of_week
##
##days_of_week.extend (['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
##
##print days_of_week
##
##print len (days_of_week)
##
###pop method - removes last item added
##
##day = days_of_week.pop()
##
##print day
##print days_of_week
##
##
##day = days_of_week.pop(3)
##print day
##print days_of_week
##
###EXERCISE - months
##
##months = ['January', 'Feburary']
##
##print months
##
##months.append('March')
##
##print months
##
##months.extend(['April', 'May', 'June', 'July'])
##months.extend(['Auguste', 'September', 'October'])
##months.extend (['November', 'December'])
##
##print months
##
##print len(months)
##
###Remove
##months.pop(0)
##
##print months
##print len (months)
##
###Insert
##
##months.insert(0,'January')
##
##print months
##print len(months)
##
###Strings to list
##
##address = "1133 19th St NW Washington, DC"
##
###splitting based an a character, space for example
##
##address_as_list = address.split (' ')
##
##print address_as_list
##
###In is something there - in list must match exact
##
##print '19th' in address_as_list
##
##print '19' in address_as_list

##name=raw_input('name?')
##
##print name

NW=[]
NE=[]
SW=[]
SE=[]
add=[]

address1=raw_input('enter address')
address2=raw_input('enter address')
address3=raw_input('enter address')
print address1
print address2
print address3

if 'NW'.lower()in address1:
    NW.append(address1)
elif 'NE'.lower() in address1:
    NE.append(address1)
elif 'SW'.lower() in address1:
    SW.append(address1)
elif 'SE'.lower() in address1:
    SE.append(address1)
else:
    add.append(add)


if 'NW'.lower() in address2:
    NW.append(address2)
elif 'NE'.lower() in address2:
    NE.append(address2)
elif 'SW'.lower() in address2:
    SW.append(address2)
elif 'SE'.lower() in address2:
    SE.append(address2)
else:
    add.append(address2)

if 'NW'.lower() in address3:
    NW.append(address3)
elif 'NE'.lower() in address3:
    NE.append(address3)
elif 'SW'.lower() in address3:
    SW.append(address3)
elif 'SE'.lower() in address3:
    SE.append(address3)
else:
    add.append(address3)



print NW
print NE
print SW
print SE







