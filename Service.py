import re


patt_email=r'[a-zA-Z|0-9|.|%|_|+|-]+\@{1}[a-zA-Z|0-9|.|-]+\.[a-zA-Z][a-zA-Z]+'
patt_num=r'^0\d{10}'


def Add_s(df,name:str,number,email):
    try:
        if re.search(patt_num,number) and re.search(patt_email,email):

            flag=True
            for ind in df.index:
                if df['name'][ind].lower()==name.lower():
                    print("\nContant with this Name is Exist")
                    flag=False
                    break
                elif df['number'][ind]==number:
                    print("\nContact with this Number is Exist")
                    flag=False
                    break
                elif df['Email'][ind]==email:
                    print("\nContact with this Email is Exist")
                    flag=False
                    break
            if flag:
                print("\n-----------------------\n")
                print('Contact Added!')
                return df._append({'name':name,'number':number,'Email':email},ignore_index=True)
            else:
                return df
        else:
            print("\n-----------------------\n")
            print("Your input is Now Valid Please Enter number and Email Correctly")
    except:
        print('error log Add Service')


def Update_s(df,name):
    for ind in df.index:
        if df['name'][ind]==name:
            new_name=input("Enter New Name or Enter 0 to keep before Name: ")
            if new_name!='0':
                df['name'][ind]=new_name
                print("Name Updated")
            
            new_number=input("Enter New number or Enter 0 to keep before number: ")
            if new_number!='0' and re.search(patt_num,new_number):
                df['number'][ind]=new_number
                print("Number Updated")

            new_email=input("Enter New email or Enter 0 to keep before email: ")
            if new_email!='0' and re.search(patt_email,new_email):
                df['Email'][ind]=new_email
                print("Email Updated")
            
            return df
    print("\n-----------------------\n")    
    print(f"Contact with {name} is NOT Exist")
    return df

    


def Remove_s(df,name):
    try:
        for ind in df.index:
            if df['name'][ind].lower()==name.lower():
                print('Contact Removed!')
                return df.drop(ind)
            else:
                print('Contact with this Name is NOT exist')
                return df
        pass

    except:
        pass

def Show_s(df):
    pass

def Sort_s(df):
    pass