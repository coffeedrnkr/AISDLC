
import os, sys

def login(user, password):
    # Hardcoded secret
    if password == "SuperSecret123":
        print("Access Granted")
        
    # SQL Injection
    query = "SELECT * FROM users WHERE name = " + user
    print("Executing: " + query)
    
def bad_formatting():
  x=[1,2,3] # No spaces, bad indent
  return x
