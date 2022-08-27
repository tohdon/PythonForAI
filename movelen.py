import  pandas as pd 

pd.options.display.max_rows = 10

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('C:\\software\\python\\ml-1m\\users.dat', sep='::', header=None, names = unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings =  pd.read_table('C:\\software\\python\\ml-1m\\ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies =  pd.read_table('C:\\software\\python\\ml-1m\\movies.dat',encoding='ISO-8859-1', sep='::', header=None, names=mnames)
print(users[:5])
print(ratings[:5])

print(movies[:5])
data = pd.merge(pd.merge(ratings, users), movies)
print(data)
print(data.iloc[0])
mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
print(mean_ratings[:5])
ratings_by_title = data.groupby('title').size()
print(ratings_by_title[:10])
