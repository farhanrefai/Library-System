import mysql.connector

#open database connection with a dictionery



conDict = {'host':'localhost','database':'db_library_python','user':'root','password':''}



db = mysql.connector.connect(**conDict)



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Using Function as addbook() to add a book details to database 
def addbook():
# Initialize variables----------------------------------------------------------------------------------------------------------
    BBook_No = 0
    BBook_title = ""
    ssubject_code = 0
    ssubject = ""
    aauthor = ""
    ppublisher = ""
    pprice = 0
    llocation = ""
# User input Book_No,Book_Title,Subject_code,Subject,Author,Publisher,Price,Location
    BBook_No = int(input("Enter Book a Number:"))
    BBook_title = str(input("Enter Book Name:"))
    ssubject_code = int(input("Enter a Subject Code:"))
    ssubject = str(input("Enter the Subject:"))
    aauthor = str(input("Enter the Author of the Book:"))
    ppublisher = str(input("Enter the Publisher of the Book:"))
    pprice = input("Enter the Price of the Book:")
    llocation = str(input("Enter the Location:"))
# execute SQL query using execute() method.
    mySQLText = "INSERT INTO addbook (Book_No, Book_Title, Subject_Code, Subject, Author, Publisher, Price, Location) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    myValues = (BBook_No,BBook_title,ssubject_code,ssubject,aauthor,ppublisher,pprice,llocation)
#prepare a cursor object using cursor() method    
    cursor = db.cursor()
    cursor.execute(mySQLText,myValues)
# commit the change
    db.commit()
# Print the output as "Book Successfully Added"
    print(cursor.rowcount, "Book Successfully Added")
    menusys()



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Using Function as addchapter() to add chapters details to database
def addchapter():
# Initialize variables------------------------------------------------------------------------------------------------------------
    BBook_No = 0
    cchapter_No = 0
    cchapter_title = ""
    sstr_page_No = 0
    eend_page_No = 0
# User input Book_No,chapter_No,chapter_title,sstr_page_No,eend_page_No    
    BBook_No = int(input("Enter a Book Number:"))
    cchapter_No = int(input("Enter a Chapter Number:"))
    cchapter_title = str(input("Enter a Chapter Title:"))
    sstr_page_No = int(input("Enter a Starting Page Number :"))
    eend_page_No = int(input("Enter a Ending Page Number:"))
# execute SQL query using execute() method.
    mySQLText2 = "INSERT INTO Chapters (Book_No, chapter_No, chapter_title, Str_Page_No, End_Page_No) VALUES (%s,%s,%s,%s,%s)"
    myValues2 = (BBook_No,cchapter_No,cchapter_title,sstr_page_No,eend_page_No)
    cursor = db.cursor()
    cursor.execute(mySQLText2,myValues2)
# commit the change
    db.commit()
# Print the output as "chapter Successfully Added"
    print(cursor.rowcount,"chapter successfully added")
    menusys()



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Using Function as addsubject() to add subjects details to database 
def addsubject():
# Initialize variables------------------------------------------------------------------------------------------------------------
    ssubject_code = 0
    ssubject = ""
# User input Subject_code,Subject
    ssubject = str(input("Enter the Subject:"))
    ssubject_code = int(input("Enter Subject Code:"))
# execute SQL query using execute() method.
    mySQLText2 = "INSERT INTO subjects (Subjects, Subject_Code) VALUES (%s,%s)"
    myValues2 = (ssubject,ssubject_code)
#prepare a cursor object using cursor() method 
    cursor = db.cursor()
    cursor.execute(mySQLText2,myValues2)
# commit the change
    db.commit()
# Print the output as "Subject Successfully Added"
    print(cursor.rowcount,"Subject successfully added")
    menusys() 



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Using Function as dispbookdetails() to display book details from database 
def dispbookdetails():
#prepare a cursor object using cursor() method
    cursor = db.cursor()
#execute SQL query using execute() method.    
    cursor.execute("SELECT Book_No, Book_Title, Subject_Code, Subject, Author, Publisher, Price, Location FROM addbook")
#Fetch results using fetchall() method.
    data = cursor.fetchall()
# using for a loop to display the book details 
    for item in data:
        print("Display Available Books :")
        print(item)
    menusys()



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Using Function as dispchapterdetails() to display chapter details from database 
def dispchapterdetails():
#prepare a cursor object using cursor() method
    cursor = db.cursor()
#execute SQL query using execute() method. 
    cursor.execute("SELECT * FROM chapters")
#Fetch results using fetchall() method.
    data1 = cursor.fetchall()
# using for a loop to display the chapter details 
    for item in data1:
        print("Display Available Chapters:")
        print(item)
    menusys()



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Using Function as dispsubjectsdetails() to display subject details from database
def dispsubjectsdetails():
#prepare a cursor object using cursor() method
    cursor = db.cursor()
#execute SQL query using execute() method.
    cursor.execute("SELECT * FROM subjects")
#Fetch results using fetchall() method.
    data2 = cursor.fetchall()
# using for a loop to display the chapter details 
    for subjects in data2:
        print("Display Available Subjects")
        print(subjects)
    menusys()



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Using Function as searchabook() to search a particular book details from the database 
def searchabook():
#prepare a cursor object using cursor() method 
    cursor = db.cursor()
# User input Book_No to search a book details
    BBook_No = input("Enter a Book Number:")
