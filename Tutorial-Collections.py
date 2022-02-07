#collections - tutorial dixtionary
books = {"The Handmaiden's Tale":"Margaret Atwood", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}
print(books["The Handmaiden's Tale"])
# add a new key-value pair
books["Treasure Island"] = "Robert Louis Stevenson"
print (books)
print(tuple(books.items()))
print ("J.K. Rowling " in books)  #false
print ("Roald Dahl" in books.values())  #true
