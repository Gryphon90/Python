#Variables
studybuddy_1 = 'Terri Lagosita, 1485 Oak Lane, Liverpool, NY 13088'
studybuddy_2 = 'Jane Morel, 892 Linden Court, Dewitt, NY 13214'
studybuddy_3 = 'Megan Dugan, 25 Willow Way, Central Square, NY 13036'
studybuddy_4 = 'Linda Maquire, 159 Lackdon Alley, Syracuse, NY 13202'
studybuddy_5 = 'Cindy Starmela, 6781 Blackdon ST, N. Syracuse, NY 13211'

ZIP1 = studybuddy_1 [-5:]
ZIP2 = studybuddy_2 [-5:]
ZIP3 = studybuddy_3 [-5:]
ZIP4 = studybuddy_4 [-5:]
ZIP5 = studybuddy_5 [-5:]



#Goal 1 - Create a program that simply shows all the ZIP codes, each on it's own line
#could have also printed the zip variables
print 'Goal 1\n'

print studybuddy_1 [-5:]
print studybuddy_2 [-5:]
print studybuddy_3 [-5:]
print studybuddy_4 [-5:]
print studybuddy_5 [-5:]


#Goal 2 - Output all ZIP codes on a single line with text explaining what they are
print '\nGoal 2\n'


print 'The study group covers a wide geographic ares there are participates from {0}, {1}, {2}, {3}, {4}.'.format ((ZIP1),(ZIP2),(ZIP3),(ZIP4),(ZIP5))



#Goal 3 - show study buddy's first name and zip separate by text

print '\nGoal3\n'


First1_sp = studybuddy_1.find(' ')
First2_sp = studybuddy_2.find(' ')
First3_sp = studybuddy_3.find(' ')
First4_sp = studybuddy_4.find(' ')
First5_sp = studybuddy_5.find(' ')

First1 = (studybuddy_1[:First1_sp])
First2 = (studybuddy_2[:First2_sp])
First3 = (studybuddy_3[:First3_sp])
First4 = (studybuddy_4[:First4_sp])
First5 = (studybuddy_5[:First5_sp])

print '''{0} lives at {1}
{2} lives at {3}
{4} lives at {5}
{6} lives at {7}
{8} lives at {9}'''.format ((First1), (ZIP1), (First2),
                            (ZIP2), (First3), (ZIP3),(First4),
                            (ZIP4), (First5),(ZIP5))





