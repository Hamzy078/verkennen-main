import db 

database = 'rubyquest.db'
dbConnection = db.connect(database)

query = 'select * from quest'
dbConnection.setQuery(query)

dbConnection.execute()

data = dbConnection.fetch()

dbConnection.printSnippet(data)