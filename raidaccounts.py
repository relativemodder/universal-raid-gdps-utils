import requests
import random
endpoint = "http://aspirix.ru/sp/"
def createAcc(userName, password, email):
    pl = {
        'userName': userName,
        'userPass': password,
        'repeatPass': password,
        'userMail': email,
        'repeatMail': email
    }
    r = requests.post(endpoint+"login/register.php", data=pl)
    return r.text

while True:
    rstr = str(random.randint(1111111, 9999999))
    un = rstr+"relative"
    em = "rela"+rstr+"@hack.you"
    a = createAcc(un, "sosi", em)
    message = a.split("card-block buffer\">")[1].split("</div>")[0]
    print(message)
    print(un, ", sosi, ", em)
