#ESTE ES EL ARCHIVO PYTHON EN EL CUAL MIS COMPAÑEROS Y YO 
# TRABAJAREMOS PARA CREAR UNA CALCULADORA DE MANERA COLABORATIVA


#SUMATORIA
num1=int(input("Ingrese primer numero\n"))
num2=int((input("Ingrese segundo numero\n")))

def suma(num1,num2):
    sumar=num1+num2
    return(sumar)

print("La suma es :",suma(num1,num2))

#MULTIPLICACION
numa=int(input("Ingrese primer multiplo\n"))
numb=int(input("Ingrese segundo multiplo\n"))

def mult(numa,numb):
    multiplicar=numa*numb
    return multiplicar

print("El resultado es :",mult(numa,numb))

# RESTA
num1=int(input("Ingrese un numero:\n"))
num2=int(input("Ingrese el otro numero:\n"))

def restar(num1,num2):
    Resta=num1-num2
    return restar
print("El resultado total es: ", restar(num1,num2))


miau