x = int(input("Input X"))

a = int(input("Input a"))
b = int(input("Input b"))
c = int(input("Input c"))



D =b**2 - 4 * a * c

if D > 0:
  print("x1 = " + (-b+math.sqrt(D))/2 * a) + " x2 = " + (-b - math.sqrt(D)/ 2 * a)
elif D == 0:
  print("x = " + (-b)/2*a)
else:
  print("none solution")
	
