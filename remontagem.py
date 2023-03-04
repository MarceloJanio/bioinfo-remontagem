import time

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
        
def findInitialnFinal(dictGraph):
    initial = ""
    final = ""

    for key, value in dictGraph.items():
        if(value[1][0] > value[1][1]):
            initial = key
        if(value[1][0] < value[1][1]):
            final = key
    
    if(initial != "" and final != ""):
        print("{} {}".format(initial, final))
        return initial, final

## abre arquivo
with open("exemplo2.txt", 'r') as file:
    fita += file.read()


fita = fita.replace(' ', '')

if(fita[-1] == ','):
    fita = fita[:-1]

fita = fita.split(',')
print(fita)
k = len(fita[0])
###########################


LinkedList = quebraPreSuf(fita,k)
initial, final = findInitialnFinal(LinkedList)

def montaEuleriano(dictGrafo, initial, k):
    primeiraParte = ""
    segundaParte = ""
    sequencias = []

    fita = initial
    ponteiro = initial

    print(dictGrafo.get(ponteiro)[0])

    while(len(dictGrafo.keys())!=0):
        if(dictGrafo.get(ponteiro)[0] != []):
            remove = ponteiro
            ponteiro = dictGrafo.get(ponteiro)[0][0]
            fita += ponteiro[-1]
            dictGrafo[remove][0].remove(ponteiro)
            if(len(dictGrafo.get(remove)[0]) == 0):
                del dictGrafo[remove]
            if(dictGrafo.get(ponteiro) == None):
                fitaAux = fita
                fita = primeiraParte+fitaAux+segundaParte
                for i in range(0, len(fita)-1):
                    atual = fita[i:i+2]
                    if(dictGrafo.get(atual) != None):
                        ponteiro = atual
                        primeiraParte = fita[0:i+2]
                        segundaParte = fita[i+2:len(fita)]
                        fita = ""
                        print("pp"+primeiraParte)
                        print("sp"+segundaParte)
                        print("p"+ponteiro)
                        break      

    print(fita)
    print(dictGrafo)
    print(sequencias)

#GA GC CCCGC ACCACGAGGTCACGAG
#GAGCCCGCCACCACGAGGTCACGAG

# ['CC', 'CG']
# {'CC': [['CC', ], [4, 4]], 'CG': [['GC'], [3, 3]], , [2, 2]]}

montaEuleriano(LinkedList, initial, k)

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
