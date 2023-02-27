fita = ""

with open("exemplo.txt", 'r') as file:
    fita += file.read()


fita = fita.replace(' ', '')

if(fita[-1] == ','):
    fita = fita[:-1]

fita = fita.split(',')
print(fita)

def mountGraph(dnaFita):
    pass