import pandas as pd
from Service import *


def Add():
    global Contact_data
    name=input("Enter Name of Contact: ")
    number=input("Enter Number of Contact: ")
    email=input("Enter Email of Contact: ")
    Contact_data=Add_s(Contact_data,name,number,email)
    print("\n-----------------------\n")

def Update():
    global Contact_data
    name=input("Enter Name of Contact: ")
    Contact_data=Update_s(Contact_data,name)
    print("\n-----------------------\n")        

def Remove():
    global Contact_data
    name=input("Enter Name of Contact: ")
    Contact_data=Remove_s(Contact_data,name)
    print("\n-----------------------\n")

def Show():
    print(Contact_data.to_string())
    print("\n-----------------------\n")

def Sort():
    print(Contact_data.sort_values(by='name').to_string())
    print("\n-----------------------\n")

def Save():
    Contact_data.to_csv('Contact.csv',index=False)
    print("Contacts Saved in File")
    print("\n-----------------------\n")

def Main():
    print("Wellcome to your contact:")
    print(" ")
    tasks=[Add,Update,Remove,Show,Sort,Save]

    while True:
        try:
            print("Main Menu")   
            task=int(input("1:Add 2:Update 3:Remove \n4:Show all 5:Sort by name and show \n6:Save Contact 7:Close App \nChoose what do you want to do: "))
            print("\n-----------------------\n")
            if task==7:
                break

            for i in range(len(tasks)):
                if i==task-1:
                    tasks[i]()
                    break 
        except:
            print("\n---Enter Valid Input---\n")


try:
    Contact_data=pd.read_csv('Contact.csv')

except:
    Contact_data = pd.DataFrame(columns=['name','number','Email'])
    
finally:
    Main()




    
    

