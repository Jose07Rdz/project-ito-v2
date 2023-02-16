import pygame, random, time

pygame.init() 

size = (600, 600) 

screenMenu = pygame.display.set_mode(size) 

menuOver = False

def drawText(surface , text, size, x, y):
    font = pygame.font.SysFont("serif", size)
    textSurface = font.render(text, True, [255, 255, 255])
    textRect = textSurface.get_rect()
    textRect.midtop = (x, y)
    surface.blit(textSurface, textRect)

finger = pygame.image.load("finger.png").convert()
backgroundMenu = pygame.image.load("fondo1.jpg").convert()
# finger.set_colorkey([255,255,255])

fingerCoor = [200,300]

while not menuOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menuOver = True

        #DEDO EN JUGAR
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                fingerCoor = [200, 300]

        #DEDO EN SALIR
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                fingerCoor = [200, 330]

        #SALIR DEL MENU
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if fingerCoor == [200, 330]:
                    menuOver = True

        #ENTRAR AL JUEGO
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if fingerCoor == [200, 300]:

                    #VARIABLES GLOBALES
                    WIDE = 600
                    HEIGHT = 600 

                    #CONFIGURACION INICIAL
                    pygame.init()
                    screenGame = pygame.display.set_mode([WIDE, HEIGHT])
                    clock = pygame.time.Clock()
                    gameOver = False

                    #FUNCIONES
                    def drawText(surface , text, size, x, y):
                        font = pygame.font.SysFont("serif", size)
                        textSurface = font.render(text, True, [255, 255, 255])
                        textRect = textSurface.get_rect()
                        textRect.midtop = (x, y)
                        surface.blit(textSurface, textRect)

                    def meteorBig():
                        for i in range(10):
                            meteorBig = MeteorBig()
                            meteorBig.rect.x = random.randrange(580)
                            meteorBig.rect.y = random.randrange(300)

                            meteorBigList.add(meteorBig)
                            allSprite.add(meteorBig)

                    def finalBoss():
                        vilgax = FinalBoss()
                        vilgax.rect.x = 200
                        vilgax.rect.y = 0

                        boosList.add(vilgax)
                        allSprite.add(vilgax)

                    def powerBall(x):
                        for i in range(x):
                            ball = WaveVital()
                            ball.rect.x = random.randrange(600)
                            ball.rect.y = random.randrange(170,300)

                            ballList.add(ball)
                            allSprite.add(ball)

                    #CLASES
                    class Meteor(pygame.sprite.Sprite):
                        def __init__(self):
                            super().__init__()
                            self.image = pygame.image.load("meteor.png").convert()
                            self.image.set_colorkey([0, 0, 0])
                            self.rect = self.image.get_rect()

                        def update(self):
                            self.rect.y += 1

                            if self.rect.y > 600:
                                self.rect.y = -10
                                self.rect.x = random.randrange(600)

                    class MeteorBig(pygame.sprite.Sprite):
                        def __init__(self):
                            super().__init__()
                            self.image = pygame.image.load("meteoroGrande.png").convert()
                            self.image.set_colorkey([0, 0, 0])
                            self.rect = self.image.get_rect()

                        def update(self):
                            self.rect.y += 1.5

                            if self.rect.y > 600:
                                self.rect.y = -20
                                self.rect.x = random.randrange(600)

                    class FinalBoss(pygame.sprite.Sprite):
                        def __init__(self):
                            super().__init__()
                            self.image = pygame.image.load("vilgax.png").convert()
                            self.image.set_colorkey([0, 0, 0])
                            self.rect = self.image.get_rect()

                        def update(self):
                            self.rect.x = 200
                            self.rect.y = 30

                    class Player(pygame.sprite.Sprite):
                        def __init__(self):
                            super().__init__()
                            self.image = pygame.image.load("player.png").convert()
                            self.image.set_colorkey([0, 0, 0])
                            self.rect = self.image.get_rect()

                        def update(self):
                            player.rect.x = playerCoorX
                            player.rect.y = playerCoorY

                    class Laser(pygame.sprite.Sprite):
                        def __init__(self):
                            super().__init__()
                            self.image = pygame.image.load("laser.png").convert()
                            self.image.set_colorkey([0, 0, 0])
                            self.rect = self.image.get_rect()

                        def update(self):
                            self.rect.y -= 5
                        
                            if self.rect.y > 600:
                                self.rect.y = 200
                                self.rect.x = random.randrange(600)

                    class WaveVital(pygame.sprite.Sprite):
                        def __init__(self):
                            super().__init__()
                            self.image = pygame.image.load("power.png").convert()
                            self.image.set_colorkey([255, 255, 255])
                            self.image.set_colorkey([0, 0, 0])
                            self.rect = self.image.get_rect()

                        def update(self):
                            self.rect.y += 1

                            if self.rect.y > 600:
                                self.rect.y = 200
                                self.rect.x = random.randrange(600)

                    #LISTAS
                    meteorList = pygame.sprite.Group()
                    meteorBigList = pygame.sprite.Group()
                    allSprite = pygame.sprite.Group()
                    laserList = pygame.sprite.Group()
                    boosList = pygame.sprite.Group()
                    ballList = pygame.sprite.Group()

                    #ARCHIVOS IMPORTADOS
                    backgroundImage = pygame.image.load("espacio.png").convert()
                    laserSound = pygame.mixer.Sound("laser5.ogg")
                    gameOverSound = pygame.mixer.Sound("gameOver.mp3")
                    winSound = pygame.mixer.Sound("winSound.mp3")

                    #VARIABLES
                    player = Player()
                    allSprite.add(player)
                    score = 0
                    speedPlayer = 0
                    playerCoorX = WIDE/2 - 37.5
                    playerCoorY = HEIGHT - 125

                    #CICLOS
                    for i in range(50):
                        meteor = Meteor()
                        meteor.rect.x = random.randrange(580)
                        meteor.rect.y = random.randrange(300)

                        meteorList.add(meteor)
                        allSprite.add(meteor)

                    #CICLO PRINCIPAL DEL JUEGO
                    while not gameOver:
                        #EVENTOS
                        for event in pygame.event.get():
                            #EVENTO DE CERRAR LA VENTANA
                            if event.type == pygame.QUIT:
                                gameOver = True
                            
                            #EVENTO PRESIONAR TECLA ESPACIO - DISPARAR
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    laser = Laser()
                                    laser.rect.x = player.rect.x + 45
                                    laser.rect.y = player.rect.y -20

                                    allSprite.add(laser)
                                    laserList.add(laser)
                                    laserSound.play()

                            #EVENTO DE PRESIONAR FLECHAS - MOVER NAVE
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RIGHT:
                                    speedPlayer = 5
                            
                            if event.type == pygame.KEYUP:
                                if event.key == pygame.K_RIGHT:
                                    speedPlayer = 0

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                    speedPlayer = -5

                            if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT:
                                    speedPlayer = 0

                        #LOGICA DEL JUEGO
                        allSprite.update()    
                        for laser in laserList:
                            #COLISIONES - LASER/METEOROS CHICOS
                            meteorHitList = pygame.sprite.spritecollide(laser, meteorList, True)
                            for meteor in meteorHitList:
                                allSprite.remove(laser)
                                laserList.remove(laser)

                            for meteor in meteorHitList:
                                score += 5

                            if score == 250:
                                score = 500
                                meteorBig()

                            if score == 2000:
                                score = 5000
                                finalBoss()
                                powerBall(40)
                                
                            if len(ballList) < 20 and score > 5000:
                                powerBall(25)

                            #COLISIONES - LASER/METEOROS GRANDES
                            meteorHitList = pygame.sprite.spritecollide(laser, meteorBigList, True)
                            for meteor in meteorHitList:
                                allSprite.remove(laser)
                                laserList.remove(laser)

                            for meteor in meteorHitList:
                                score += 100

                            #COLISIONES - LASER/JEFE FINAL
                            bossHitList = pygame.sprite.spritecollide(laser, boosList, False)
                            for boss in bossHitList:
                                allSprite.remove(laser)
                                laserList.remove(laser)

                            for boss in bossHitList:
                                score += 50

                            #COLISION - LASER/ONDA VITAL
                            ballHitList = pygame.sprite.spritecollide(laser, ballList, True)
                            for ball in ballHitList:
                                allSprite.remove(laser)
                                laserList.remove(laser)

                        
                        #COLISIONES - JUGADOR/METEOROS CHICOS
                        hits = pygame.sprite.spritecollide(player, meteorList, False)
                        if hits:
                            gameOver = True

                        #COLISIONES - JUGADOR/METEOROS GRANDES
                        hits = pygame.sprite.spritecollide(player, meteorBigList, False)
                        if hits:
                            gameOver = True

                        #COLISIONES - JUGADOR/ONDA VITAL
                        hits = pygame.sprite.spritecollide(player, ballList, False)
                        if hits:
                            gameOver = True

                        if playerCoorX < 0 : playerCoorX = 10
                        elif playerCoorX > 501 : playerCoorX = 491
                        else: playerCoorX += speedPlayer

                        #FONDO DE PANTALLA
                        screenGame.blit(backgroundImage, [0, 0])

                        #ZONA DE DIBUJO
                        allSprite.draw(screenGame)
                        drawText(screenGame, str("Pts "+ str(score)), 25, 300, 10)

                        if score <= 250 :
                            objective = "Objetivo: 250pts"
                        elif score >= 250 and score <= 2000:
                            objective = "Objetivo: 3000pts"
                        elif score > 3000:
                            objective = "Objetivo: 10000pts"

                        drawText(screenGame, str(objective), 25, 115, 570)

                        if gameOver:
                            gameOverStr = "Juego Terminado"
                            drawText(screenGame, str(gameOverStr), 50, 300, 300)
                            gameOverSound.play()
                        
                        if score > 10000:
                            winStr = "Victoria Magistral"
                            drawText(screenGame, str(winStr), 50, 300, 300)
                            winSound.play()
                            time.sleep(3)
                            pygame.quit()

                        #CONFIGURACION
                        pygame.display.flip()
                        clock.tick(60) #FPS

                    time.sleep(3)
                        
    screenMenu.blit(backgroundMenu, [-1500, -475])

    drawText(screenMenu, str("JUGAR"), 25, 300, 300)
    drawText(screenMenu, str("SALIR"), 25, 300, 330)

    screenMenu.blit(finger, fingerCoor)

    pygame.display.flip()

pygame.quit()