from Heap import Heap
import copy

def Prim(graphe,s):
    '''
    Fontion Réalisée par Hugo MARTIN.
    La fonction Prim prend en paramètre une liste d'adjascence comme
    représentation d'un graphe et un sommet présent dans le grapphe,
    et revoie un arbre couvrant minimal du graphe créé suivant la méthode de
    l'agorithme de prim donné. Les doublons d'arrêtes ne sont pas renvoyés.
    La fonction renverra un dictionnaire vide si le graphe est de longueur
    nulle/1 ou si le sommet passé en paramètre n'appartient pas au graphe.
    >>> Prim({'A':[('B',5),('C',7)], 'B':[('C',8)], 'C':[('D',3)], 'D':[]},'A')
    {'A': [('B', 5), ('C', 7)], 'B': [], 'C': [('D', 3)], 'D': []}
    >>> Prim({'A':[('B',5),('C',7)], 'B':[('C',8)], 'C':[('D',3)], 'D':[]},'M')
    {}
    >>> Prim({'A':[]},'A')
    {}
    >>> Prim({},'A')
    {}
    '''
    if len(graphe) == 0 or len(graphe) == 1 or s not in graphe.keys():
        return {}
    acm = {}
    f = Heap()
    len_f = 0
    for i in graphe.keys():
        acm[i] = []
        for j in range(len(graphe[i])):
            f.insert([graphe[i][j][1],i,graphe[i][j][0]])
            len_f += 1

    heap = copy.deepcopy(f)
    vus = [s]
    while len(vus) != len(graphe):
        value = f.shorten()
        if (value[1] in vus) != (value[2] in vus):
            acm[value[1]].append((value[2],value[0]))
            f = copy.deepcopy(heap)
            if value[1] in vus:
                vus.append(value[2])
            else:
                vus.append(value[1])
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
		
		
