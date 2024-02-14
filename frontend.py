from connectToFilmFlix import *

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root=Tk() #defines a window
root.title(f'Filmflix Database - {status}')
root.minsize(960,400) #minimum window size
label1 = Label(root, text="Welcome to the FilmFlix Database Control Panel", font=('Sans serif', 22))
#define a dropdown selection box for Search by genre

combo=ttk.Combobox()

combo=ttk.Combobox(state="readonly", values=["action", "comedy", "documentary", "drama", "mystery","science fiction"], width=15)
combo.set("action")

combo.place(x=774, y=88)
#create a label for the combo box
combolabel1=Label(root, text="Search by Film Genre")
combolabel1.place(x=740, y=65)

combolabel2=Label(root, text="Search by Release Year")
combolabel2.place(x=740, y=155)
year=Entry(root, width=5, font=("Arial",12))
year.place(x=854, y=180)

label9=Label(root, text="                                     ", pady=20)

#define a dropdown selection box for Search by Rating
combo2=ttk.Combobox()
combo2=ttk.Combobox(state="readonly", values=["U", "PG", "12A", "15", "18"], width=4)
combo2.set("U")

combo2.place(x=850, y=270)
combolabel2=Label(root, text="Search by Rating")
combolabel2.place(x=740, y=245)

#Define a dropdown box for the rating entry by user
comborating=ttk.Combobox()
comborating=ttk.Combobox(state="readonly", values=("U", "PG","12A", "15", "18"), width=4, font=("Arial",12))
comborating.set("U")
comborating.place(x=178, y=174)

#Define a dropdown box for genre entry by user
combo3=ttk.Combobox()
combo3=ttk.Combobox(state="readonly", values=["action", "comedy", "documentary", "drama", "mystery","science fiction"], width=14)
combo3.set("action")
combo3.place(x=178, y=234)

label9.grid(row=11, column=1)
label10=Label(root, text=" #ID       Film                Release Yr   Rating  Running Time     Genre" )
label10.grid( sticky=W,row=14, column=1)

text=Text(root, width=70, height=6, font=("Arial",12))





text.grid(sticky="W",row=15, column=1)

label3 = Label(root, text="Instructions:\nTo add a record, please fill in all of the yellow fields, select rating and genre, then click the 'ADD RECORD' button.\nTo find a record, input the Film ID and click the '*FIND RECORD BY ID*' button.\nTo delete a record, put the Film ID number in the first box, then click the 'DELETE RECORD' button.\nTo update a record, first enter the FilmID, then fill out any or all of the other fields to be updated and\nthen click the 'UPDATE RECORD' button." ,font=('Sans serif',12), justify="left")
def updatetopmessage():
    label5.config(text="")
label5 = Label(root, text=status, fg="green", font="Arial 11 bold", bd=2, relief="ridge", padx=10)
label5.after(4000,updatetopmessage)
label6= Label(root, text="                                           ")
label7 = Label(root, text="                                 ")
msg2="Not an integer value. \nPlease try again."
msg3="Value must be a four digit integer."

def add():
    msg="One or more fields is empty. \nPlease check and fill in all values"
    #check if a field is empty. If so, popup
    #a message to notify user
    print(filmTitle.get(),relYear.get(),comborating.get(), duration.get(), combo3.get())
    if filmTitle.get() !="" and relYear.get()   !="" and comborating.get() !="" and duration.get() !="" and combo3.get() !="":

        print(f"The following record has been added: Film Title:", filmTitle.get(), "Year of Release:",relYear.get(), "Rating:",comborating.get(),"Duration:",duration.get(), "Genre:",combo3.get())

        dbCursor.execute("insert into   tblfilms values (null, %s, %s, %s,    %s, %s)" , (filmTitle.get(), relYear.get(),   comborating.get(), duration.get(), combo3.get()))

        dbCon.commit()#append the record
        #now get rid of all the text in the text fields
        filmid.delete(0,"end")
        filmTitle.delete(0,"end")
        relYear.delete(0,"end")
        #rating.delete(0,"end")
        duration.delete(0,"end")

        def updatetopmessage():
            label5.config(text="")
        label5 = Label(root, text="Record Added", fg="green", font="Arial 11 bold", bd=2, relief="ridge", padx=10)
        label5.grid(row=1, column=1)
        label5.after(4000,updatetopmessage)
        
    else:
        messagebox.showinfo('message', msg)
        return

  

