# Ordenamiento
El objetivo de ordenar cualquier cosa es ahorrar tiempo en el momento de la busqueda. Un problema muy comun es hallar la manera de ordenar una secuencia de elementos por su clave.

Una condicion para poder ordenar cosas es que sean comparables. El diseno de la **funcion de comparacion** puede ser sutil, como el ordenamiento por nombres de archivo. Ademas de una funcion de comparacion se necesita una **funcion de swap**, es decir, una funcion que intercambie las posiciones de dos elementos. El cuello de botella puede encontrarse en cualquiera de estas dos funciones. Por ejemplo, si estoy escribiendo sobre una memoria muy lenta, podria tener un cuello debotella en el swap.

Se dice que un algoritmo de ordenamiento es **estable** cuando no cambia el orden relativo de los elementos de igual clave. Tambien se puede ver omo que se respeta el _orden de llegada_ a la funcion.


## Algoritmos de Ordenamiento
### Bubble Sort
Es uno de los algoritmos mas ineficientes que existen. Burbujea los valores mas altos hasta el final del arreglo. Tiene una complejidad en tiempo de $O(n^2)$. En memoria tiene una complejidad de $O(1)$ ya que el ordenamiento es in-situ.

