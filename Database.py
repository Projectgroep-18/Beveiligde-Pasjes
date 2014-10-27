__author__ = 'Joël'


import sqlite3
conn = sqlite3.connect('data.db')

c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS persoon''')
c.execute('''DROP TABLE IF EXISTS versleuteling''')
c.execute('''DROP TABLE IF EXISTS history''')

# Create table
c.execute('''CREATE TABLE persoon
             ('UID' integer, 'Naam' text, 'Rechten' text)''')

c.execute('''CREATE TABLE versleuteling
             ('KID' integer, 'key' text)''')

c.execute('''CREATE TABLE history
             ('UID' integer, 'Datum' text, 'tijd' text, 'TID' integer)''')

c.execute('''INSERT INTO persoon VALUES (3529442660, 'Dirk-Jan Verandering', 'Gast')''')
c.execute('''INSERT INTO persoon VALUES (4039826975, 'Jan Janssen', 'Eigenaar')''')
# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()