class Books:
    def __init__(self, title, author, isbn, is_available:bool):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def display_book_info(self):
        
        print(f"ISBN:{self.isbn}, Title: {self.title}, Author:{self.author}, Status:{self.is_available}")

    def change_book_status(self):
        self.is_available = not self.is_available

class Members:
    def __init__(self, name, member_id, borrowed_books: list[Books]):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books

    def display_member_info(self):
        print(f"ID:{self.member_id}, Name: {self.name}")

    def display_borrowed_books(self):
        print(f"Borrowed_books:{self.borrowed_books}")
        

class Library:
    def __init__( self, books: list[Books], members: list[Members]):
        self.books= books
        self.members = members

    def display_library_books(self):
        for book in self.books:
            print(f"{book.title} {book.author} {book.isbn} {book.is_available}")

    def display_library_members(self):
        for member in self.members:
            book_list = [book.title for book in member.borrowed_books]
            print(f"{member.name} {member.member_id} {book_list}")

    def add_book(self, book):
        for new_book in self.books:
            if new_book.isbn == book.isbn:
                print(f"The {book.title} with isbn {book.isbn} is already exist")
                return

        self.books.append(book)

    def add_member(self, member):
        for new_member in self.members:
            if new_member.member_id == member.member_id:
                print(f"User with ID:{new_member.member_id} is already exists.")
                return
                
        self.members.append(member)

    def search_book(self, title):
        find_book= [ book for book in self.books if title in book.title]
        return find_book
        
    def borrow_book(self, member, book):
        if not any(m.member_id == member.member_id for m in self.members):
            return "Member does not exist."
                        
        if not any(b.isbn == book.isbn for b in self.books):
            return "There is no such book in library."
        
        if not book.is_available:
            return f"isbn:{book.isbn} is not available for borrowing."
        
        if len(member.borrowed_books) >=3:
            return f"Member has already borrowed {len(member.borrowed_books)} books."
        
           
        member.borrowed_books.append(book)
        book.change_book_status()
        return(f"{member.name} borrowed book with isbn:{book.isbn} title:{book.title}")
        
    def return_book(self, member, book):
        if not any(m.member_id == member.member_id for m in self.members):
            return "Member does not exist."
                        
        if not any(b.isbn == book.isbn for b in self.books):
            return "There is no such book in library."
        
        if book.is_available:
            return f"isbn:{book.isbn} has not being borrowed."
        
        if book in member.borrowed_books:
            member.borrowed_books.remove(book)
            book.change_book_status()
            return(f"{member.name} returned book with isbn:{book.isbn} title:{book.title}")

        else:
            return(f"{member.name} did not borrow book with isbn:{book.isbn} title:{book.title}")

    def library_report(self):
        available=0
        borrowed = 0
        borrowed_by_members =0
        for b in self.books: 
            if b.is_available:
                available +=1
        print (f"The number of available books: {available}")
        for b in self.books: 
            if not b.is_available:
                borrowed +=1

        for m in self.members:
            if len(m.borrowed_books)> 0:
                borrowed_by_members += len(m.borrowed_books)
                    
        print (f"Total number of borrowed books: {borrowed}")
        print (f"Total number of books in the library: {len (self.books)} ")
        print (f"Total number of members in the library: {len (self.members)} ")
        print (f"Total number of books that borrowed by members: {borrowed_by_members}")


    def validate_library_data(self):
        errors=[]
        isbn_record =set()
        for b in self.books:
            if b.isbn not in isbn_record:
                isbn_record.add(b.isbn)
            else:
                errors.append (f"Data integrity error: Duplicate ISBN found: {b.isbn}")  
            borrowing_count=0
            for m in self.members:
                for i in m.borrowed_books:
                    if b.isbn == i.isbn:
                        borrowing_count +=1
            if borrowing_count >1:
               errors.append("Data integrity error: A book cannot be borrowed by more than one member at a time.")           
            if not b.is_available:
                if borrowing_count ==0:
                   errors.append(f"Data integrity error: Book {b.isbn} status is inconsistent. The book is not borrowed but marked as unavailable.")

            if b.is_available and borrowing_count>0:
               errors.append(f"Data integrity error: Book {b.isbn} status is inconsistent. The book is borrowed but marked as available.")
       
        return errors



'''books = [
    {"isbn": 1, "title": "کتاب۱", "author": "نویسنده۱", "is_available": True},
    {"isbn": 2, "title": "کتاب۲", "author": "نویسنده۲", "is_available": False},
]

members = [
    {"member_id": 1, "name": "علی", "borrowed_books": []},
    {"member_id": 2, "name": "مریم", "borrowed_books": []},
]
lib = Library(books, members)

print(lib.books)
print(lib.members)
print(len(lib.books))       
print(lib.books[0]["title"])'''


book3=Books("کتاب3", "نویسنده3", 3,  False)
book4=Books("book4", "author4", 4,  False)


member3 = Members("reza", 3, [])
member4 = Members("reza", 8, [])
member5 = Members("mel", 7, [])
member6 = Members("dela", 6, [])

#lib = Library([], [])

book1 = Books("Python", "Author A", 101, True)
book2 = Books("Python Advanced", "Author B", 101, True)

member1 = Members("Ali", 1, [book1])
member2 = Members("Sara", 2, [])

lib = Library([book1, book2], [member1, member2])
members = [member1, member2, member3, member4]
books=[book1, book2, book3, book4]


#lib.display_library_books()

result=lib.validate_library_data()
print(result)

'''   
print(len(lib.books))
print(len(lib.members))
for book in lib.books:
    book.display_book_info()'''


'''
for member in lib.members:
    member.display_member_info()
result= lib.search_book("booke")
for book in result:
    book.display_book_info()


returned = lib.return_book(member1, book1)
print(returned)'''
