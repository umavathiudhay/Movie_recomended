from tkinter import *
import sqlite3
main_screen = Tk()
main_screen.geometry("300x250")
main_screen.title("Movie Recommentation System")

    
 
# Set text variables
user= StringVar()
movie = StringVar()
rating=StringVar()
id=StringVar()
def database():
   nameid=user.get()
   movieid=movie.get()
   ratingid=rating.get()
   idno=id.get()
   
   conn = sqlite3.connect('predict.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS predict (user TEXT,movie TEXT,rating TEXT,id TEXT)')
   cursor.execute('INSERT INTO  predict(user,movie,rating,id) VALUES(?,?,?,?)',(nameid,movieid,ratingid,idno))
   conn.commit()
 
# Set label for user's instruction
Label(main_screen, text="Please enter details below", bg="orange").pack()
Label(main_screen, text="").pack()
    
# Set username label
user_lable = Label(main_screen, text="user  ")
user_lable.pack()
 
# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    
user_entry = Entry(main_screen, textvariable=user)
user_entry.pack()
   
# Set password label
movie_lable = Label(main_screen, text="movie  ")
movie_lable.pack()

movie_entry = Entry(main_screen, textvariable=movie)
movie_entry.pack()

rating_lable = Label(main_screen, text="rating  ")
rating_lable.pack()

rating_entry = Entry(main_screen, textvariable=rating)
rating_entry.pack()


id_lable = Label(main_screen, text="id ")
id_lable.pack()

id_lable = Entry(main_screen, textvariable= id)
id_lable.pack()
    
Label(main_screen, text="").pack()
# Set register button
Button(main_screen, text="Submit", width=10, height=1, bg="blue",command=database).pack()


main_screen.mainloop()



