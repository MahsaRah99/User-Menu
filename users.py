from uuid import uuid4
import hashlib

"""
    contains a class called User which has 
    different methods for creating a user sign-up 
    system.
"""

class User:
    
    users = {}
    
    def __init__(self, username:str, password:str, phone_number = None):
        self.username = username
        self.__password = password
        self.phone_number = phone_number
        self.id = str(uuid4())[:8]
     
      
    @classmethod  
    def create_user(cls, user_name:str, pass_word: str, phone_num:str)-> int|None:
        """
          creates a User instance using username, phone number 
           and encoded form of password of a user   
        """
        if user_name in cls.users:
            return 1  #print("user name already exists!")
        if cls.validate_password(pass_word) == False: 
            return 2  #print("password is too short")
        if cls.validate_username(user_name) == False: 
            return 3  #print("username cant be empty")
        encoded_pass = cls.pass_builder(pass_word)   
        new_user = cls(user_name, encoded_pass, phone_num)
        cls.users[new_user.username] = new_user   
    
        
     
    @staticmethod    
    def validate_password(pass_word:str)->bool:
        """
            checks if the given password's 
            length is greater than four characters
            and return True otherwise False
        """
        if len(pass_word) >= 4:
            return True
        return False
    
    @staticmethod    
    def validate_username(user_name:str)-> bool:
        """
            checks if the given password's 
            length is greater than four characters
            and return True otherwise False
        """
        if len(user_name) > 0:
            return True
        return False
    
        
            
    def log_in(self, user_name:str, pass_word:str)-> int:
        """
        checks if a user exists in users list and if they 
        do, checks their password. otherwise returns numbers
        to print messages in the main function.
        """
        if user_name not in self.users:
            return 1 #print("user not found") 
        user = self.users[user_name]
        if user.__password != self.pass_builder(pass_word):
            return 2  #print("wrong password") 
           
     
     
    def edit_info(self,old_user:str, new_user_name:str, new_phone_num:str)-> bool|None:
        """
        replaces users old username and phone numbers
        with new ones.
        """
        if self.validate_username(new_user_name) == False:
            return 0
        
        user = self.users[old_user]
        user.username = new_user_name
        user.phone_number = new_phone_num
        self.users.pop(old_user)
        self.users[new_user_name] = user
        
        
    def change_password(self,user_name:str, old_pass:str, new_pass:str)-> int|None:
        """
        changes user's old password with new one.
        """
        user = self.users[user_name]
        if user.__password != self.pass_builder(old_pass):
            return 1 #print("wrong password")
        if self.validate_password(new_pass) == False:
            return 2 #print("too short password")    
        user.__password = self.pass_builder(new_pass)
        self.users[user_name] = user
      
        
    @staticmethod
    def pass_builder(pass_word:str)-> str:
        """
        gets a password and encodes it using salt and hashlib.
        """        
        salt = "S@lt#"
        # Adding salt at the last of the password
        dB_password = pass_word + salt
        # Encoding the password
        hashed = hashlib.md5(dB_password.encode())
        
        return hashed.hexdigest()


            
    def __str__(self):
        return f"ID: {self.users[self.username].id} * Username: {self.users[self.username].username} * Phone-number: {self.users[self.username].phone_number}\n"
        
        
