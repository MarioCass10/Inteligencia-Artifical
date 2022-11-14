import copy
#Implementar la siguiente funcion para que devuelva el camino mas corto y su largo
lista_nodos = []
print(lista_nodos)
mejor_camino = 10000

grafo = [("S","A",2),("S","B",3),("A","C",4),("A","D",2),("B","E",4),("B","H",1),("E","G",2),("H","G",1)]

lista_nodos.append(("S",0,[]))


while len(lista_nodos) > 0:
    tmpNodo = lista_nodos.pop(0)
    nuevo_camino = tmpNodo[2].copy()
    nuevo_camino.append(tmpNodo[0])

    
    
    if tmpNodo[0] == "G" and mejor_camino > tmpNodo[1]:
        mejor_camino = tmpNodo[1]
        print(tmpNodo[1])
    
    for x,y,z in grafo:
        if x == tmpNodo[0]:
            lista_nodos.append((y,z + tmpNodo[1], nuevo_camino))
    print(lista_nodos)
print(mejor_camino, nuevo_camino)