# execute SQL query using execute() method.
    cursor.execute("SELECT Book_Title, Subject_Code, Subject, Author, Publisher, Price, Location  FROM addbook WHERE Book_No = " + BBook_No + "" )
#Fetch results using fetchall() method.
    data = cursor.fetchall()
# using for a loop to display the search Book details 
    for item in data:
        print("Books Available by search:")
        print(item)
        menusys()



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Using Function as updatebook() to update a book details to database
def updatebook():
# Initialize variables-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    BBook_No = 0
    BBook_title = ""
    ssubject_code = 0
    ssubject = ""
    aauthor = ""
    ppublisher = ""
    pprice = 0
    llocation = ""
#prepare a cursor object using cursor() method
    cursor = db.cursor()
#User input to update Book_No,Book_Title,Subject_code,Subject,Author,Publisher,Price,Location 
    BBook_No = input("Enter a Book Number:")
    BBook_title = str(input("Enter a Book Title:"))
    ssubject_code = input("Enter a Subject Code:")
    ssubject = str(input("Enter a Subject:"))
    aauthor = str(input("Enter a Author Name:"))
    ppublisher = str(input("Enter a Publisher Name:"))
    pprice = input("Enter a Price:")
    llocation = str(input("Enter a Location:"))
#execute SQL query using execute() method.
    updTxt = "UPDATE addbook SET Book_Title = '" + BBook_title + "' ,Subject_Code = '" + ssubject_code + "' ,Subject = '" + ssubject + "' ,Author = '" + aauthor + "' ,Publisher = '" + ppublisher + "' ,Price = '" + pprice + "' ,Location = '" + llocation + "' WHERE Book_No = '" + BBook_No + "'"
    cursor.execute(updTxt)
#commit the change
    db.commit()
#print the output as "Book details Record Updated Successfully"
    print(cursor.rowcount, "Book details Record Updated Successfully")
    menusys()



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Using Function as updatesubject() to update a subject details to database
def updatesubject():
#Initialize variables-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ssubject_code = 0
    ssubject = ""
#prepare a cursor object using cursor() method
    cursor = db.cursor()
#User input to update Subject_code,Subject
    ssubject_code = input("Enter a Subject Code:")
    ssubject = input("Enter a Subject:")
#execute SQL query using execute() method.
    updTxt = "UPDATE subjects SET Subject = '" + ssubject + "' WHERE Subject_Code = " + ssubject_code + ""
    cursor.execute(updTxt)
#commit the change
    db.commit()
# print the output as "Subject details Record updated Successfully"
    print(cursor.rowcount, "Subject details Record Updated Successfully")
    menusys()



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Using Function as deleteabook() to delete a Book details from database
def deleteabook():
#prepare a cursor object using cursor() method
    cursor = db.cursor()
#User input Book_No to delete a Book details from database
    BBook_No = input("Enter a Number to Delete a Record:")
#execute SQL query using execute() method.
    cursor.execute("DELETE FROM addbook WHERE Book_No = " + BBook_No + "")
#commit the change
    db.commit()
#print the output as "Book details Record Deleted Successfully"
    print(cursor.rowcount, "Book details Record Deleted Successfully")
    menusys()



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Using Function as deleteachapter() to delete a chapter details from database
def deleteachapter():
#prepare a cursor object using cursor() method
    cursor = db.cursor()
#User input Book_No to delete a chapter details from database
    BBook_No = input("Enter a Number to Delete a Record:")
#execute SQL query using execute() method.
    cursor.execute("DELETE FROM chapters WHERE Book_No = " + BBook_No + "")
#commit the change
    db.commit()
#print the output as "Chapter details Record Deleted Successfully"
    print(cursor.rowcount, "Chapter details Record Deleted Successfully")
    menusys()



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Using Function as deleteasubject() to delete a subject details from database
def deleteasubject():
#prepare a cursor object using cursor() method
    cursor = db.cursor()
#User input subject_No to delete a chapter details from database
    ssubject_code = input("Enter a Number to Delete a Record:")
#execute SQL query using execute() method.
    cursor.execute("DELETE FROM subjects WHERE Subject_Code = " + ssubject_code + "")
#commit the change
    db.commit()
#print the output as "Subject details Record Deleted Successfully"
    print(cursor.rowcount, "Subject details Record Deleted Successfully")
    menusys()



#Using Function as menusys() to make menu system to run the above Library program
def menusys():
    print("""...............Library Program...........
    1.Add a Book
    2.Add a Chapter
    3.Add a Subject
    4.Display Book details
    5.Display Chapter details
    6.Display Subject details
    7.Search a Book using Book_No
    8.Update a Book details
    9.Update a Subject
    10.Delete a Book deatails
    11.Delete a Chapter details
    12.Delete a Subject details
    13.Exit
    """)
    choice = input("Enter a Number from the above Menu :")
    print("............")
    if choice == '1':
        addbook()
    elif choice == '2':
        addchapter()
    elif choice == '3':
        addsubject()
    elif choice == '4':
        dispbookdetails()
    elif choice == '5':
        dispchapterdetails()
    elif choice == '6':
        dispsubjectsdetails()
    elif choice == '7':
        searchabook()
    elif choice == '8':
        updatebook()
    elif choice == '9':
        updatesubject()
    elif choice == '10':
        deleteabook()
    elif choice == '11':
        deleteachapter()
    elif choice == '12':
        deleteasubject()
    else:
        choice == '13'
        print("Exit")

menusys()
        











