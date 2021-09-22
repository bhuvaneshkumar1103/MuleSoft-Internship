#importing the sqlite3 database to this file.
import sqlite3

#creating a try and exception block if any error occured during the process.
try:
    # creating a database with name = moviesdata and making a connection with it.
    connector = sqlite3.connect('MoviesDataBase.db')
    cur = connector.cursor()
    print("Created and Opened Database successfully !!!")
    
        
    '''creating a new table with name = Movies with parameters such as,
       movie name, actor name, actress name,director name and 
       finally year of release of the movie.'''
    cur.execute("""CREATE TABLE MOVIES(MOVIE_NAME TEXT, ACTOR_NAME TEXT, ACTRESS_NAME TEXT, DIRECTOR_NAME TEXT, YEAR_OF_RELEASE_MOVIE INT) """)
    print("Table created Successfully !!!")
    
    #Insering the values in the Movies table.
    cur.execute("INSERT INTO MOVIES VALUES('Avengers:Endgame','Chris Evans','Scarlett Johansson','Anthony Russo',2019)")
    cur.execute("INSERT INTO MOVIES VALUES('Inception','Leonardo DiCaprio','Marion Cotillard','Christopher Nolano',2010)")
    cur.execute("INSERT INTO MOVIES VALUES('The Pursit of Happyness','Will Smith','Thandiwe Newton','Gabriele Muccino',2006)")
    cur.execute("INSERT INTO MOVIES VALUES ('The Matrix','Keanu Reeves','Carrie-Anne Moss',1999,'Lana Wachowski')")
    print("Data Inserted Successfully !!!")

    #Quering data from the Movies table.
    cur.execute("SELECT * FROM MOVIES")
    print(cur.fetchall())
    print("----------------------------------------")
    cur.execute("SELECT * FROM MOVIES WHERE ACTRESS_NAME = 'Scarlett Johansson'")
    print(cur.fetchall())
    print("Displayed the queries successfully !!!")
    
    connector.commit()
    

except Exception as err:
    print("ERROR OCCURED AT:",str(err))
