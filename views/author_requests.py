AUTHORS = [
    {
      "id": 1,
      "email": "author1@gmail.com",
      "first_name": "Author1",
      "last_name": "One",
      "image": "https://thumbs.dreamstime.com/b/author-word-wood-type-abstract-vintage-letterpress-printing-blocks-80925459.jpg",
      "favorite": True
    },
    {
      "id": 2,
      "email": "author2@gmail.com",
      "first_name": "Author2",
      "last_name": "Two",
      "image": "https://www.shutterstock.com/image-photo/concept-dices-letters-forming-words-260nw-127361840.jpg",
      "favorite": False
    },
    {
      "id": 3,
      "email": "author3@gmail.com",
      "first_name": "Author3",
      "last_name": "Three",
      "image": "https://images.unsplash.com/photo-1455390582262-044cdead277a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8YXV0aG9yfGVufDB8fDB8fA%3D%3D&w=1000&q=80",
      "favorite": True
    }
]

def get_all_authors():
    return AUTHORS
  
def get_single_author(id):
  requested_author = None
  
  for author in AUTHORS:
    if author["id"] == id:
      requested_author = author
  
  return requested_author

def create_author(author):
  #get the id value of the last author in the list
  max_id = AUTHORS[-1]["id"]
  
  # add 1 to whatever that number was
  new_id = max_id + 1
  
  # add an `id` property to the author dictionary
  author["id"] = new_id

  # add the author dictionary to the list
  AUTHORS.append(author)

  # return the dictionary with `id` property added
  return author 

def delete_author(id):
  # initial -1 value for author index, in case one isn't found
  author_index = -1
  
  # iterate the AUTHORS list, but use enumerate() so that you
  # can access the index calue of each item
  for index, author in enumerate(AUTHORS):
    if author["id"] == id:
      # found the author. store the current index.
      author_index = index
  
  # if the author was found, use pop(int) to remove it from the list
  if author_index >= 0:
    AUTHORS.pop(author_index)
  
