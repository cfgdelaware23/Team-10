import sqlite3



connection = sqlite3.connect('./db.sqlite3')
cursor_v = connection.cursor()
cursor_e = connection.cursor()

#a query for volunteers
#cursor_v.execute('SELECT Email FROM myapp_volunteer')
#cursor_e.execute('SELECT * FROM myapp_events')
Emaildata= cursor_v.execute('SELECT Email FROM myapp_volunteer').fetchall()
Eventsdata= cursor_e.execute('SELECT * FROM myapp_events').fetchall()

