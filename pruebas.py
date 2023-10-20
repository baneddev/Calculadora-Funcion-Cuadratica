
print(" ____  _   _  _____  ____  ____  _")
print("|  __|| | | ||  _  ||  _ ||  _ || |")
print("| |__ | |_| || |_| || |_||| |_||| |")
print("|____||_____||_| |_||____||_| |||_|")


#Te pide el valor de A,B y C para poder hacer los calculos
a = input("Ingrese el valor de A: ")
b = input("Ingrese el valor de B: ")
c = input("Ingrese el valor de C: ")

d1 = float(b) **2 -4 * float(a) * float(c)

x1 = (-float(b) + d1**0.5)/(2 * float(a))

d2 =  float(b) **2 -4 * float(a) * float(c)

x2 = (-float(b) - d2**0.5)/(2 * float(a))

print("x1 = " + str(x1))
print("x2 = " + str(x2))

xv = (x1 + x2)/2

print("xv = " + str(xv))

yv = float(a) * xv + float(b) * xv + float(c)
print("yv = " + str(yv))

print("Forma Factorizada: " + "y=" + str(a) + "*(x +" + str(x1) ")*(x-" str(x2) ")") 