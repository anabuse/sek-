#!/usr/bin/env python3
import ev3dev.ev3 as ev3

motorEsq = ev3.LargeMotor('outC'); assert motorEsq.connected
motorDir = ev3.LargeMotor('outB'); assert motorDir.connected
## motorGarra = ev3.MediumMotor('outA'); assert motorGarra.connected

## Sensores de cor
corEsq = ev3.ColorSensor('in1'); assert corEsq.connected
corEsq.mode = 'COL-COLOR'

corDir = ev3.ColorSensor('in4'); assert corDir.connected
corDir.mode = 'COL-COLOR'

corCheck = ev3.ColorSensor('in2'); assert corCheck.connected
corCheck.mode = 'COL-COLOR'

# Valores
velocidade = -300    
delta = 100         # delta de velocidade nas curvas
K = 3               # K proporcional da curva

branco=6
preto=1
nocolor=0

cor[1]=0
cor[2]=0
cor[3]=0
n[1]=0
n[2]=0
n[3]=0
t = 100

def andareto():

    while corCheck.value() == branco:
     # Valor dos sensores a cada loop

        motorEsq.run_timed(speed_sp = velocidade, time_sp = t)
        motorDir.run_timed(speed_sp = velocidade, time_sp = t)
            
            # Testar NO-COLOR nos sensores para ajeitar o caminho
        if corDir.value() == 0:
            motorEsq.run_timed(speed_sp = velocidade + delta, time_sp = t)
            motorDir.run_timed(speed_sp = velocidade - delta, time_sp = t)
            
        if corEsq.value() == 0:
            motorDir.run_timed(speed_sp = velocidade + delta, time_sp = t)
            motorEsq.run_timed(speed_sp = velocidade - delta, time_sp = t)

def saindoReto():
     while(corCheck.value() != branco): 
         motorEsq.run_timed(speed_sp = velocidade, time_sp = t)
         motorDir.run_timed(speed_sp = velocidade, time_sp = t)
            
            # Testar NO-COLOR nos sensores para ajeitar o caminho
         if corDir.value() == 0:
            motorEsq.run_timed(speed_sp = velocidade + delta, time_sp = t)
            motorDir.run_timed(speed_sp = velocidade - delta, time_sp = t)
            
         if corEsq.value() == 0:
            motorDir.run_timed(speed_sp = velocidade + delta, time_sp = t)
            motorEsq.run_timed(speed_sp = velocidade - delta, time_sp = t)

#funcao seguir frente dependendo da necessidade

def seguirfrente(x):
    motorDir.run_to_rel_pos(position_sp = -x, speed_sp = velocidade)
    motorEsq.run_to_rel_pos(position_sp = -x, speed_sp = velocidade)
    motorDir.wait_while("running")
    motorEsq.wait_while("running")

#funcao curva direita

def curvadir():
    parar()
    seguirfrente(200)
    motorDir.run_timed(speed_sp = 100, time_sp = 32 * t)
    motorEsq.run_timed(speed_sp = (-1) * 100, time_sp = 32 * t)
    motorDir.wait_while("running")
    motorEsq.wait_while("running")

#funcao curva esquerda

def curvaesq():
    parar()
    seguirfrente(200)
    motorEsq.run_timed(speed_sp = 100, time_sp = 32 * t)
    motorDir.run_timed(speed_sp = (-1) * 100, time_sp = 32 * t)
    motorDir.wait_while("running")
    motorEsq.wait_while("running")
   
#funçao meia volta

def darmeiavolta():
    motorDir.run_timed(speed_sp = 100, time_sp = 64 * t)
    motorEsq.run_timed(speed_sp = (-1) * 100, time_sp = 64 * t)
    motorDir.wait_while("running")
    motorEsq.wait_while("running")

#função parar

def parar():
    motorDir.stop()
    motorEsq.stop()


