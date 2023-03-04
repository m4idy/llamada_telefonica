print("...................................................................")
print("......................llamada telefonica...........................")
print("...................................................................")


# imput 

n=int(input("digite el tiempo de su llamada: "))
E= 300



# output


if n<3 :

    rta= ("el costo de su llamada es: "  + str (E))

   
else: 
     
     T= (n-3)
     A= (T*50)
     Y= (E+A)
     rta = "el costo de su llamada es: " + str(Y)

print( str (rta))