class aresta:
    def __init__(self, noInicial, noFinal, label):
        self.noInicial = noInicial
        self.noFinal = noFinal
        self.label = label

    def getNoInicial(self):
        return self.noInicial
    
    def getNoFinal(self):
        return self.noFinal

    def getLabel(self):
        return self.label

class grafo:
    nos = []
    arestas = []
    
    def __init__(self):
        pass
    
    def addAresta(self, aresta):
        self.arestas.append(aresta)
        
    def addNos(self, no):
        if(no not in self.nos):
            self.nos.append(no)
            
    def getNos(self):
        return self.nos

    def getArestas(self):
            return self.arestas

fita = ""

def quebraPreSuf(listaFita, k):
    LinkedList = []
    for i in listaFita:
        a = aresta(i[0:k-1], i[1:k], i)
        LinkedList.append(a)

    for i in LinkedList:
        print("V1: {} V2: {} Label: {}".format(i.getNoInicial(), i.getNoFinal(), i.getLabel()))
        
    return LinkedList
        
def MontaEuleriano(linkedList):
    pass


with open("exemplo.txt", 'r') as file:
    fita += file.read()


fita = fita.replace(' ', '')

if(fita[-1] == ','):
    fita = fita[:-1]

fita = fita.split(',')
print(fita)
k = len(fita[0])

LinkedList = quebraPreSuf(fita,k)

grafoG = grafo()

for i in LinkedList:
    grafoG.addAresta(i)
    grafoG.addNos(i.getNoInicial())
    grafoG.addNos(i.getNoFinal())
    
print(grafoG.getNos())

def mountGraph(dnaFita, k):
    pass
