import requests
import asyncio
endpoint = "http://aspirix.ru/sp/"
async def getSong(sid):
    data = {
        'songID': sid
    }
    r = requests.post(endpoint+"database/getGJSongInfo.php", data=data)
    print(r.text)

startpos = 600000
endpos = 99999999
while startpos <= endpos:
    asyncio.run(getSong(startpos))
    startpos+=1
