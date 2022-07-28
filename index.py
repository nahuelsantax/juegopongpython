import pygame, datetime


pygame.init()


pygame.display.set_caption("Juego Pong")  #el nombre de la ventana



#Colores
black = (0, 0, 0)
white = (255, 255, 255)
green   =  (  0, 255,   0)
red     =  (255,   0,   0)
blue    =  (  0,   0, 255)
amarillo =	(255, 233, 0)
violeta = 	(120, 40, 140)



display_ancho = 800
display_altura = 600

screen_size = (display_ancho, display_altura)  #definimos las medidas de la ventana
player_width = 15
player_height = 90


screen = pygame.display.set_mode(screen_size)  #creamos la ventana
clock = pygame.time.Clock() #creamos el reloj para los fps 

#importar la imagen
background = pygame.image.load("fondo.png").convert()  #el metodo convert le facilita el trabajo a pygames para trabajar con imagenes


fuente = pygame.font.SysFont ("Copperplate Gothic bol", 39) #defino el tipo y tamaño de la letra 
#sound = pygame.mixer.Sound("ruido.MP3")

#Goudy stout

def menu():
    
    bandera = False

    while not bandera:
        screen.fill(black)
        
        menu_juego = fuente.render("MENU ", 0, (white))
        screen.blit(menu_juego,(330, 175))

        jugar = fuente.render("1)Reanudar", 0, (white))
        screen.blit(jugar,(300, 210))

        salir = fuente.render("2)Nueva partida", 0, (white))
        screen.blit(salir,(300, 240))
        
        reanudar = fuente.render("3)Salir", 0, (white))
        screen.blit(reanudar,(300, 270))
        


        pygame.display.update() 

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.type == pygame.QUIT:
                    python.quit()
    
                if event.key == pygame.K_1:
                    bandera = True 

                if event.key == pygame.K_2:
                    gameLoop()

                if event.key == pygame.K_3:
                    python.quit()








