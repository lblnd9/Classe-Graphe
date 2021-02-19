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
    
    def kruskal(self):
        return
