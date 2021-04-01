import os
# connection credentials
os.environ['DB_URL'] = 'postgresql+psycopg2://test_user:password@127.0.0.1:5432/test_db'
DB_URL = os.environ['DB_URL']
# entities properties
ACTOR_FIELDS = ['id', 'name', 'gender', 'date_of_birth']
MOVIE_FIELDS = ['id', 'name', 'year', 'genre']

# date of birth format
DATE_FORMAT = '%d.%m.%Y'