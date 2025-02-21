import db 

database = 'rubyquest.db'
dbConnection = db.connect(database)

query = 'select region, name from city where region = 1;'
dbConnection.setQuery(query)

dbConnection.execute()

data = dbConnection.fetch()

dbConnection.printSnippet(data)