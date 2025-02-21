import db 

database = 'rubyquest.db'
dbConnection = db.connect(database)

query = 'select * from animal except type = sheep;'
dbConnection.setQuery(query)

dbConnection.execute()

data = dbConnection.fetch()

dbConnection.printSnippet(data)