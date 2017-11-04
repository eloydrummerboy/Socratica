# Scalene triangle: All sides have different lenghts.
# Isosceles triangle: Two sides have the same length.
# Equilateral triangle: All sides are equal.

a = int(raw_input("The length of side a = "))
b = int(raw_input("The lenght of side b = "))
c = int(raw_input("The lenght of side c = "))

if a != b and b != c and a != c:
  print("This is a scalene triangle.")
elif a == b and b == c:
  print("This is an Equilateral triangle.")
else:
  print("This is an isosceles triangle.")
