import db 

database = 'rubyquest.db'
dbConnection = db.connect(database)

query = 'select owner, type from animal where owner > 0;'
dbConnection.setQuery(query)

dbConnection.execute()

data = dbConnection.fetch()

dbConnection.printSnippet(data)