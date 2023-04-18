import pygame

pygame.init()
pygame.mixer.music.load("Fatality.mp3")

# loop principal do programa
while True:
    # verifica se alguma tecla foi pressionada
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # verifica se a tecla "P" foi pressionada
            if event.key == K_p:
                # toca a música
                pygame.mixer.music.play()
