from Heap import Heap

def Prim(graphe,s):
    '''
    La fonction Prim prend en paramètres une liste d'adjascence comme
    représentation d'un graphe et un sommet présent dans le graphe,
    et elle revoie un arbre couvrant minimal du graphe créé suivant la méthode
    de l'agorithme de prim donné. Les doublons d'arrêtes ne sont pas renvoyés.
    La fonction renverra un dictionnaire vide si le graphe est de longueur
    nulle/1 ou si le sommet passé en paramètre n'appartient pas au graphe.
    Fonction Réalisée par Hugo MARTIN.
    
    >>> Prim({'A':[('B',5),('C',7)], 'B':[('C',8)], 'C':[('D',3)], 'D':[]},'A')
    {'A': [('B', 5), ('C', 7)], 'B': [], 'C': [('D', 3)], 'D': []}
    >>> Prim({'A':[('B',5),('C',7)], 'B':[('C',8)], 'C':[('D',3)], 'D':[]},'M')
    {}
    >>> Prim({'A':[]},'A')
    {}
    >>> Prim({},'A')
    {}
    '''
    if len(graphe) == 0 or len(graphe) == 1 or s not in graphe.keys():          #Cas de base
        return {}
    acm = {}
    f = Heap()
    for i in graphe.keys():
        acm[i] = []                                                             #Création du graphe à renvoyer
        for j in range(len(graphe[i])):
            f.insert([graphe[i][j][1],i,graphe[i][j][0]])                       #Création du Heap

    vus = [s]
    waiting = []
    while len(vus) != len(graphe):                                              #Exploitation du Heap pour résoudre le problème
        value = f.shorten()
        if value == None:                                                           #i.e Si le Heap est vide
            for elem in waiting:
                f.insert(elem)
            waiting = []
        elif (value[1] in vus) != (value[2] in vus):                                #i.e Sinon si un sommest est dans vus et l'autre non
            acm[value[1]].append((value[2],value[0]))
            if value[1] in vus:
                vus.append(value[2])
            else:
                vus.append(value[1])
        elif (not value[1] in vus) and (not value[2] in vus):                       #sinon si aucun des deux sommets n'est dans vus (arrête encore inaccesible)
            waiting.append(value)

    return acm
		
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    G = {'A':[('B',5),('C',7)], 'B':[('C',8)], 'C':[('D',3)], 'D':[]}
    G_bis = {}
    G_ter = {'A':[]}
    assert(Prim(G,'A') == {'A': [('B', 5), ('C', 7)], 'B': [], 'C': [('D', 3)], 'D': []})
    assert(Prim(G,'M') == {})
    assert(Prim(G_bis,'A') == {})
    assert(Prim(G_ter,'A') == {})
		
		