def delete():
    try:
        if (filmid.get() !=""):

            #select the unique record from the filmid table
            dbCursor.execute(f"Select * from tblfilms where filmId = {filmid.get()}")
        else:
            messagebox.showinfo('message', "ID field is empty.")
            return


        row = dbCursor.fetchone()
        #return the specific record to check it exists
        if row == None:
            print(f"No record with that id exists")
        else:
            dbCursor.execute(f"delete from tblfilms where filmid = {filmid.get()}")
            dbCon.commit()
            #clear the text from the text fields
            filmid.delete(0,"end")
            filmTitle.delete(0, "end")
            relYear.delete(0, "end")
            #rating.delete(0, "end")
            duration.delete(0, "end")
            
            text=Text(root, width=70, height=6)
            text.grid(sticky="W",row=15, column=1)
            text.delete("1.0","end")



            print(f"Record {filmid.get()} has been deleted")
           
        def updatetopmessage():
            label5.config(text="", bg="lightgrey")
        label5 = Label(root, text="Record Deleted", fg="red", bg="yellow", font=("Arial 11 bold"), bd=2, relief="ridge", padx=10)
        label5.grid(row=1, column=1)
        label5.after(4000,updatetopmessage)
    except sql.errors.Error as e:
        print(f"Database error : {e}")
    

def update():

    try:
        try:
            int(filmid.get())
            #check that filmid is an integer
        except ValueError:
            messagebox.showinfo('message', msg2)
            return

        # updating the tblfilms table
        # Updating each field individually
        # to screen blank fields
        if(filmTitle.get() !=""):

            dbCursor.execute(f"Update tblfilms set title = '{filmTitle.get()}' where filmid = {filmid.get()} ")
            dbCon.commit()
                                              
        if(relYear.get() !=""):

            dbCursor.execute(f"Update tblfilms set yearReleased = '{relYear.get()}' where filmid = {filmid.get()} ")
            dbCon.commit()

        if(comborating.get() !=""):

            dbCursor.execute(f"Update tblfilms set rating = '{comborating.get()}' where filmid = {filmid.get()} ")
            dbCon.commit()
        
        if(duration.get() !=""):

            dbCursor.execute(f"Update tblfilms set duration = '{duration.get()}' where filmid = {filmid.get()} ")
            dbCon.commit()
        
        if(filmTitle.get() !=""):

            dbCursor.execute(f"Update tblfilms set genre = '{combo3.get()}' where filmid = {filmid.get()} ")
            dbCon.commit()
        
        print(f"Record {filmid.get()} updated")
        displayone() #update the output in the Text box
        
        def updatetopmessage():
            label5.config(text="")
        label5 = Label(root, text="Record Updated", fg="green", font="Arial 11 bold", bd=2, relief="ridge", padx=10)
        label5.grid(row=1, column=1)
        label5.after(4000,updatetopmessage)
    except sql.errors.Error as e:
        print(f"Failed : {e}")
        

def displayall():
   dbCursor.execute("SELECT * FROM tblfilms")
   records=dbCursor.fetchall()
   print(records)
   print_records=''
   label10=Label(root, text=" #ID       Film                Release Yr   Rating  Running Time     Genre" )
   label10.grid( sticky=W,row=14, column=1)
  
   for r in records:
        print_records+= str(r)+"\n"

   #querylabel=Label(root, text=print_records, width=100, bg="#fffec8")
   #querylabel.grid(row=15, column=0)
   text=Text(root, width=70, height=6)
   
   #text.configure(yscrollcommand=v.set)
   text.insert(INSERT, print_records)
   text.grid(sticky="W",row=15, column=1)
   scrollbar=ttk.Scrollbar(root,orient='vertical',command=text.yview)
   scrollbar.grid(row=15, column=2, sticky=NS)
   text['yscrollcommand']= scrollbar.set
  

def displayone(): #find record by ID
    #reset all of the text fields
    #unless the id field is empty
    a=filmid.get()
    print(a)
    if a!="":
        filmTitle.delete(0, "end")
        relYear.delete(0, "end")
        
        duration.delete(0, "end")
        genre.delete(0,"end")
        #select the record which has the filmid     equal to what the user input
        dbCursor.execute(f"SELECT * FROM tblfilms   where filmid = {filmid.get()}")
        records=dbCursor.fetchall()
        print(records)
        if(records==""):
            return
        print(records)
        print_records=''
        label10=Label(root, text=" #ID       Film                Release Yr   Rating  Running Time     Genre" )
        label10.grid( sticky=W,row=14, column=1)
    else:
        print("ID IS EMPTY!")
        return

    for r in records:
        print_records+= str(r)+"\n"
        #filmTitle.text= {title}
    text=Text(root, width=70, height=6)
    if(print_records==""):
        messagebox.showinfo('message', "No record with that ID")

        return
    #display the record in the Text box
    text.insert(INSERT, print_records)
    text.grid(sticky="W",row=15, column=1)
    #splitting the record into a list of string values separated by commas
    splitrecords=print_records.split(", ")
    #now select the second value (Film title
    #removequotes variable is taking the string and stripping off the quotes
    removequotes=splitrecords[1]
    #now remove the quotes on each end
    removequotes=removequotes[1:-1]
    #putting the correct value into the corresponding text field for Film Title
    filmTitle.insert(INSERT, removequotes)
    
    #Release Year does not have any quotes
    relYear.insert(INSERT, splitrecords[2])

    removequotes=splitrecords[3]
    removequotes=removequotes[1:-1]
    #not needed - using a combobox instead
    comborating.set(removequotes)

    #Film duration does not have any quotes
    duration.insert(INSERT, splitrecords[4])
    #remove quotes from genre
    removequotes=splitrecords[5]
    removequotes=removequotes[1:-3]
    combo3.set(removequotes)
    # NB. With a combobox we use 'set' to
    # set its value, rather than insert