while True:

    print("Estou aqui!", valorCorCheck())
    andareto()  ## Andar em Linha Reta ate ver uma cor
         while corCheck.value() not in {branco}: ## Checar se o ladrilho é colorido
             c[1]=corCheck.value() 
             curvadir()
             print("c1 =", c[1], ": corCheck.value =", corCheck.value()) 

         saindoReto()
         print("Seguiu de novo")
         andareto() ## anda enquanto for branco
         print("Estais aqui?") ## está em algo diferente do branco

         while n[1] == 0: ## n1 = 0 significa que ele não decidiu nada ainda
             print("Entrou no while hahaha")

             if corCheck.value() not in {branco}: ## se chegar em algo que não seja branco, ele para
                 parar()
             if corCheck.value() not in {branco, preto}: ## se esse algo for uma cor (tira preto e branco), ele grava
                 n[1] = 1
             else:  ## ele está em preto, logo ele volta
                 darmeiavolta()     
                 saindoReto()
                 print("Seguiu de novo")
                 andareto()
                 print("cor ", corCheck.value()) ##tava vendo marrom no branco
                ## voltando para o primeiro ladrilho
                 if corCheck.value() == c[1]:
                     curvadir() ##virando pela segunda vez para a direita na primeira cor
                     saindoReto()
                     print("Seguiu de novo")
                     andareto()
                     while valorCorCheck() != branco:
                         parar() ##se a proxima cor for difrerente de preto a primeira cor é seguir em frente e chegamos na segunda cor
                         if valorCorCheck() != preto:
                                 n[1]=2 ##se a proxima cor nao for preto entao a primeira é seguir frente
                         else:
                             n[1]=3 ##se a proxima for preto entao a primeira é virar a esquerda
                             #voltando para a primeira cor
                             darmeiavolta()
                             saindoReto()
                             andareto()
                                 if valorCorCheck() ==c[1]:
                                     curvadir()
                                     andareto()
                                     if valorCorCheck !=branco:
                                         parar()
                                       
     while n[3]==0:  ##se a primeira cor foi igual a segunda, da ruim, pq ainda n aprendeu oq signica as duas outras cores
     ##por isso ele n sai desse loop enquanto n tiver passado por duas cores diferentes e ter definido o cada uma significa
     #estamos parados na segunda cor
     #chegar se a segunda cor é igual a primeira da ruim
         if valorCorCheck() ==c[1]:
             if n[1]==1:
                   curvadir()
             if n[1]==2:
                  seguirfrente(700) ##OU SAINDORETO VER OQ EH MELHOR
             if n[1]==3:
                  curvaesq()
             saindoReto()
             andareto() ##anda ate o terceiro quadrado
              
         
         else:
         c[2]= valorCorCheck()
             if n[1]==1:
                 seguirfrente()
                 andareto() ##anda ate o terceiro quadrado
                 if valorCorCheck() != preto: ##se o terceiro quadrado é uma cor
                     n[2]=2
                     n[3]=3
                 else:    ##se for preto e o caminho ta errado
                     n[2]=3
                     n[3]=2
                     darmeiavolta()
                     saindoReto()
                     andareto()
                      if valorCorCheck() == c[2]
                          curvadir()
                          saindoReto()
                          andareto() ##anda ate o terceiro quadrado para no inico deste, quando o sensor ver a cor

             if n[1]==2: ## ta na segunda cor sendo q a primeira é seguir frente
                 curvadir()
                 saindoReto() ##anda ate o terceiro quadrado
                 andareto() 
                 if valorCorCheck() != preto: ##se chegar em uma cor, a segunda cor é virar a direita e a outra é virar a esquerda
                     n[2]=1
                     n[3]=3
                 else:   ##se nao chegar em cor, a segunda é virar a esquerda e a outra é direita
                     n[2]=3
                     n[3]=1
                     darmeiavolta()
                     andareto()
                     if valorCorCheck() == c[2]:
                         seguirfrente()
                         andareto()
             if n[1]==3:
                 seguirfrente()
                 andareto() ##anda ate o terceiro quadrado
                 if valorCorCheck() != preto: ##se o terceiro quadrado é uma cor
                     n[2]=2
                     n[3]=1
                 else:    ##se for preto e o caminho ta errado
                     n[2]=1
                     n[3]=2
                     darmeiavolta()
                     saindoReto()
                     andareto()
                      if valorCorCheck() == c[2]
                          curvaesq()
                          saindoReto()
                          andareto() ##anda ate o terceiro quadrado para no inico deste, quando o sensor ver a cor

     ##nao sabemos mais em que quadrado estamos, mas paramos no inicio deste, e que é da terceira cor
     c3= valorCorCheck()
     print("aprendeu que a terceira cor é", c[3] )
     while True: ##ate ver rampa. ver como mud IMPORTANTE
         for i in [1,2,3]:
             if valorCorCheck() ==c[i]:
                 if n[i]==1:
                     curvadir()
                 if n[i]==2:
                     seguirfrente(700) ##OU SAINDORETO VER OQ EH MELHOR
                 if n[i]==3:
                     curvaesq()
                 saindoReto()
                 andareto()
        
         





