from account import *


def main():
    choice = -1
    while choice != 0:
        print("MENU:")
        print("0. Quit")
        print("1. Create Account")
        print("2. Login\n")

        choice = int(input("Enter menu number: "))

        if choice == 1:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            taken = find(username)
            if taken == None:
                create(username, password)
                print("Account Created")
            else:
                print("Username Taken")


        elif choice == 2:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            correct = login(username, password)


            if correct == None:
                print("\nUsername or Password incorrect.")


            else:
                print(login(username, password))
                in_choice = -1

                while  in_choice != 0:

                    print("ACCOUNT MENU:")
                    print("0. Log Out")
                    print("1. Change Username")
                    print("2. Change Password")
                    print("3. Delete account\n")
                    in_choice = int(input("Enter menu number: "))

                    if in_choice == 1:
                        new_user = input("Enter new username: ")
                        update_username(username, new_user)
                        print(f"Username is now '{find(new_user)['username']}'")
                        username = new_user
                        
                    elif in_choice == 2:
                        new_pass = input("Enter new password: ")
                        update_password(username, password, new_pass)
                        print(f"Password is now '{find(username)['password']}'")
                        password = new_pass
                        
                    elif in_choice == 3:
                        confirm = input("Are you sure you want to delete your account (y/n): ")
                        if confirm.upper() == 'Y':
                            delete(username, password)
                            print("Account Deleted")
                            in_choice = 0

    print("Thank you!")

if __name__ == "__main__":
    main()