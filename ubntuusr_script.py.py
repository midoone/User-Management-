#!/usr/bin/env python3

# the ubuntu script i change the wheel group to sudo to add the users to the sodoers group, and the command adduser  to useradd 
#import the module os to interact with the file system.
import os 

# function to add the first 27 users to the developers group.
def Add_developers(file):
    # open the given file.
    with open(file,'r') as infile:
        #read the file.
        data = infile.readlines()[0:27]
        #for loop to read every line in file.
        for i in data:
            # split lines in to words
            names = i.split()
            # if the lines is compose of two words get the last name and first initial of the first name.
            if ((len(names)) ==2 ):
                First_Int= names[0][0]
                Lastname= names[1]
                uid = First_Int+Lastname
            # if the lines are compose of 3 words or more get the first initial and the midel initial and the last name as id.    
            if ((len(names)) >=3 ):
                Midel_Int= names[1][0]
                First_Int= names[0][0]
                Lastname= names[-1]
                uid = First_Int+Midel_Int+Lastname
            # execute the command adduser to add the users to the developers group     
            os.system("sudo useradd -s /usr/bin/csh -G developers %s" %uid)
    print("the 27 users has been added to developers")        
    infile.close()

# function to add users to admin group the same way as the first function     
def Add_admin(file):
    with open(file,'r') as infile:
        data = infile.readlines()[20:54]
        for i in data:
            names = i.split()
            if ((len(names)) ==2 ):
                Firstname= names[0]
                First_Int= names[0][0]
                Lastname= names[1]
                uid = First_Int+Lastname
            if ((len(names)) >=3 ):
                Midel_Int= names[1][0]
                First_Int= names[0][0]
                Lastname= names[-1]
                uid = First_Int+Midel_Int+Lastname
            os.system("sudo useradd -G admin %s" %uid)
            #here we add the users the while group
            os.system("sudo usermod -aG sudo %s" %uid)
    print(" the 27 users has been added to admin\n added to sudo with full permission")         
    infile.close()

# function to add users to staff group the same way as the first function    
def Add_staff(file):
    with open(file,'r') as infile:
        data = infile.readlines()[55:81]
        for i in data:
            names = i.split()
            if ((len(names)) ==2 ):
                Firstname= names[0]
                First_Int= names[0][0]
                Lastname= names[1]
                uid = First_Int+Lastname
            if ((len(names)) >=3 ):
                Midel_Int= names[1][0]
                First_Int= names[0][0]
                Lastname= names[-1]
                uid = First_Int+Midel_Int+Lastname
            os.system("sudo useradd -G staff %s" %uid)
    print(" the 27 users has been added to staff")
    infile.close()  

# function to add users to the temp group the same way as the fisrt function
def Add_temp(file):
    with open(file,'r') as infile:
        data = infile.readlines()[82:108]
        for i in data:
            names = i.split()
            if ((len(names)) ==2 ):
                Firstname= names[0]
                First_Int= names[0][0]
                Lastname= names[1]
                uid = First_Int+Lastname
            if ((len(names)) >=3 ):
                Midel_Int= names[1][0]
                First_Int= names[0][0]
                Lastname= names[-1]
                uid = First_Int+Midel_Int+Lastname
            os.system("sudo useradd -G temp %s" %uid)
    print(" the 27 users has been added to temp") 
    infile.close()

# the main function where we ask the user for the file and we execute the four function.    
def main():
    file= input("Enter a file name:")
    Add_admin(file)
    Add_staff(file)
    Add_temp(file)
    Add_developers(file)
main()
