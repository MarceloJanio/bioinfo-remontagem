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
    nos = {}
    arestas = []
    initialNode = ""
    finalNode = ""
    
    def __init__(self):
        pass
    
    def addAresta(self, aresta):
        self.arestas.append(aresta)
        
    def addNos(self, no, operation):
        if(no not in self.nos):
            self.nos[no] = [0,0]
        if operation == "pre":
            self.nos[no] = [self.nos[no][0] + 1, self.nos[no][1]]
        if operation == "suf":
            self.nos[no] = [self.nos[no][0], self.nos[no][1] + 1]
            
    def getNos(self):
        return self.nos

    def getArestas(self):
        return self.arestas
    
    def setInitialNode(self, no):
        self.initialNode = no

    def getInitialNode(self):
        return self.initialNode 
    
    def setFinalNode(self, no):
        self.finalNode = no

    def getFinalNode(self):
        return self.finalNode 
    
    def MontaEuleriano(self):
        pointer = self.initialNode
        self.arestas

fita = ""

def quebraPreSuf(listaFita, k):
    dictGraph = {}
    for i in listaFita:
        prefix = i[0:k-1]
        sufix = i[1:k]
        if(prefix in dictGraph.keys()):
            dictGraph[prefix][0].append(sufix)
            dictGraph[prefix][1][0] = dictGraph[prefix][1][0] + 1
        else:
            dictGraph[prefix] = [[sufix],[1,0]]

        if(sufix not in dictGraph.keys()):
            dictGraph[sufix] = [[],[0,1]]
        else:
            dictGraph[sufix][1][1] = dictGraph[sufix][1][1] + 1

    print(dictGraph)
        
    return dictGraph
        
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

# grafoG = grafo()

# for i in LinkedList:
#     grafoG.addAresta(i)
#     grafoG.addNos(i.getNoInicial(), "pre")
#     grafoG.addNos(i.getNoFinal(), "suf")
    
# for key, value in grafoG.getNos().items():
#     if value[0] > value[1]:
#         grafoG.setInitialNode(key)
#     if value[1] > value[0]:
#         grafoG.setFinalNode(key)

#     if(grafoG.getFinalNode() != "" and grafoG.getInitialNode() != ""):
#         break

# print(grafoG.getNos())
# print(grafoG.getInitialNode())
# print(grafoG.getFinalNode())

# def mountGraph(dnaFita, k):
#     pass
