__author__ = 'Joël'


import sqlite3
conn = sqlite3.connect('data.db')

# Zet fire (brandmelder) op 0. Als deze op 1 staat, gaan alle deuren open.
c = conn.cursor()

c.execute("""DROP TABLE IF EXISTS persoon""")
c.execute("""DROP TABLE IF EXISTS versleuteling""")
c.execute("""DROP TABLE IF EXISTS history""")
c.execute("""DROP TABLE IF EXISTS terminal""")
c.execute("""DROP TABLE IF EXISTS fire""")
# Create tables
c.execute("""CREATE TABLE fire
             ('Fire' integer)""")

c.execute("""CREATE TABLE persoon
             ('UID' integer primary key, 'CID' integer, 'Naam' text, 'Rechten' integer, 'Access' text)""")
# Rechten is een integer die aangeeft welke 'rang' de gebruiker heeft.
# 1 is gast, 2 is schoonmaker, 3 is beveiliging, 4 is eigenaar. Uitbreiding mogelijk.
# De persoon met de hoogste rank moet overal bijkunnen.

c.execute("""CREATE TABLE versleuteling
             ('KeyID' integer, 'key' text)""")

c.execute("""CREATE TABLE terminal
             ('TID' integer primary key, 'Rechten' integer, 'CID' integer)""")
# Rechten is een integer die aangeeft welke 'rang' de gebruiker heeft.
# 1 is gast, 2 is schoonmaker, 3 is beveiliging, 4 is eigenaar. Uitbreiding mogelijk.
# De persoon met de hoogste rank moet overal bijkunnen.

c.execute("""CREATE TABLE history
             ('Naam' text, 'CID' integer, 'Datum' text, 'TID' integer)""")

c.execute("""INSERT INTO fire VALUES (0)""")
c.execute("""INSERT INTO persoon VALUES (1, 3529442660, 'Dirk-Jan Verandering', 3, 'Aan')""")
c.execute("""INSERT INTO persoon VALUES (2, 4039826975, 'Jan Janssen', 4, 'Aan')""")
c.execute("""INSERT INTO persoon VALUES (3, 1694667529, 'Meneer De Schoonmaker', 2, 'Aan')""")
c.execute("""INSERT INTO persoon VALUES (4, 641312192, 'Jeroen Weener STUDENT', 1, 'Aan')""")
c.execute("""INSERT INTO persoon VALUES (5, 1918555232, 'Joël Ledelay STUDENT', 1, 'Aan')""")
c.execute("""INSERT INTO persoon VALUES (6, 1695383881, 'Joël Ledelay OV', 1, 'Aan')""")
c.execute("""INSERT INTO persoon VALUES (7, 2649988782, 'Menno Schober OV', 1, 'Aan')""")
c.execute("""INSERT INTO terminal VALUES (1, 4, 0)""")
c.execute("""INSERT INTO terminal VALUES (2, 3, 0)""")
c.execute("""INSERT INTO terminal VALUES (3, 2, 0)""")
c.execute("""INSERT INTO terminal VALUES (4, 1, 641312192)""")
c.execute("""INSERT INTO terminal VALUES (5, 1, 1918555232)""")
c.execute("""INSERT INTO terminal VALUES (6, 1, 1695383881)""")
c.execute("""INSERT INTO terminal VALUES (7, 1, 2649988782)""")


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

# CID in tabel terminal geeft aan welke card id de kamer in mag. Als de CID in de terminal 0 is, maakt het niet uit.