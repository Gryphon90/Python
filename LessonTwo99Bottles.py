##print 99 bottles of beer song using range and loop


for bot_num in range (99,0,-1):
    print '''{0} bottles of beer on the wall, {0} bottles of beer...
If one of those bottles should happen to fall, {1} bottles of beer on the wall'''.format(bot_num, bot_num-1)


##1 bottles of beer is not grammatically correct so could make range end
##at 2 and print last lines outside of range


for bot_num2 in range (99,2,-1):
    print '''{0} bottles of beer on the wall, {0} bottles of beer...
If one of those bottles should happen to fall, {1} bottles of beer on the wall'''.format(bot_num2, bot_num2-1)

print '''2 bottles of beer on the wall, 2 bottles of beer...
If one of those bottles should happen to fall, 1 bottle of beer on the wall
1 bottle of beer on the wall, 1 bottle of beer...
If that bottle should happen to fall, 0 bottles of beer on the wall'''

##Or could make a ranges for the last 2 bottles


for bot_num3 in range (99,2,-1):
    print '''{0} bottles of beer on the wall, {0} bottles of beer...
If one of those bottles should happen to fall, {1} bottles of beer on the wall'''.format(bot_num3, bot_num3-1)


for bot_num4 in range (2,1,-1):
    print '''{0} bottles of beer on the wall, {0} bottles of beer...
If one of those bottles should happen to fall, {1} bottle of beer on the wall'''.format(bot_num4,bot_num4-1)

for bot_num5 in range (1,0,-1):
    print'''{0} bottle of beer on the wall, {0} bottle of beer...
If that bottle should happen to fall, {1} bottles of beer on the wall'''.format(bot_num5,bot_num-1)
