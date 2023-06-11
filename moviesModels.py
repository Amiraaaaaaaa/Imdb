from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

# Database connection details
DB_HOST = 'localhost'
DB_NAME = 'your_database_name'
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'

# Route for the search page
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        #Creating request forms for the search filters
        search_criteria = request.form['search_criteria']
        genre_filter = request.form['genre_filter']
        min_rating = request.form['min_rating']
        year_filter = request.form['year_filter']
        actors_filter = request.form['actors_filter']
        
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        cursor = conn.cursor()
        
        # Construct the SQL query
        query = "SELECT * FROM movies WHERE title ILIKE '%{}%'".format(search_criteria)
        
        # Genre filter
        if genre_filter:
            query += " AND genre ILIKE '%{}%'".format(genre_filter)
        
        # Rating filter
        if min_rating:
            query += " AND rating >= {}".format(min_rating)
        
        # Year of release filter
        if year_filter:
            query += " AND year = {}".format(year_filter)
         # Actors filter
         if actors_filter:
            query += " AND actor = {}".format(actors_filter)
        
        # Execute the SQL query
        cursor.execute(query)
        
        # Fetch the results
        movies = cursor.fetchall()
        
        # Close the database connection
        cursor.close()
        conn.close()
        
        return render_template('results.html', movies=movies)
    
    return render_template('search.html')

if __name__ == '__main__':
    app.run()
