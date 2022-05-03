import pygame
import json
import httplib2

http = httplib2.Http()
pygame.init()

def sendData(key):
    url_json = 'http://192.168.15.33/controller'   
    data = {'command': key}
    headers={'Content-Type': 'application/json; charset=UTF-8'}
    response, content = http.request(url_json, 'POST', headers=headers, body=json.dumps(data))
    return (key)

def main():
    clock = pygame.time.Clock()
    running = True
 
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for joy in joysticks:
        joy.init()
 
    while running:
        for event in pygame.event.get():
            '''if event.type == pygame.JOYAXISMOTION:
                print(event)'''
            if event.type == pygame.JOYHATMOTION:
                print(event)
                frenteTras = event.value[1]
                dirEsq = event.value[0]


                if frenteTras == 1:
                    print(sendData("2"))
                if frenteTras == -1:
                    print(sendData("1"))
                

                if dirEsq == 1:
                    print(sendData("4"))
                if dirEsq == -1:
                    print(sendData("3"))

                if frenteTras == 0 and dirEsq==0:
                    print(sendData("0"))

                #print(frenteTras)


                
            elif event.type == pygame.JOYBUTTONDOWN:
                button = event.button
                print("Botão: ", button)
                if(button == 8):
                    running = False
                if(button == 4):
                    print(sendData("5"))
                if(button == 5):
                    print(sendData("6"))
 
        #clock.tick(20)
 
    pygame.quit()
 
main()
