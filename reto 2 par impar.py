#Realice un programa que pida un número por pantalla y verifique si es par o imparPista: Utilice el operador de modulo (%) el cual retorna el residuo de la división entre un número y otro, si el resultado del residuo entre los dos números es cero quiere decir que la división fue exacta y el primer número es divisible entre el segundo.
print(" conoce si un numero es par o impar de otro numero".center(50,"*"))
print("===================================================")
a=int(input("digite el numero a consultar: "))
b=int(input("digite numero a consultar paridad: "))
a=a % b
print(a)
if a == 0:
  print("es par")
else:
  print(" es impar")