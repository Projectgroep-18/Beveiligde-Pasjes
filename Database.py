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
             ('UID' integer primary key, 'CID' integer, 'Naam' text, 'Rechten' text, 'Access' text)''')

c.execute('''CREATE TABLE versleuteling
             ('KID' integer, 'key' text)''')

c.execute('''CREATE TABLE terminal
             ('TID' integer primary key, 'Rechten' text)''')

c.execute('''CREATE TABLE history
             ('UID' integer primary key, 'CID' integer, 'Datum' text, 'tijd' text, 'TID' integer)''')

c.execute('''INSERT INTO persoon VALUES (1, 241821987043432866395696, 'Dirk-Jan Verandering', 'Gast', 'Uit')''')
c.execute('''INSERT INTO persoon VALUES (2, 246452191867917525661493, 'Jan Janssen', 'Eigenaar', 'Aan')''')
c.execute('''INSERT INTO persoon VALUES (3, 100000000000000000000000, 'Mevrouw De Schoonmaakster', 'Schoonmaker', 'Aan')''')
c.execute('''INSERT INTO terminal VALUES (1, 'Eigenaar')''')
c.execute('''INSERT INTO terminal VALUES (2, 'Gast')''')
c.execute('''INSERT INTO terminal VALUES (3, 'Schoonmaker')''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()