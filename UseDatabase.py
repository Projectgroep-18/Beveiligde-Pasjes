__author__ = 'Joël'


import sqlite3
conn = sqlite3.connect('data.db')

c = conn.cursor()
# We gaan uit van byteorder = big
userid = int.from_bytes(b'3529442660', byteorder='big')
print(userid)

def check(userid):
    c.execute("""SELECT UID from persoon WHERE UID = %i """ % userid)
    persoon = c.fetchall()
    if persoon:
        print('Open deur')
        return persoon
    else:
        print('NO.')
        False

check(userid)

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()