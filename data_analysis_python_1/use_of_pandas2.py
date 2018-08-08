import os

import pandas as pd

data_folder = os.path.join("input")

u_names = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('input/users.dat', sep='::', header=None,
                      names=u_names, engine='python')
r_names = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('input/ratings.dat', sep='::', header=None,
                        names=r_names, engine='python')
m_names = ['movie_id', 'title', 'genres']
movies = pd.read_table('input/movies.dat', sep='::', header=None,
                       names=m_names, engine='python')  # avoiding warning by using engine='python'
print(users[:5])
print(ratings[:5])
print(movies[:5])
