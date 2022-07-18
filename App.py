import random
escolhas = ('PEDRA', 'PAPEL', 'TESOURA', 'LAGARTO', 'SPOCK')
n2 = False

	
print('Vamo jogar pedra, papel, tesoura, lagarto ou spock: \nAs regras sao:')
print('PEDRA esmaga LAGARTO e destroi TESOURA')
print('PAPEL cobre PEDRA e REFURA Spock')
print('TESOURA corta PAPEL e decapita LAGARTO')
print('LAGARTO envenena o SPOCK e come o PAPEL')
print('SPOCK quebra a TESOURA e vaporiza PEDRA')


	
##validando
while n2 == False:
    num = input('Digiteo numero correspondete do que voce deseja jogar: \n1-Pedra, \n2-Papel, \n3-Tesoura, \n4-Lagarto, \n5-Spock\n')
    try:
        num = int(num)
        if num > 5 or num < 0:
            print('numero invalida')

        else:
            n2=True

    except:
        print('formato invalido')
        

n3 = random.randint(0,4)
num=num-1
## 1 pedra 2 papel 3 tesoura 4 lagarto 5 spock

print('O seu computador escolheu: ', escolhas [n3])
print('Voce escolheu: ', escolhas [num])
n3 = n3 + 1
num=num+1
if n3 == num:
    print ('EMPATE')
    
elif num == 1 and n3 == 3:
    print ('voce venceu')

elif num == 1 and n3 == 4:
    print ('voce venceu')
    
elif num == 2 and n3 == 1:
    print ('voce venceu')

elif num == 2 and n3 == 5:
    print ('voce venceu')

elif num == 3 and n3 == 2:
    print ('voce venceu')
           
elif num == 3 and n3 == 4:
    print ('voce venceu')         

elif num == 4 and n3 == 2:
    print ('voce venceu')

elif num == 4 and n3 == 5:
    print ('voce venceu')

elif num == 5 and n3 == 3:
    print ('voce venceu')

elif num == 5 and n3 == 1:
    print ('voce venceu')
    
else:
    print ('voce perdeu')
    