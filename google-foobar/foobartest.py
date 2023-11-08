
def solution(data, n):
    x = 0
    for i in range(0, 100):
        for j in data:
            if(i == j):
                x +=1
            if(x == n):
                print(str(i)+","+str(x))
                x = 0
def listar_itens(lista):
    for item in lista:
        print(item)
        


lista = ["a", "b", "c"]
listar_itens(lista)
    
b = [1, 2, 2, 3, 3, 3, 4, 5, 5]
solution(b,1)