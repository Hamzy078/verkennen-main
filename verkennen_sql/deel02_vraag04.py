import db 

database = 'rubyquest.db'
dbConnection = db.connect(database)

query = 'select type from animal where type = Sheep;'
dbConnection.setQuery(query)

dbConnection.execute()

data = dbConnection.fetch()

dbConnection.printSnippet(data)