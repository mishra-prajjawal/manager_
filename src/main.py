#creating an employee management system
from source import *
#creating a menu driven program
"""
/*
 * Manage+ BY PRAJJAWAL MISHRA,
 * Copyright © 2022 Prajjawal Mishra
*/
    Permission to use, copy, modify, and/or distribute this software for any
    purpose with or without fee is hereby granted.
    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
    REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
    AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
    INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
    LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
    OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
    PERFORMANCE OF THIS SOFTWARE.
"""
def create_user():
    a = worker().create_user()
    if a == 0:
        print("User created successfully")
    else:
        print("<system-failure> User data not created")
def read_userdata():
    a = worker().read_user_alldata()
    for i in a: 
        for j in i.keys():
            print(j,":",i[j])
def read_user(userid):
    a = worker().read_user(userid)
    if a == None:
        print("<system-failure> User data not found")
    else:
        for i in a.keys():
            print(i,":",a[i])

def update_user(userid):
    a = worker().update_user(userid)
    if a == None:
        print("<system-failure> User data not found")
    else:
        print("User data updated successfully")
def delete_user(userid):
    a = worker().delete_user(userid)
    if a == None:
        print("<system-failure> User data not found")
    else:
        print("User data deleted successfully")
def search_user(userid):
    a = worker().search_user(userid)
    if a == None:
        print("<system-failure> User data not found")
    else:
        print(a["userid"],":",a["name"],"\nUser data found successfully")
def search_user_name(name):
    a = worker().search_user_name(name)
    if a == None:
        print("<system-failure> User data not found")
    else:
        for i in a:
            print(i["userid"],":",i["name"],"\nUser found")
def export_csv():
    a = worker().export_csv()
    if a == 0:
        print("Data exported successfully","Path: manager_/data.csv -> data.csv")
    else:
        print("<system-failure> Data not exported")
print("""
        1. Create a new user by entering the data
        2. Read all user data 
        3. Read a user data by id
        4. Update a user data by id
        5. Delete a user data by id 
        6. Search a user name by id if it exists
        7. Search a user data by name or part of the name if it exists
        8. Exit or Type "exit" to exit the program
        9. Export the data in a csv file
        10. Help or Type "help" to get the help menu
        """)
def main():
    while True:
        choice = int(input("system/manager+>>> "))
        if choice == 1:
            create_user()
        elif choice == 2:
            read_userdata()
        elif choice == 3:
            userid = int(input("system/manager+>>> USER ID to get data about employee : "))
            read_user(userid)
        elif choice == 4:
            userid = int(input("system/manager+>>> USER ID(Enter the user id to update) :"))
            update_user(userid)
        elif choice == 5:
            userid = int(input("system/manager+>>> Enter the user id to delete :"))
            delete_user(userid)
        elif choice == 6:
            userid = int(input("Enter the user id : "))
            search_user(userid)
        elif choice == 7:
            name = input("Enter the name : ")
            search_user_name(name)
        elif choice == 8 or (str(choice).strip()).lower() == "exit":
            print("Exiting the program")
            break
        elif choice == 9:
            export_csv()
        elif choice == 10 or (str(choice).strip()).lower() == "help":
            print("""
            1. Create a new user by entering the data
            2. Read all user data 
            3. Read a user data by id
            4. Update a user data by id
            5. Delete a user data by id
            6. Search a user name by id if it exists
            7. Search a user data by name or part of the name if it exists
            8. Exit or Type "exit" to exit the program
            9. Export the data in a csv file named "data.csv"
            10. Help or Type "help" to get the help menu
            """)

main()