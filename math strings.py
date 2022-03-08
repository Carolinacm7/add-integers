#sumar enteros con string
#Annie C
def suma (a,b):
 c=a+b
 print ("{} esla suma de {}+{}".format(c,a,b))
suma(4,6)
#esta funcion divide dos numeros 
def divide (e,f):
 d=e/f
 print ("{} esla division de {}/{}".format(d,e,f))
divide(4,6)

""" #por medio del teclado saca una ventana emergente
 a = int(input())
 b = int(input())
 def division(a,b):
  c = a + b
  print(c)
  division (a,b) """
  

#multiplicacion para examen
""" 
def multiplicacion(x,y,z):
      d = x*y*z
      print(d)

    a = int(input())
    b = int(input())
    c = int(input())
    multiplicacion(a,b,c)
    multiplicacion(5, 6, 5) """
    
#algoritmo que determina el valor mayor para 3 valores dados
def mayor(a,b,c):
        if(a>b):
            if(a>c):
                print("{} es el mayor".format(a))
            else:
                print("{} es el mayor".format(c))
        else:
            if(b>c):
                print("{} es el mayor".format(b))
            else:
                print("{} es el mayor".format(c)) 


mayor(1,2,3)   
mayor(8,2,3)  
mayor(1,5,3)      