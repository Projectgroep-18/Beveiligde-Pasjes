__author__ = 'Joël'


import sqlite3
conn = sqlite3.connect('data.db')

c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS persoon''')
c.execute('''DROP TABLE IF EXISTS versleuteling''')
c.execute('''DROP TABLE IF EXISTS history''')
c.execute('''DROP TABLE IF EXISTS terminal''')
# Create table
c.execute('''CREATE TABLE persoon
             ('UID' integer primary key, 'CID' integer, 'Naam' text, 'Rechten' integer, 'Access' text)''')
# Rechten is een integer die aangeeft welke 'rang' de gebruiker heeft.
# 1 is gast, 2 is schoonmaker, 3 is beveiliging, 4 is eigenaar. Uitbreiding mogelijk.
# De persoon met de hoogste rank moet overal bijkunnen.

c.execute('''CREATE TABLE versleuteling
             ('KeyID' integer, 'key' text)''')

c.execute('''CREATE TABLE terminal
             ('TID' integer primary key, 'Rechten' integer, 'CID' integer)''')
# Rechten is een integer die aangeeft welke 'rang' de gebruiker heeft.
# 1 is gast, 2 is schoonmaker, 3 is beveiliging, 4 is eigenaar. Uitbreiding mogelijk.
# De persoon met de hoogste rank moet overal bijkunnen.

c.execute('''CREATE TABLE history
             ('UID' integer primary key, 'CID' integer, 'Datum' text, 'tijd' text, 'TID' integer)''')

c.execute('''INSERT INTO persoon VALUES (1, 241821987043432866395696, 'Dirk-Jan Verandering', 3, 'Aan')''')
c.execute('''INSERT INTO persoon VALUES (2, 246452191867917525661493, 'Jan Janssen', 4, 'Aan')''')
c.execute('''INSERT INTO persoon VALUES (3, 232396203819758364471865, 'Mevrouw De Schoonmaakster', 2, 'Aan')''')
c.execute("""INSERT INTO persoon VALUES (4, 255970565998217052893709, 'Jeroen Weener STUDENT', 1, 'Aan')""")
c.execute("""INSERT INTO persoon VALUES (5, 232450968716023256199986, 'Joël Ledelay STUDENT', 1, 'Aan')""")
c.execute("""INSERT INTO persoon VALUES (6, 232396204097943329323057, 'Joël Ledelay OV', 1, 'Aan')""")
c.execute("""INSERT INTO persoon VALUES (7, 237118211425339845326898, 'Menno Schober OV', 1, 'Aan')""")
c.execute('''INSERT INTO terminal VALUES (1, 4, 0)''')
c.execute('''INSERT INTO terminal VALUES (2, 3, 0)''')
c.execute('''INSERT INTO terminal VALUES (3, 2, 0)''')
c.execute('''INSERT INTO terminal VALUES (4, 1, 0)''')
c.execute('''INSERT INTO terminal VALUES (5, 1, 246452191867917525661493)''')
c.execute('''INSERT INTO terminal VALUES (6, 1, 0)''')


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

# CID in tabel terminal geeft aan welke card id de kamer in mag. Als de CID in de terminal 0 is, maakt het niet uit.