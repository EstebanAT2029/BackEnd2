#Lista (Arreglo)
# Modificable y ordenada
numeros_de_emergencia = ["104", "980874153","979503242", "051352200"]

print(numeros_de_emergencia)
print(numeros_de_emergencia[0])

longitud_numeros = len(numeros_de_emergencia)
print(numeros_de_emergencia[longitud_numeros-1])
#si queremos recorrer la lista de derecha a izquierda podemos usar valores negativos
print(numeros_de_emergencia[-1])
#si yo quiero hacer una sub lista de la lista
#pos_inicio:            > desde la pos inicial hasta el final
#pos_inicio: pos_final  > desde la pos inicial hasta la menor que la pos final
# :pos_final            > desde el inicio hasta la pos final
print(numeros_de_emergencia[2:])
print(numeros_de_emergencia[1:3])
print(numeros_de_emergencia[:2])

##Agregar o Quitar listas
numeros_de_emergencia.append("9808741522")
numeros_de_emergencia.append("981612634")
print(numeros_de_emergencia)

#Remueve el elemento de la vista y los siguientes elementos ocupan su lugar
numero_eliminado = numeros_de_emergencia.pop(3)
print(numero_eliminado)
print(numeros_de_emergencia) 
# del > delete
del numeros_de_emergencia[3]
print(numeros_de_emergencia)
