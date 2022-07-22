from library import *

#loop que para quando chega no objetivo
while at_goal()!=1:
    
    #fica checando se há uma parede na frente ou não
    if wall_in_front()==1:
        #tem parede, entao chama a funcao jump
       jump()
    elif wall_in_front()==0 and is_facing_north()==0:
        #nao tem parede e ele nao esta virado pra cima, entao ele se move
       move()

    #quando chegar no objetivo, chama a funcao done para parar.
    if at_goal()==1:
    done()   