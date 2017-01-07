##PIG LATIN TRANSLATOR

print 'Welcome to the Pig Latin Translator!'

suff= "ay"

word =raw_input ("please enter a word. ")

if len (word)> 0 and word.isalpha():
    word = word.lower()
    first_letter = word [0]
    new_word = word + first_letter + suff
    
    tran_word = new_word [1:]
    
    print tran_word

else:
    print "no word entered"
