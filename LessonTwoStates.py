##Need list of states

states = ['Alabama', 'Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']



print '<select name = "state">'
print '<option value="">Select State</option>'

for state in (states):
    print '<option value="">{0}</option>'.format(state)
	
print '</select>'

##The above does create a drop down with all the state names in it. Most likely
##it wouldn't work though because it's just a list of the names with no index
##There needs to be an index key to match with what's in the database. The
##state name is just the display name. So adding an abbreviation for the index,
##in a real situation this could also be an ID number. Depends on what is in the
##database.

states = ['Alabama', 'Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
abbreviations = ['AL','AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA','HI', 'ID', 'IL', 'IN','IA','KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR','PA','RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']


print '<select name = "state">'
print '<option value="">Select State</option>'

for abbr, state in zip(abbreviations,states):
    print '<option value="{0}">{1}</option>'.format(abbr,state)
	
print '</select>'


