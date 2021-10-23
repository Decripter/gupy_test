import random as rd

moto_boys = ['','Moto 1','Moto 2','Moto 3','Moto 4','Moto 5']

def imprime_motos(comissao, moto):
        print(str(moto_boys[moto]) + ", Pedidos: 10")
        pedidos = 3
        print("Loja 1 - " + str(pedidos) + " Pedidos")
        print("Vai ganhar: $" + str(7.5+(comissao*pedidos)))
        pedidos = 4
        print("Loja 2 - " + str(pedidos) + " Pedidos")
        print("Vai ganhar: $" + str(10+(comissao * pedidos)))
        pedidos = 3
        print("Loja 3 - " + str(pedidos) + " Pedidos")
        print("Vai ganhar: $" + str(30+(comissao * pedidos)))
        print("Total : $" + str(47.5 +(comissao * 10)))

def sel_moto(moto=rd.randrange(1, 6)):
    if moto == 0 or moto > 5:
        sel_moto()
    
    elif moto == 4:
        pedidos = 3
        comissao = 2
        print(str(moto_boys[moto]) + ", Pedidos: 3")
        print("Loja 1 - " + str(pedidos) + " Pedidos")
        print("Vai ganhar: $" + str(7.5+(comissao * pedidos)))
        print("Total : $" + str(7.5+(comissao * pedidos)))

    elif moto == 5:
        imprime_motos(3, moto)#3 é  comissao do motoboy 5
        
    else: 
        imprime_motos(2, moto) #os demais motoboys tem a mesma comissao
    print("")

#inserir um valor entre 1 - 5 
#se não inserir nenhum valor ou valores diferentes o sistema fará um sorteio entre os motoboys disponíveis

sel_moto() #pode inserir o numero do motoboy diretamente dentro dos parênteses

# ou se preferir que apareca uma mensagem pedindo para o usuário inserir o número, 
# adicione uma cerquilha a sel_moto() acime e remova as cerquilhas '#' das 5 linhas abaixo:

#op = input("Digite o numero do motoboy") 
#if op == "":
#    sel_moto()
#else:
#    sel_moto(op)


