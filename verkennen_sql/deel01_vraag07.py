import db 

database = 'rubyquest.db'
dbConnection = db.connect(database)

query = 'select name, health from creature'
dbConnection.setQuery(query)

dbConnection.execute()

data = dbConnection.fetch()

dbConnection.printSnippet(data)