import json, time
import keyboard
import httplib2

http = httplib2.Http()

def sendData(key):
    url_json = 'http://192.168.15.33/controller'   
    data = {'command': key}
    headers={'Content-Type': 'application/json; charset=UTF-8'}
    response, content = http.request(url_json, 'POST', headers=headers, body=json.dumps(data))
    return (response,content)
    
while True:
    if keyboard.is_pressed("w"):
        print(sendData("w"))
    if keyboard.is_pressed("s"):
        print(sendData("s"))
    if keyboard.is_pressed("a"):
        print(sendData("a"))
    if keyboard.is_pressed("d"):
        print(sendData("d"))
