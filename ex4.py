v1 = 0
v2 = 0
v3 = 0
v4 = 0


for i in range (20):
    opçao = input("Escolha umaopção (1-Pablo nasal 2-peixe 3-El_primo 4-Mosquito)")
    match opçao:
        case "1":
            Plabo_nasal=input("sou triolimpico")
            v1+=1
        case "2":
            peixe=input("Vou te catar na porrada")
            v2+=1
        case "3":
            El_primo=input("pela gloria e pela dor")
            v3+=1
        case "4":
            Mosquito = input("Sou gay")
            v4+=1  
        case _:
            print("opção invalida")

print(f'O candidato 1 resebeu: ' +str (v1) + " votos")
print(f'O candidato 2 resebeu: ' +str (v2)+ " votos")
print(f'O candidato 3 resebeu: ' +str (v3)+ " votos")
print(f'O candidato 4 resebeu: ' +str (v4)+ " votos")