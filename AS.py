from segment_tree import SegmentTree 
  
# elementos de la matriz
arr = [23, 22, 32, 44, 50, 6, 79, 8, 9, 10] 

t = SegmentTree(arr) 
 
a = t.query(0, 9, "max")  
print("El valor máximo de este rango es: ", a) 
  
a = t.query(0, 9, "min")  
print("El valor mínimo de este rango es: ", a) 
  
a = t.query(0, 9, "sum")  
print("La suma de este rango es : ", a) 
  
t.update(0, 25)  
  
print("La matriz actualizada es : ", arr) 