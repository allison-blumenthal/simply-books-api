BOOKS = [
    {
      "id": 1,
      "title": "Old Possom's Book of Practical Cats",
      "image": "https://m.media-amazon.com/images/I/61FJmS+33YL._SX260_.jpg",
      "price": 21,
      "sale": False,
      "description": "These lovable cat poems were written by T. S. Eliot for his godchildren and continue to delight children and adults alike. This collection is a curious and artful homage to felines young and old, merry and fierce, small and unmistakably round. This edition features vibrant illustrations by Axel Scheffler."
    },
    {
      "id": 2,
      "title": "My Life in a Cat House",
      "image": "https://m.media-amazon.com/images/I/41rsIwoUhKS._SY346_.jpg",
      "price": 9,
      "sale": True,
      "description": "Gwen Cooper—author of the blockbuster bestseller Homer's Odyssey: A Fearless Feline Tale, or How I Learned About Love and Life With a Blind Wonder Cat—returns with the ongoing adventures of her much-beloved, world-famous fur family. Ideal for new readers and longtime fans alike, this memoir told in eight purr-fect cat stories is filled with all the humor and heart Gwen's devoted readership has come to know and love."
    },
    {
      "id": 3,
      "title": "The Travelling Cat Chronicles",
      "image": "https://m.media-amazon.com/images/I/518ILrdwEGL.jpg",
      "price": 11,
      "sale": True,
      "description": "A book that “speak[s] volumes about our need for connection—human, feline or otherwise” (The San Francisco Chronicle), The Travelling Cat Chronicles is a life-affirming anthem to kindness and self-sacrifice that shows how the smallest things can provide the greatest joy—the perfect gift for cat lovers and travellers!"
    }
]

def get_all_books():
    return BOOKS
  
def get_single_book(id):
  requested_book = None
  
  for book in BOOKS:
    if book["id"] == id:
      requested_book = book
  
  return requested_book

def create_book(book):
  max_id = BOOKS[-1]["id"]
  
  new_id = max_id + 1
  
  book["id"] = new_id
  
  BOOKS.append(book)
  
  return book