def searchgenre(): #search by genre
    #reset all of the text fields
    
    filmTitle.delete(0, "end")
    relYear.delete(0, "end")
    #rating.delete(0, "end")
    duration.delete(0, "end")
    genre.delete(0,"end")
    #put single quotes around the user input
    ft=filmsearch.get()
    print(ft)
    comboquotes="'"+combo.get()+"'"

    #select the records which have the genre equal to what the user chose
    dbCursor.execute(f"SELECT * FROM tblfilms where genre = {comboquotes}")
    records=dbCursor.fetchall()
  
    print(records)
    print_records=''
    label10=Label(root, text=" #ID       Film                Release Yr   Rating  Running Time     Genre" )
    label10.grid( sticky=W,row=14, column=1)
    for r in records:
        print_records+= str(r)+"\n"
        #filmTitle.text= {title}
    text=Text(root, width=70, height=6)
   
    #display the record in the Text box
    text.insert(INSERT, print_records)
    text.grid(sticky="W",row=15, column=1)
    #text.configure(yscrollcommand=v.set)
    
    scrollbar=ttk.Scrollbar(root,orient='vertical',command=text.yview,)
    scrollbar.grid(row=15,column=2,sticky='NS')
    text['yscrollcommand']= scrollbar.set

def searchyear(): #search by genre
    #reset all of the text fields
    if year.get() !="" and int(year.get()) and len(year.get())==4:

        filmTitle.delete(0, "end")
        relYear.delete(0, "end")
        #rating.delete(0, "end")
        duration.delete(0, "end")
        genre.delete(0,"end")
        #put single quotes around the user input
        ft=filmsearch.get()
        print(ft)
        

        #select the records which have the genre equal to what the user chose
        dbCursor.execute(f"SELECT * FROM tblfilms where yearReleased = {year.get()}")
        records=dbCursor.fetchall()
        print(filmsearch.get())
        print(records)
        print_records=''
        label10=Label(root, text=" #ID       Film            Release Yr   Rating  Running Time  Genre" )
        label10.grid( sticky=W,row=14, column=1)
        for r in records:
            print_records+= str(r)+"\n"
            #filmTitle.text= {title}
        text=Text(root, width=70, height=6)
   
        #display the record in the Text box
        text.insert(INSERT, print_records)
        text.grid(sticky="W",row=15, column=1)
        #text.configure(yscrollcommand=v.set)
    
        scrollbar=ttk.Scrollbar(root,orient='vertical',command=text.yview,)
        scrollbar.grid(row=15,column=2,sticky='NS')
        text['yscrollcommand']= scrollbar.set
    else:
        messagebox.showinfo('message', msg3)



def searchrating(): #search by genre
    #reset all of the text fields
    
    filmTitle.delete(0, "end")
    relYear.delete(0, "end")
    #rating.delete(0, "end")
    duration.delete(0, "end")
    genre.delete(0,"end")
    #put single quotes around the user input
    ft=filmsearch.get()
    print(ft)
    combo2quotes="'"+combo2.get()+"'"

    #select the records which have the genre equal to what the user chose
    dbCursor.execute(f"SELECT * FROM tblfilms where rating = {combo2quotes}")
    records=dbCursor.fetchall()
  
    print(records)
    print_records=''
    label10=Label(root, text=" #ID       Film                Release Yr   Rating  Running Time     Genre" )
    label10.grid( sticky=W,row=14, column=1)
    for r in records:
        print_records+= str(r)+"\n"
        #filmTitle.text= {title}
    text=Text(root, width=70, height=6)
   
    #display the record in the Text box
    text.insert(INSERT, print_records)
    text.grid(sticky="W",row=15, column=1)
    #text.configure(yscrollcommand=v.set)
    
    scrollbar=ttk.Scrollbar(root,orient='vertical',command=text.yview,)
    scrollbar.grid(row=15,column=2,sticky='NS')
    text['yscrollcommand']= scrollbar.set


