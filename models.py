from flask import Flask
from psycopg2 import sql
import __init__
from IMDB import conn


#selecting a movie by it's serial tiltle 
def select_movies(serial_title):
    cur = conn.cursor()
    sql = """
    SELECT Movies
    FROM Movies 
    WHERE Movies.Series_Title = 'The Dark Knight'

    ;
    """
    cur.execute(sql, (serial_title,))
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset


#selecting a movie by it's serial tiltle 

def select_movies(serial_title):
    cur = conn.cursor()
    sql = """
    SELECT Movies
    FROM Movies
    WHERE Movies.Series_Title = 'The Godfather'
    ;
    """
    cur.execute(sql, (serial_title,))
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset

#delete movies that has a rating > 9
def delete_movies1(serial_title):
    cur = conn.cursor()
    sql = """
    DELETE FROM Movies
    WHERE IMDB_Rating > 9;
     ;
    """
    cur.execute(sql, (serial_title,))
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset
