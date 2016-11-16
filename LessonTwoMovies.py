##Create lists - keep things in the same order

movies =['Galaxy Quest','Snow Cake','Truly Madly Deeply','Mesmer','Judas Kiss']
parent_rate=['PG','NR','PG','NR','R']
IMDB_rate=['7.3','7.6','7.3','6.2','6.4']
bechdel=['1','3','No bechdel','No bechdel','No bechdel']
genre=['Adventure/Action/Comedy','Drama/Romance','Comedy/Drama/Fantasy','Biography/Drama','Crime/Drama/Thriller']


print 'Alan Rickman film fest!'

for movie, rate, imdb, bech, gen in zip(movies, parent_rate, IMDB_rate,bechdel, genre):
    print "{0},{1},{2},{3},{4}".format (movie, rate, imdb, bech, gen)
