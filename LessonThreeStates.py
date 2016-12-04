
##Goal one - open states.txt and generate html drop down

with open ("states.txt", "r") as statestxt_file:
    states = statestxt_file.read().split("\n")


for index, state in enumerate (states):
        states [index] = state.split("\t")


state_abbr = []
state_name = []

for state in states:
    state_abbr.append (state[0])
    state_name.append (state[1])


print '<select name = "state">'
print '<option value ="">Select State </option>'

for ab, st in zip (state_abbr, state_name):
    print '<option value="{0}">{1}</option>'.format(ab,st)

print '</select>'

###Goal Two - save to html file instead of printing to screen

with open ("states.txt", "r") as statestxt2_file:
    states2 = statestxt2_file.read().split("\n")
print states2

for index, state2 in enumerate (states2):
        states2[index]= state2.split("\t")


state_abbr2 = []
state_name2 = []

for state2 in states2:
    state_abbr2.append (state2[0])
    state_name2.append (state2[1])

print state_abbr2
print state_name2


html_text=""

html_text+='<select name = "state">'
html_text+='<option value ="">Select State </option>'

for a, s in zip(state_abbr2, state_name2):
    html_text+='<option value="{0}">{1}</option>'.format(a,s)

html_text+='</select>'

with open ("LessonThreeStates.html","w") as new_file:
    new_file.write(html_text)


##Goal three - create html page with state info

##print to idle - manually create file

with open ("state_info.csv", "r") as state_infocsv_file:
    state_i=state_infocsv_file.read().split("\n")

for index, st in enumerate (state_i):
    state_i [index] = st.split (",")

state_i.pop (0)


rank=[]
state=[]
popul=[]
house_mem=[]
per_popul=[]

for st in state_i:
    rank.append (st[0])
    state.append (st[1])
    popul.append (st[2])
    house_mem.append (st[3])
    per_popul.append (st[4])

num = len (state_i)

while num > 0:
    print '<table border ="1">'
    print '<tr>'
    print '<td colspan="2"> {0} </td>'.format (state[0])
    print '</tr>'
    print '<tr>'
    print '<td> Rank: {0}</td>'.format(rank[0])
    print '<td> Percent: {0}</td>'.format(per_popul[0])
    print '</tr>'
    print '<tr>'
    print '<td> US House Members: {0}</td>'.format(house_mem[0])
    print '<td> Population: {0}</td>'.format(popul[0])
    print '</tr>'
    print '</table>'
    rank.pop (0)
    state.pop (0)
    popul.pop (0)
    house_mem.pop (0)
    per_popul.pop (0)
    num = num-1

##Do same thing but automatically write to file

with open ("state_info.csv", "r") as state_infocsv_file:
    state_i=state_infocsv_file.read().split("\n")

for index, st in enumerate (state_i):
    state_i [index] = st.split (",")

state_i.pop (0)


rank=[]
state=[]
popul=[]
house_mem=[]
per_popul=[]

for st in state_i:
    rank.append (st[0])
    state.append (st[1])
    popul.append (st[2])
    house_mem.append (st[3])
    per_popul.append (st[4])

html_info = ""

num = len (state_i)

while num > 0:
    html_info+='<table border =\"1\">'
    html_info+='<tr>'
    html_info+='<td colspan=\"2\"> {0} </td>'.format (state[0])
    html_info+='</tr>'
    html_info+='<tr>'
    html_info+='<td> Rank: {0}</td>'.format(rank[0])
    html_info+='<td> Percent: {0}</td>'.format(per_popul[0])
    html_info+='</tr>'
    html_info+='<tr>'
    html_info+='<td> US House Members: {0}</td>'.format(house_mem[0])
    html_info+='<td> Population: {0}</td>'.format(popul[0])
    html_info+='</tr>'
    html_info+='</table>'
    rank.pop (0)
    state.pop (0)
    popul.pop (0)
    house_mem.pop (0)
    per_popul.pop (0)
    num = num-1

with open ("LessonThreeStateInfo.html","w") as new_html_file:
    new_html_file.write(html_info)
    
    





    
    





                
                                  
