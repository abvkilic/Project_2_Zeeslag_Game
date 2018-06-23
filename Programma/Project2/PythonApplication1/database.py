import psycopg2


# Use the database
def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=Battleport user=postgres password=root")
    cursor = connection.cursor()

    # Execute the command
    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # Nothing to fetch
        pass

    # Close connection
    cursor.close()
    connection.close()

    return results


# Uploads a score into the hiscore table
def upload_score(playername, beurten):
    connection = psycopg2.connect("dbname=Battleport user=postgres password=root")
    cursor = connection.cursor()

    # Execute the command
    cursor.execute("""INSERT INTO highscore (playername, beurten) VALUES(%(name)s, %(turn)s);""",
                   {'name': playername, 'turn': beurten})
    connection.commit()

# Downloads score data from database
def download_scores():
    return interact_with_database("SELECT * FROM Highscore ORDER BY beurten LIMIT 5")

def NormalCards():
    return interact_with_database("SELECT * FROM Deck WHERE cardtype = 1")




# Downloads the top score from database
def download_top_score():
    result = interact_with_database("SELECT * FROM Highscore ORDER BY beurten")[0][1]
    return result

# Downloads all the cards from the database
# def download_cards():
#    result = interact_with_database("SELECT * FROM Cards")
#    return result
