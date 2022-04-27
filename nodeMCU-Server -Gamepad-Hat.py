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
    return (response,content)

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
                frenteTras = event.value[1]
                dirEsq = event.value[0]

                while (frenteTras > 0):
                    #Frente
                    for event in pygame.event.get():
                        if event.type == pygame.JOYHATMOTION:
                            if(event.value[1] == 0):
                                frenteTras = 0
                                
                    print("Frente, Resposta: \n", sendData("w"))

                while (frenteTras < 0):
                    #Ré
                    for event in pygame.event.get():
                        if event.type == pygame.JOYHATMOTION:
                            if(event.value[1] == 0):
                                frenteTras = 0
                                
                    print("Ré, Resposta: \n", sendData("s"))
                    

                while (dirEsq > 0):
                    #Dir
                    for event in pygame.event.get():
                        if event.type == pygame.JOYHATMOTION:
                            if(event.value[0] == 0):
                                dirEsq = 0
                                
                    print("Direita, Resposta: \n", sendData("d"))

                while (dirEsq < 0):
                    #Esq
                    for event in pygame.event.get():
                        if event.type == pygame.JOYHATMOTION:
                            if(event.value[0] == 0):
                                dirEsq = 0
                                
                    print("Esquerda, Resposta: \n", sendData("a"))

                
            elif event.type == pygame.JOYBUTTONDOWN:
                button = event.button
                print("Botão: ", button)
                if(button == 8):
                    running = False
 
        #clock.tick(20)
 
    pygame.quit()
 
main()