def gameLoop():
    
    #VARIABLES
     


    #Cronometro
    
    t = datetime.time(0, 0, 0)
    minutos =0
    horas =0

    # PUNTAJE 
    puntosJ1 = 0
    puntosJ2 = 0

    #Contador para cada gol, para alternar la direccion para donde sale la pelota cuando saca.
    contadorGoles = 0 



    #Coordenadas y velocidad del jugador 1
    player1_x_coor = 50
    player1_y_coor = 300 - 45
    player1_y_speed = 0

    #Coordenadas y velocidad del jugador 2
    player2_x_coor = 750 - player_width  #menos el ancho del jugador, para que no quede tan lejos del borde
    player2_y_coor = 300 - 45
    player2_y_speed = 0

    #Coordenadas de la pelota
    pelota_x = 400 #la mitad de 800 
    pelota_y = 300
    pelota_speed_x = 0
    pelota_speed_y = 0

    game_over = False  #una variable que te hace salir del bucle principal
    
    #game_exit = False

    while not game_over:
      


        # CRONOMETRO  
        segundos = pygame.time.get_ticks()/1000 #se divide por mil y aparece en segundos. el metodo getticks regresa un entero, es el valor entero en milisegundos desde que pygame.init esta ejecutnadose
        segundos = int(segundos) #asi no esta mas en flotante y queda en entero.
            
        segundos = segundos-(horas*3600+minutos*60)

        if segundos > 59:
            minutos = minutos + 1 #minutos + ((segundos -horas*3600)/60)
            segundos = 0 #si entra al if, segundos ya vale 60, por lo tanto lo ponemos en 0 para mostrar 0.

        if minutos > 59:
            horas = horas + 1
            minutos = 0
    
        t = datetime.time( int(horas) , int (minutos), int(segundos))  #segundos tiene que estar si o si entre 0 y 59 incluidos
        contadorTiempo = fuente.render("Tiempo: " + str(t) , 0, (120, 70, 0))  #lo convertimos a string el numero, si no pones "int" aparecen con los decimales. los numeros son el color en rgb
        
        
        # hacemos esto para que cuando recien arranque el juego, no este en movimiento y el usuario apriete el espacio para que se mueva.
        if segundos == 1:
        
            pelota_speed_x = 0
            pelota_speed_y = 0 

    
        





        # --- DETECTAR EVENTOS

        for event in pygame.event.get():

            # Para quitar el juego 
            if event.type == pygame.QUIT:
                game_over = True 

            # CUANDO APRETAS EL BOTON

            if event.type == pygame.KEYDOWN:
                # JUGADOR 1 
                if event.key == pygame.K_w:
                    player1_y_speed = -5 # quiero que vaya subiendo 
                if event.key == pygame.K_s:
                    player1_y_speed = 5


                if event.key == pygame.K_ESCAPE:
                    menu()
                #sound.play()

                # JUGADOR 2
                if event.key == pygame.K_UP:
                    player2_y_speed = -5 # quiero que vaya subiendo 
                if event.key == pygame.K_DOWN:
                    player2_y_speed = 5   


                # SAQUE DEL MEDIO
                if event.key == pygame.K_SPACE: 
                    if pelota_speed_x == 0 and pelota_speed_y == 0:  # validamos que la pelota este quieta, si no se cumple, no se puede usar el espacio
                        if contadorGoles % 2 == 0:   #Simplemente se hace para alternar el saque del medio, si es par que salga para arriba y si es impar para abajo
                            pelota_speed_x = 10    
                            pelota_speed_y = -10   
                        else: 
                            pelota_speed_x = -10
                            pelota_speed_y = 10   
                                    

            # CUANDO SOLTAS EL BOTON

            if event.type == pygame.KEYUP: # esto ses para cuando se suelta la tecla
                # JUGADOR 1 
                if event.key == pygame.K_w:
                    player1_y_speed = 0 
                if event.key == pygame.K_s:
                    player1_y_speed = 0



                # JUGADOR 2
                if event.key == pygame.K_UP:
                    player2_y_speed = 0  
                if event.key == pygame.K_DOWN:
                    player2_y_speed = 0   

                # SAQUE DEL MEDIO
                if event.key == pygame.K_SPACE:
                    if pelota_speed_x == 0 and pelota_speed_y == 0: # validamos que la pelota este quieta, si no se cumple, no se puede usar el espacio
                        if contadorGoles % 2 == 0:  #se hace lo mismo que arriba para que cuando se suelte el espacio, siga todo igual.
                            pelota_speed_x = 10
                            pelota_speed_y = -10   
                        else: 
                            pelota_speed_x = -10
                            pelota_speed_y = 10 

                if event.key == pygame.K_ESCAPE:
                    menu()            


        # --- DETECTAR EVENTOS
        

        #Hacemos el rebote de la pelota de arriba y de abajo
        if pelota_y >590 or pelota_y <10:
            pelota_speed_y *= -1


        #Vemos si la pelota sale del lado derecho
        if pelota_x > 800: #ve si la coordenada se pasa del limite de la ventana
            pelota_x = 400 #pone las 2 coordenadas para que arranque a moverse del medio
            pelota_y = 300

            pelota_speed_x *= 0  #Si la pelota se sale de la pantalla, invierte la direccion poniendo -1 y 1 en otro
            pelota_speed_y *= 0
            puntosJ1 += 1
            contadorGoles += 1

            # si se hace un gol, los dos jugadores empiezan desde cero en el medio, al igual que la pelota-
            player1_x_coor = 50
            player1_y_coor = 300 - 45
            player1_y_speed = 0

            player2_x_coor = 750 - player_width  
            player2_y_coor = 300 - 45
            player2_y_speed = 0
            

        if pelota_x < 0:
            pelota_x = 400 
            pelota_y = 300

            pelota_speed_x *= 0  
            pelota_speed_y *= 0
            puntosJ2 += 1  
            contadorGoles += 1

            # si se hace un gol, los dos jugadores empiezan desde cero en el medio, al igual que la pelota-
            player1_x_coor = 50
            player1_y_coor = 300 - 45
            player1_y_speed = 0

            player2_x_coor = 750 - player_width  
            player2_y_coor = 300 - 45
            player2_y_speed = 0            


        puntajeJ1 = fuente.render("Puntaje: " + str(puntosJ1) , 0, (120, 70, 0))
        puntajeJ2 = fuente.render("Puntaje: " + str(puntosJ2) , 0, (120, 70, 0))

        
            # if event.type == pygame.KEYDOWN:
                
            #     if event.key == pygame.K_SPACE:

            #       pelota_speed_x += 7   
            #       pelota_speed_y += -7


    



        #Modificamos las coordenadas para dar movimiento a los jugadores
        player1_y_coor += player1_y_speed
        player2_y_coor += player2_y_speed

    
        #Movimiento de pelota
        pelota_x += pelota_speed_x
        pelota_y += pelota_speed_y

        
        #Rebote de jugadores arriba y abajo 
        if ( player1_y_coor > 520 or player1_y_coor < 0 ):    #al principio (size = (800, 500)) definimos el tamaño de la pantalla, por eso ponemos 720
            player1_y_speed *= -1  #vamos a invertir la velocidad, el valor se hace negativo
        
        if ( player2_y_coor > 520 or player2_y_coor < 0):
            player2_y_speed *= -1


        player1_y_coor += player1_y_speed #speed vale algo negativo, entonces cuando lo sumas rebota
        player2_y_coor += player2_y_speed

        

        

        # ---- ZONA DE DIBUJO
        screen.blit(background, [0, 0])

        screen.blit(contadorTiempo,(308, 580))

        screen.blit(puntajeJ1,(65, 20))
        screen.blit(puntajeJ2,(600, 20))
        

        # if segundos % 2 == 0:
            
        #     jugador1 = pygame.draw.rect(screen, blue, (player1_x_coor, player1_y_coor, player_width, player_height))

        # else: jugador1 = pygame.draw.rect(screen, green, (player1_x_coor, player1_y_coor, player_width, player_height))

        jugador1 = pygame.draw.rect(screen, black, (player1_x_coor, player1_y_coor, player_width, player_height))
        jugador2 = pygame.draw.rect(screen, black, (player2_x_coor, player2_y_coor, player_width, player_height))    
        pelota = pygame.draw.circle(screen, red, (pelota_x, pelota_y), 10)
        
        # if segundos % 2 == 0:
            
        #     jugador2 = pygame.draw.rect(screen, red, (player2_x_coor, player2_y_coor, player_width, player_height))

        # else: jugador2 = pygame.draw.rect(screen, amarillo, (player2_x_coor, player2_y_coor, player_width, player_height))    
        
        
        # if segundos % 2 == 0:
            
        #     pelota = pygame.draw.circle(screen, black, (pelota_x, pelota_y), 10)

        # else: pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)    


        # ---- ZONA DE DIBUJOs

        # COLISIONES
        if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):  #pygames tiene el metodo "colliderect" para las colisiones
            pelota_speed_x *= -1

        pygame.display.flip()
        clock.tick(60)
gameLoop()


pygame.quit()