def clear():
    filmid.delete(0,"end")
    filmTitle.delete(0, "end")
    relYear.delete(0, "end")
    
    duration.delete(0, "end")
    
    text=Text(root, width=70, height=6)
    text.grid(sticky="W",row=15, column=1)
    text.delete("1.0","end")
    year.delete(0, "end")

    


#######CREATE THE BUTTONS##############
#button6=Button(root, text=" SEARCH FOR A FILM",  command=search)
filmsearch=Entry(root, width=12, bg="lightyellow", font=("Arial", 12))
button0=Button(root, text=" ADD RECORD", command=add, padx=26) 
buttonfind=Button(root, text=" *FIND RECORD BY ID*", command=displayone) 
button1=Button(root, text=" DISPLAY A RECORD", command=displayone)
button2=Button(root, text=" DELETE RECORD", command=delete, padx=18)
button3=Button(root, text=" UPDATE RECORD", command=update, padx=16)
button4=Button(root, text=" DISPLAY ALL RECORDS", command=displayall)
button8=Button(root, text="CLEAR ALL FIELDS", command=clear, padx=17)

button9=Button(root, text="SEARCH", command=searchgenre)
button10=Button(root, text="SEARCH", command=searchyear)
button11=Button(root, text="SEARCH", command=searchrating)




#button6.place(x=740, y=82)
#filmsearch.place(x=625, y=88)
buttonfind.place(x=220, y=82)
button0.grid(sticky=N, row=6, column=1)
#button1.grid(sticky=N, row=6, column=1)
button2.grid(sticky=N, row=7, column=1)
button3.grid(sticky=N, row=8, column=1)
button4.grid(row=9, column=1)
button8.grid(row=4, column=1)
button9.place(x=844, y=116)
button10.place(x=844, y=206)
button11.place(x=844, y=296)

#label 4 is just to add some vertical space
label4 = Label(root, text="                                     ")
label1.grid(sticky=W, row=0, column=1)


label3.grid(sticky=N, row=22, column=0, columnspan=6)
label4.grid(row=3, column=0)
label5.grid(row=1, column=1)
label6.grid(row=11, column=0)
label7.grid(row=26, column=1)

filmid=Entry(root,width=3, font=('Arial',12), bg="lightyellow")
filmid.grid(sticky=W, row=4, column=1)
filmidLabel=Label(root, text="Film ID", font=('Arial',12) )
filmidLabel.grid(sticky=E,row=4, column=0)

filmTitle=Entry(root,width=20, font=('Arial',12),bg="lightyellow" )
filmTitle.grid(sticky=W, row=5, column=1)
filmTitleLabel=Label(root, text="Film Title",font=('Arial',12))
filmTitleLabel.grid(sticky=E, row=5, column=0)

relYear=Entry(root,width=4,  font=('Arial',12),bg="lightyellow")
relYear.grid(sticky=W, row=6, column=1)
relYearLabel=Label(root, text="Year Released",font=('Arial',12))
relYearLabel.grid(sticky=E, row=6, column=0)

#routine to automatically capitalise the 
#rating text entered by the user
var = StringVar()

#The following routine ensures that the text
#entered into the rating field is converted
#to capitals (Not needed - using combobox instead#)
# def caps(event):
#     v.set(v.get().upper())

# v = StringVar()
# rating = Entry(root, width=3, textvariable=v, bg="lightyellow", font=("Arial", 12)) 

# rating.bind("<KeyRelease>", caps)
#End of capital conversion routine

#display the rating text field
#rating.grid(sticky=W, row=7, column=1)

ratingLabel=Label(root, text="Rating",font=('Arial',12))
#display the rating label
ratingLabel.grid(sticky=E, row=7, column=0)


duration=Entry(root,width=3, font=('Arial',12),bg="lightyellow")
duration.grid(sticky=W, row=8, column=1)
durationLabel=Label(root, text="Duration(mins)",font=('Arial',12))
durationLabel.grid(sticky=E, row=8, column=0)

genre=Entry(root,width=14, font=('Arial',12),bg="lightyellow")
#genre.grid(sticky=W, row=9, column=1)
genreLabel=Label(root, text="Genre",font=('Arial',12))
genreLabel.grid(sticky=E, row=9, column=0)



root.mainloop() # KEEP THIS COMMAND AT THE BOTTOM