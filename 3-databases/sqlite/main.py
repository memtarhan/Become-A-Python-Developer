import sqlite3

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()


def create_movies_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Year INT)''')
    connection.commit()


def add_movie():
    cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1976)")
    connection.commit()


def add_movies(movies: [()]):
    cursor.executemany('INSERT INTO Movies VALUES (?, ?, ?)', movies)
    connection.commit()


def fetch_movies():
    return cursor.execute("SELECT * FROM Movies")


def fetch_single_movie():
    cursor.execute("SELECT * FROM Movies")
    return cursor.fetchone()


def close_connection():
    connection.close()


famous_movies = [
    ('Pulp Fiction', 'Quentin Tarantino', 1994)
]

if __name__ == '__main__':
    # add_movies(famous_movies)
    movies = fetch_movies()
    for movie in movies:
        print(movie)
    close_connection()
