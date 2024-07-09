# blank vs. null:
# blank = True,    when providing a value for this model field(via a form), this field may be blank (empty)
# null = True,     when no value is received for that field, the special NULL value should be store in DataBase.
# if null = False,  You have to ensure that some default value is set in case of blank values.


# Updating Data in Database:
#
# Firstly, write this data in shell
# from book_outlet.models import Book
# code:
# harry_potter = Book.objects.all()[0]
# harry_potter.title    # "Harry Potter 1 - The Philosopher's stone"
# lotr = Book.objects.all()[1]
# lotr.title      # 'Lord Of the rings'
#
#
# Now; if I write in shell and hit enter
# harry_potter.author = 'J.K. Rowling'
# It won't do anything yet, now also write this and hit enter it not do anything,
# harry_potter.is_bestselling = True
# Now,
# harry_potter.save()
# Now if I write upper code and hit enter then it now not generate any new thing in Database, and it just Updates the Database.
# To verify!,
# Book.objects.all()[0].author  # Output: 'J.K. Rowling'


# Delete Data in Database:
# code for shell:
# lotr = Book.objects.all()[1]
# lotr.delete()
# It will delete data from database
# Now if write,
# Book.objects.all()
# It will return: <QuerySet [<Book: Harry Potter 1 - The Philosopher's stone (5)>]>

# create():
# For faster data enter a database, write in shell like
# Book.objects.create(title='Lord Of the Rings', rating=4, author='r.j. shah', is_bestselling=True)
# Book.objects.create(title='My Diary', rating=2, author='k.k. rajkumar', is_bestselling=True)
# Book.objects.create(title='Random', rating=1, author='Random Dude', is_bestselling=False)



# Querying & Filtering Data:
# For getting data on certain condition bases like id = 2 or title = 'Lord Of The Rings' then write like,
# Book.objects.get(title='Lord Of the Rings')   # return: <Book: Lord Of the Rings (4)>
# Book.objects.get(rating=5)
#
# Remember:
# Book.objects.get(is_bestselling=True)
# Then it will return more than one book, and it not handles by get method, get method handle only that query which return single value so pass inside like that query.







