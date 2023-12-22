#quebra em prefixo e sufixo

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

        
    return dictGraph
        
# acha codon inicial e final
def findInitialnFinal(dictGraph):
    initial = ""
    final = ""
    for key, value in dictGraph.items():
        if(value[1][0] > value[1][1]):
            initial = key
        elif(value[1][0] < value[1][1]):
            final = key
    if(initial != "" and final != ""):
        return initial, final

## abre arquivo

def abreArquivo(nome, modo):
    fita = ""
    with open(nome, modo) as file:
        fita += file.read()

    fita = fita.replace(' ', '')

    if(fita[-1] == ','):
        fita = fita[:-1]

    fita = fita.split(',')
    k = len(fita[0])

    return fita, k


#constroi grafo euleriano

def montaEuleriano(dictGrafo, initial, k, final):
    primeiraParte = ""
    segundaParte = ""

    fita = initial
    ponteiro = initial

    while(len(dictGrafo.keys())!=0):
        if(len(dictGrafo.get(ponteiro)[0]) > 0):
            remove = ponteiro
            ponteiro = dictGrafo.get(ponteiro)[0][0]
            fita += ponteiro[-1]
            dictGrafo[remove][0].remove(ponteiro)
            if(len(dictGrafo.get(remove)[0]) == 0):
                del dictGrafo[remove]
            try:
                if(dictGrafo.get(ponteiro)[0] == []):
                    del dictGrafo[ponteiro]
            except:
                pass
            if((dictGrafo.get(ponteiro) == None and len(dictGrafo.keys())>0)):
                while(len(dictGrafo.keys())!=0):
                    for i in range(0, len(fita)-1):
                        if(len(dictGrafo.keys())!=0):
                            atual = fita[i:i+k-1]
                            if(atual in dictGrafo.keys()):
                                primeiraParte = fita[0:i+k-1]
                                segundaParte = fita[i+k-1:len(fita)]
                                fitaAux = ""
                                ponteiro = dictGrafo.get(atual)[0][0]
                                while(ponteiro in dictGrafo.keys()):
                                    remove = ponteiro
                                    fitaAux += ponteiro[-1]
                                    ponteiro = dictGrafo.get(remove)[0][0]
                                    dictGrafo[remove][0].remove(ponteiro)
                                    if(len(dictGrafo.get(remove)[0]) == 0):
                                        del dictGrafo[remove]
                                fita = primeiraParte+fitaAux+segundaParte
                        else:
                            break
    return fita


#carrega arquivo
fita, k  = abreArquivo('exemplo.txt', 'r')

#constroi grafo
LinkedList = quebraPreSuf(fita,k)
initial, final = findInitialnFinal(LinkedList)
fitaFinal = montaEuleriano(LinkedList, initial, k, final)

#salva saida
with open("output.txt", "w") as arquivo:
    arquivo.write(fitaFinal)

