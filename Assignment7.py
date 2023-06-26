def fileHandle(file):
    print("File Handling function...")

    f = open(file,"a+")
    print("File opened successfully...")
    try:
        rollno=input("Enter your rollno :")
        name=input("Enter your name :")
        dept=input("Enter your department :")
        f.writelines(rollno)
        f.writelines(name)
        f.writelines(dept)
        print("Writed successfully in the file")
    except IOError:
        print("IO Error Exception Handled Here...")
    finally:
        print("No exception present now...")


    f.seek(0)               #gets the cursor at first index of file
    infile=f.readlines()
    print("Data present in File")
    print(infile)           #displays content present inside the file
    print("Readed successfully...")

    f.close()
    print("File closed successfully")

#calling function by passing the file_name as parameter
#on which operations are performed
fileHandle("abc.txt")