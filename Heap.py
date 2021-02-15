class Heap:
    """
    La structure de tas binaire minimal est définie par ses primitives :
    * un constructeur crée un tas vide
    * entasse ajoute un élément dans le tas, en conservant la structure de tas, 
    * minimum renvoie la racine, qui est le minimum des éléments du tas,
    en conservant la structure de tas.
    """
    
    def __init__(self):
        '''
        Fonction par Hugo MARTIN, crée un tas binaire.
        '''
        sekf.heap = []
    
    def entasse(self,e):
        '''
        Fonction par Hugo MARTIN, insère un élément dans le tas binaire.
        '''
        self.heap.append(n)
        index_n = len(self.heap)-1
        while n[0] < self.heap[int((index_n-1)/2)][0]:
            self.heap[index_n], self.heap[int((index_n-1)/2)] = self.heap[int((index_n-1)/2)],self.heap[index_n]
            index_n = int((index_n-1)/2)   
            
            
    def minimum(self):
        '''
        Fonction par Hugo MARTIN, renvoie le plus petit élément du tas binaire minimal.
        '''
        if self.heap == []:
            return None
        r_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        if self.heap == []:
            return r_value
        n = self.heap[0][0]
        index_n=0
        while (len(self.heap)-1 >= 2*index_n+1 and n > self.heap[2*index_n +1][0]) or (len(self.heap)-1 >= 2*index_n+2 and n > self.heap[2*index_n +2][0]):
            if len(self.heap)-1 == 2*index_n +1: #un seul fils
                change_index = 2*index_n +1
            else:                                #deux fils
                if self.heap[2*index_n +1][0] > self.heap[2*index_n +2][0]:
                    change_index = 2*index_n + 2
                else:
                    change_index = 2*index_n +1
            self.heap[index_n],self.heap[change_index] = self.heap[change_index],self.heap[index_n]
            index_n = change_index
            n = self.heap[index_n][0]
        return r_value

