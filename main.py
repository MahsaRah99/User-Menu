from users import User
from getpass import getpass

def check_pass(entered,confirmed):
    """
    gets two passwords and returns True if 
    they match and False otherwise.
    
    """
    if entered == confirmed:
        return True
    return False

def main():
    """
    creates User Menu and Login Menu,
    users can create account or login in User Menu,
    users can edit their username, phone number
    or change their password in Login Menu
    
    """
            
    while True:
        print("-----------------------------\n\tUSER MENU\n-----------------------------")
        print("1) SIGN-IN\n2) LOG-IN\n0) EXIT")
        command = int(input())
        
        match command:
            case 0:
                break
            
            
            case 1:
                print("WELCOME!")
                user_name = input("Enter Your Username:\n")
                pass_word = getpass("Enter Your Password:\n")
                phone_num = input("Enter Your Phone Number(optional):\n")
                
                result = User.create_user(user_name,pass_word,phone_num)
                
                if result == 1:
                    print("Username Already Exists!")
                elif result == 2:
                    print("Password Is Too Short!")
                else:
                    print("User Created Successfully!")
                
                    
            case 2:
                
                username = input("Username:\n")
                password = getpass("Password:\n")
                logged_user = User(username,password) 
                flag = logged_user.log_in(username, password)
                
                while True:
                    print("-----------------------------\n\tLOGIN MENU\n-----------------------------")
                    if flag == 1:
                        print("User Not Found")
                        break 
                    elif flag == 2:
                        print("Wrong Password")
                        break 
                    else:
                        print("1) REVIEW INFO\n2) EDIT INFO\n3) CHANGE PASSWORD\n4) BACK TO USER MENU")
                        x = int(input())
                        match x:
                            case 1:
                                
                                print(User.users[username]) 
                            
                            case 2:
                                new_user_name = input("Enter Your NEW Username:\n")
                                new_phone_num = input("Enter Your NEW Phone Number:\n")
                                logged_user.edit_info(username,new_user_name,new_phone_num)
                                
                                print("User Info Edited Successfuly!")
                                username = new_user_name
                                
                            case 3:
                                old_pass = getpass("Old Passsword:\n")
                                new_pass = getpass("New Passsword:\n")
                                conf_pass = getpass("Confirm Your Passsword:\n")
                                
                                if check_pass(new_pass,conf_pass):
                                    res = logged_user.change_password(username,old_pass,new_pass)
                                    if res == 1:
                                        print("Wrong Password")
                                    elif res == 2:
                                        print("Too Short Password")
                                    else:
                                        print("Password Changed!")
                                else:
                                    print("Passwords doesn't match!")
                            
                            case 4:
                                break
                
                    
if __name__ == "__main__":
    main()
        
