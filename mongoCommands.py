users.insert({
	name: 'Joe, but better',
	holdings: {
		ticker: 'holdings tick',
		count: 5,
	},
	trade_hist: {
		date: 'date time',
		count: 5,
		ticker: 'trade tick',
		id: 100,
	}
})



# db.users.insert() is deprecated!!!
# db.users.remove() is deprecated!!!


##### Python Code
users.insert_one({ 'name': 'Joe, but better', 'holdings': {'ticker': 'holdings tick', 'count': 5,}, 'trade_hist': {'date': 'date time', 'count': 5, 'ticker': 'trade tick', 'id': 100} })

users.delete_one({ 'name': 'Joe, but better' })

search = users.find_one({'name': 'Joe, but better'})
print(search.get('name'))


##### Shell
db.users.insertOne({ name: 'Joe, but better', holdings: {ticker: 'holdings tick', count: 5,}, trade_hist: {date: 'date time', count: 5, ticker: 'trade tick', id: 100} })

db.users.deleteOne({ name: 'Joe' })

db.users.find({ name: 'Testing!' })