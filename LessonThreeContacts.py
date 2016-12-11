##Goal 1 loop through dictionary to print out contact information

contacts ={
    'Shannon':{'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannon'},
    'Beyonce':{'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},
    'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': 'tegsara'}
    }

for  key, value in contacts.items():
    print "{0}'s contact information is:".format (key)
    print "\tPhone: ", value.get('phone')
    print "\tTwitter: ", value.get('twitter')
    print "\tGithub: ", value.get('github')


#Goal 2 display as html table - this puts each contact info in own table

##contacts ={
##    'Shannon':{'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannon'},
##    'Beyonce':{'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},
##    'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': 'tegsara'}
##    }
##
##for key, value in contacts.items():
##    print '<table border = "1">'
##    print '<tr>'
##    print '<td colspan="2">{0}</td>'.format(key)
##    print '</tr>'
##    print '<tr>'
##    print '<td> Phone:',value.get ('phone')+ '</td>'
##    print '<td> Twitter:', value.get ('twitter') + '</td>'
##    print '<td> Github: ', value.get('github') + '</td>'
##    print '</tr>'
##    print '</table>'

## try to get all contacts in one table

contacts ={
    'Shannon':{'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannon'},
    'Beyonce':{'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},
    'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': 'tegsara'}
    }

print '<table border = "1">'
print '<tr>'


for key, value in contacts.items():
    print '<td colspan="2">{0}</td>'.format(key)
    print '<td> Phone:',value.get ('phone')+ '</td>'
    print '<td> Twitter:', value.get ('twitter') + '</td>'
    print '<td> Github: ', value.get('github') + '</td>'
    print '</tr>'
    print '<tr>'

    
print '</tr>'
print '</table>'

#Goal 3 write to a file using append. Note = when using append you can't
##keep rerunning for debugging without deleting the previous file or else
##you may get 'odd' results.

contacts ={
    'Shannon':{'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannon'},
    'Beyonce':{'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},
    'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': 'tegsara'}
    }

with open ("LessonThreeContactsFile.html","a") as new_html_file:
    new_html_file.write('<table border = "1">')
    new_html_file.write('<tr>')
    for key, value in contacts.items():
        new_html_file.write('<td colspan="2">{0}</td>'.format(key))
        new_html_file.write('<td> Phone: {0}</td>'.format(value.get ('phone')))
        new_html_file.write('<td> Twitter: {0}</td>'.format(value.get ('twitter')))
        new_html_file.write('<td> Github: {0}</td>'.format(value.get('github')))
        new_html_file.write('</tr>')
        new_html_file.write('<tr>')
    new_html_file.write('</tr>')
    new_html_file.write('</table>')

####Goal 3a - write to a file by creating html string and writing that to file


contacts ={
    'Shannon':{'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannon'},
    'Beyonce':{'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},
    'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': 'tegsara'}
    }

html_st = ""
##
with open ("LessonThreeContactsFile2.html", "w") as new_file:
    new_file.write(html_st)

html_st+='<table border = "1">'
html_st+='<tr>'

for key, value in contacts.items():
    html_st+='<td colspan="2">{0}</td>'.format(key)
    html_st+='<td> Phone: {0}</td>'.format(value.get ('phone'))
    html_st+='<td> Twitter: {0}</td>'.format(value.get ('twitter'))
    html_st+='<td> Github: {0}</td>'.format(value.get('github'))
    html_st+='</tr>'
    html_st+='<tr>'

html_st+='</tr>'
html_st+='</table>'

with open ("LessonThreeContactsFile2.html", "w") as new_file:
    new_file.write(html_st)

##Goal 4 read from contacts .csv file

with open ("contacts.csv", "r") as contact_file:
    contact_i=contact_file.read().split("\n")



for index, ct in enumerate (contact_i):
    contact_i [index] = ct.split (",")

contact_i.pop(0)

name=[]
phone=[]
twitter=[]
github=[]

for ct in contact_i:
    name.append (ct[0])
    phone.append (ct[1])
    twitter.append (ct[2])
    github.append (ct[3])

h_string = ""

h_string += '<table border = "1">'
h_string += '<tr>'

number = len (contact_i)

while number>0:
    h_string+='<td colspan="2">{0}</td>'.format(name[0])
    h_string+='<td> Phone: {0}</td>'.format(phone[0])
    h_string+='<td> Twitter: {0}</td>'.format(twitter[0])
    h_string+='<td> Github: {0}</td>'.format(github[0])
    h_string+='</tr>'
    h_string+='<tr>'
    name.pop(0)
    phone.pop(0)
    twitter.pop(0)
    github.pop(0)
    number=number-1

h_string+='</tr>'
h_string+='</table>'

with open ("LessonThreeContactsReadWrite.html", "w") as n_file:
    n_file.write(h_string)


        
                             
        
    





    
