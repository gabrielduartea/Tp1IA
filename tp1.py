import copy


def imprimev(visitados):
  print(visitados[0],"\n")
  print(visitados[1],"\n")
  print(visitados[2],"\n")


def verificar(matriz):
  aux=False
  cont=0
  if matriz[0][0]==1:
    cont=cont+1
  if matriz[0][1]==2:
    cont=cont+1
  if matriz[0][2]==3:
    cont=cont+1 
  if matriz[1][0]==4:
    cont=cont+1     
  if matriz[1][1]==5:
    cont=cont+1
  if matriz[1][2]==6:
    cont=cont+1
  if matriz[2][0]==7:
    cont=cont+1
  if matriz[2][1]==8:
    cont=cont+1
  if matriz[2][2]==0:
    cont=cont+1 
  if cont==9:
    aux=True
  return aux         
        
def imprime(matriz): 
  
  print(matriz[0])
  print(matriz[1])
  print(matriz[2],"\n")
  


def busca_largura(matriz):
  fila = []
  visitados=[]
  fila.append(matriz) 
  num=0
  while(len(fila)!=0):
    no = fila.pop(0) 
    num=num+1
    
   
    if no not in visitados:
      visitados.append(no)
      imprime(no)
    
      
      if verificar(no) == True:
        print("\n** Você chegou a solução!  ***]\n","Número de nós expandidos=",num)
        visitados.append(no)
        
        
        imprime(no)
        break;
      else:
        
        filho = jogar(no,aresta)
        for n in filho:
          fila.append(n)
        
def busca_profundidade_limitada(matriz):
  pilha = []
  visitados=[]
  
  pilha.insert(0,matriz) 
  num=0
  limitador=0
  
  while(len(pilha)!=0 and limitador<100000):
    no = pilha.pop(0) 
    num=num+1
    imprime(no)
    limitador=limitador+1
    if no not in visitados:
      visitados.append(no)
      
    
    
      if verificar(no) == True:
        print("\*n** Você chegou a solução!  ***]\n","Número de nós expandidos=",num)
        visitados.extend(no)
        
        
        
        imprime(no)
        break;
      else:
        
        filho = jogar(no,aresta)
        for n in filho:
          pilha.insert(0,n)
          


  





def jogar(matriz,aresta):

    trocas=[]

    if matriz[0][0]==aresta:
    
      aux = copy.deepcopy(matriz) 
      aux[0][0] = aux[1][0]
      aux[1][0] = aresta
    
    
      trocas.append(aux)
   
      aux = copy.deepcopy(matriz) 
      aux[0][0] = aux[0][1]
      aux[0][1] = aresta
    
    
      trocas.append(aux)
 
   
    elif matriz[0][1]==aresta:

      aux = copy.deepcopy(matriz) 
      aux[0][1] = aux[1][1]
      aux[1][1] = aresta
    
    
      trocas.append(aux)
    
      aux = copy.deepcopy(matriz) 
      aux[0][1] = aux[0][0]
      aux[0][0] = aresta
    
    
      trocas.append(aux)
    
      aux = copy.deepcopy(matriz) 
      aux[0][1] = aux[0][2]
      aux[0][2] = aresta
    
    
      trocas.append(aux)
   
    elif matriz[0][2]==aresta:
 
      aux = copy.deepcopy(matriz) 
      aux[0][2] = aux[1][2]
      aux[1][2] = aresta
    
    
      trocas.append(aux)
    
      aux = copy.deepcopy(matriz) 
      aux[0][2] = aux[0][1]
      aux[0][1] = aresta
    
    
      trocas.append(aux)
   
    elif matriz[1][0]==0:
  
      aux = copy.deepcopy(matriz) 
      aux[1][0] = aux[0][0]
      aux[0][0] = aresta
    
    
      trocas.append(aux)
  
      aux = copy.deepcopy(matriz) 
      aux[1][0] = aux[2][0]
      aux[2][0] = aresta
    
    
      trocas.append(aux)
  
      aux = copy.deepcopy(matriz) 
      aux[1][0] = aux[1][1]
      aux[1][1] = aresta
    
    
      trocas.append(aux)
   
   
    elif matriz[1][1]==aresta:
    
      aux = copy.deepcopy(matriz) 
      aux[1][1] =  aux[0][1]
      aux[0][1] = aresta
    
     
      trocas.append(aux)

      aux = copy.deepcopy(matriz) 
      aux[1][1] = aux[1][0]
      aux[1][0] = aresta
    
    
      trocas.append(aux)

      aux = copy.deepcopy(matriz) 
      aux[1][1] = aux[1][2]
      aux[1][2] = aresta
    
    
      trocas.append(aux)
 
      aux = copy.deepcopy(matriz) 
      aux[1][1] = aux[2][1]
      aux[2][1] = aresta
    
    
      trocas.append(aux)
   
   
    elif matriz[1][2]==0:
  
      aux = copy.deepcopy(matriz) 
      aux[1][2] = aux[0][2]
      aux[0][2] = aresta
    
    
      trocas.append(aux)
  
      aux = copy.deepcopy(matriz) 
      aux[1][2] = aux[2][2]
      aux[2][2] = aresta
    
    
      trocas.append(aux)
  
      aux = copy.deepcopy(matriz) 
      aux[1][2] = aux[1][1]
      aux[1][1] = aresta
    
    
      trocas.append(aux)
    
    
    
  
    elif matriz[2][0]==aresta:
    
      aux = copy.deepcopy(matriz) 
      aux[2][0] = aux[1][0]
      aux[1][0] = aresta
    
    
      trocas.append(aux)
    
      aux = copy.deepcopy(matriz) 
      aux[2][0] = aux[2][1]
      aux[2][1] = aresta
    
    
      trocas.append(aux)
  
    elif matriz[2][1]==aresta:

      aux = copy.deepcopy(matriz) 
      aux[2][1] = aux[1][1]
      aux[1][1] = aresta
    
    
      trocas.append(aux)
    
      aux = copy.deepcopy(matriz) 
      aux[2][1] = aux[2][0]
      aux[2][0] = aresta
    
    
      trocas.append(aux)
    
      aux = copy.deepcopy(matriz) 
      aux[2][1] = aux[2][2]
      aux[2][2] = aresta
    
    
      trocas.append(aux)
    
    elif matriz[2][2]==aresta:
    
      aux = copy.deepcopy(matriz) 
      aux[2][2] = aux[1][2]
      aux[1][2] = aresta
    
    
      trocas.append(aux)
    
      aux = copy.deepcopy(matriz) 
      aux[2][2] = aux[2][1]
      aux[2][1] = aresta
    
    
      trocas.append(aux)
  
    return trocas

print("Digite a sequencia desejada para iniciar o jogo, o '0' representa a opçao vazia!")

a=int(input("Digite o primeiro numero:"))
b=int(input("Digite o segundo numero:"))
c=int(input("Digite o terceiro numero:"))
d=int(input("Digite o quarto numero:"))
e=int(input("Digite o quinto numero:"))
f=int(input("Digite o sexto numero:"))
g=int(input("Digite o setimo numero:"))
h=int(input("Digite o oitavo numero:"))
i=int(input("Digite o nono numero:"))

matriz=[
    [a,b,c],
    [d,e,f],
    [g,h,i],
  
    
    
]
 
 
 


aresta=0   
    



aresta=0
op = int(input('Informe uma opção de busca:\n1-busca em largura.\n2-busca em profundidade limitada\n'))
if(op==1):
  busca_largura(matriz)
elif(op==2):
  busca_profundidade_limitada(matriz)   

