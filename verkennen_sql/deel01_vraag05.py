import db 

database = 'rubyquest.db'
dbConnection = db.connect(database)

query = 'select name from armor'
dbConnection.setQuery(query)

dbConnection.execute()

data = dbConnection.fetch()

dbConnection.printSnippet(data)