class Graphe:
    """
    cette classe permet de travailler sur des graphes simples, orientés ou non,
    valués ou non
    """
    def __init__(self):
        self.G=dict()
        self.pds=dict()
        
    def ajouteSommet(self,s):
        if s not in self.G.keys():
            self.G[s]=[]
    
    def ajouteArete(self,s,t,p=1):
        self.ajouteSommet(s)
        self.ajouteSommet(t)
        if t not in self.G[s]:
            self.G[s].append(t)
        if s not in self.G[t]:
            self.G[t].append(s)
        self.pds[(s,t)]=p
        self.pds[(t,s)]=p
        
    def ajouteArc(self,s,t,p=1):
        self.ajouteSommet(s)
        self.ajouteSommet(t)
        if t not in self.G[s]:
            self.G[s].append(t)
        self.pds[(s,t)]=p
   
    def sommets(self):
       return list(self.G.keys())
   
    def voisins(self,s):
       return self.G[s]
   
    import heapq
    import collections

    def Dijkstra(self, sommet_depart):
        """
        Cette fonction renvoie la distance la plus courte d'un sommet de
        départ vers tous les autres sommets d'un graphe pondéré.
        >>> Graph = {'A':{'B':1, 'C':2},
            'B':{'A':1, 'D':2, 'F':3},
            'C':{'A':2, 'D':3, 'E':4},
            'D':{'B':2, 'C':3, 'E':2, 'F':3, 'G':3},
            'E':{'C':4, 'D':2, 'G':5},
            'F':{'B':3, 'D':3, 'G':4},
            'G':{'D':3, 'E':5, 'F':4}}
        >>> print(Dijkstra(Graph, 'G'))
        OrderedDict([('A', 6), ('B', 5), ('C', 6), ('D', 3), ('E', 5), ('F', 4), ('G', 0)])
        """
        distances = {sommet: float('infinity') for sommet in self}
        # La distance du sommet de départ à lui-même est évidemment 0
        distances[sommet_depart] = 0

        liste = [(0, sommet_depart)]
        while len(liste) > 0:
            distance_actuelle, sommet_actuel = heapq.heappop(liste)

            # Permet de comparer plusieurs fois des distances pour un même sommet
            if distance_actuelle > distances[sommet_actuel]:
                continue

            # .items renvoie clés et valeurs du dictionnaire self
            for voisin, poids in self[sommet_actuel].items():
                plus_courte_distance = distance_actuelle + poids

                # Nouveau chemin uniquement pris s'il est meilleur que les précédents
                if plus_courte_distance < distances[voisin]:
                    distances[voisin] = plus_courte_distance
                    heapq.heappush(liste, (plus_courte_distance, voisin))

        # Permet d'obtenir un dictionnaire ordonné selon les clés
        # Tri obtenu avec lambda, où la valeur 0 indique les clés
        distances = collections.OrderedDict(sorted(distances.items(), key=lambda t: t[0]))
        return distances
    
    def kruskal(self):
        return
    
    def prim(self):
        """
        cette méthode implémente l'algorithme de Prim, qui construit un ACM
        """
        return
