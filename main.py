import math

A, B, C = input().split()
A, B, C = float(A), float(B), float(C)
delta = (B**2) - (4 * A * C)
raiz = math.sqrt(delta)
soma = -B - raiz
soma1 = -B + raiz
if A <= 0 or B <= 0 or C <= 0:
	print("R1 = {:.2f}".format(soma))
	print("R2 = {:.2f}".format(soma1))
