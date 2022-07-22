#funcao para fazer o robo virar de lado
def turn():
    turn_left()
    turn_left()

#funcao para fazer o robo virar para a direita    
def turn_right():
    for n in range(3):
        turn_left()

#funcao para fazer o robo tracar o caminho em forma de um quadrado
def drawSquare():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#funcao que faz o robo pular
def jump():
    #caso ele tenha uma parede na direita dele, ele ira virar a esquerda (ira apontar para cima)
    #essa parte garante que se ele estiver acabado de chegar no chao apos ele pular uma parede,
    #ele ira se virar para a esquerda para continuar o percurso
    if wall_on_right()==1:
        turn_left()

    #quando ele estiver apontado pra cima, enquanto nao houver paredes em sua frente 
    #mas houverem paredes a sua direita, ele ira se mover    
    while wall_in_front()==0 and wall_on_right()==1:
        move()

    #quando ele chegar no ponto em que nao há mais paredes a sua direita, ele irá virar para
    #a direita, vai andar uma casa e vai virar para a direita (apontar para baixo)   
    if wall_on_right()==0:
        turn_right()
        move()
        turn_right()

        #agora apontando para baixo, enquanto nao houver nenhuma parede em sua frente, ele vai
        #se mover (no caso descer)
        while wall_in_front()!=1:
            move()
    
       