import db 

database = 'rubyquest.db'
dbConnection = db.connect(database)

query = 'select gold, title from quest where gold = 0;'
dbConnection.setQuery(query)

dbConnection.execute()

data = dbConnection.fetch()

dbConnection.printSnippet(data)