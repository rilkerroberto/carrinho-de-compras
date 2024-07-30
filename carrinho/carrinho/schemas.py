from pydantic import Basemodel , Emailstr

class user (Basemodel):
    name = str 
    email = str 

class product (Basemodel):
    name = str 
    category = str
    value = float 

 