import db 

database = 'rubyquest.db'
dbConnection = db.connect(database)

query = 'select id, name from person where id = 7;'
dbConnection.setQuery(query)

dbConnection.execute()

data = dbConnection.fetch()

dbConnection.printSnippet(data)