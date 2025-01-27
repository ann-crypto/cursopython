import pygame
pygame.init()

# Carregar a imagem
imagem = pygame.image.load('iconefundobranco.jpg')

# Criar a tela de exibição (definindo tamanho da janela)
largura, altura = imagem.get_width(), imagem.get_height()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Exibir Imagem')

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Exibir a imagem na tela
    tela.blit(imagem, (0, 0))

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame
pygame.quit()
