import random

#Informe o tamanho total da fita de dna:
bases = 1500

#Informe o tamanho do k:
k = 25

#Não precisa alterar o código a partir da linha
#---------------------------------------------------------------------------------------------------#

dna = []
mers = []
letras = "ACGT"
resposta = ""
if( k <= bases ):
    for x in range( bases ):
        dna.append( letras[random.randint(0,3)] )
    resposta = "".join( dna )
    bases = bases - k + 1
    control = 0
    for x in range( bases ):
        mers.append( resposta[control:control+k] + ",")
        control = control + 1
    
    mers.sort()
    mers = "".join(mers).replace(" ","").replace("[","").replace("]","").replace("'","")
    
file = open("input.txt","w")
file.write(mers)
file.close()
file = open("resposta.txt","w")
file.write(resposta)
file.close()
print("Feito!")