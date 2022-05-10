# 7. Arboles
Un arbol es un conjunto de nodos organizados segun una jerarquia. Si contiene al menos un nodo, entonces debe tener un _nodo raiz_. Este es el nodo de nivel mas alto, a partir de este naces los demas. Es el nivel mas alto de jerarquia. Todos los nodos del arbol estan unidos al nodo raiz mediante algun camino.

Los nodos pueden tener mutiples nodos hijos, pero solamente un nodo padre. El vinculo entre dos nodos se llama _brazo_. En los arboles se definen _nodo hermano, ancestro_ y _descendiente_. Sus definiciones son analogas a los arboles genealogicos.

Un nodo sin hijos se llama _hoja_. Un nodo con hijos se llama _nodo interno_. El nivel de un nodo es el  numero de brazos entre el nodo y la raiz, mas uno. La altura de un arbol no vacio es el numero de brazos en el camino mas largo entre el nodo raiz y una hoja. Si no tiene brazos, se dice que tiene altura 0. Si no tiene nodos, se dice que tiene altura -1.

A partir de un nodo dentro de u n arbol, se puede definir un _sub-arbol_. Este conocimiento me da la idea de que puede ser muy potente trabajar los arboles de manera recursiva.

## Codear arboles
Podemos representar los nodos de los arboles con un elemento y una lista de punteros a nodos hijo. Para lograr mejor eficiencia de memoria, esta lista se puede crear con un `vector`.
```C++
template <class T>
class Treenode
{
	public:
		T value;
		vector<TreeNode<T> *> children;
};
```
![[vector-tree.png]]
Asi es como se ve un arbol hecho con `vector`. Con `list`, todos los elementos quedan asociados por punteros. Como ya se dijo, sera mucho mas eficiente en insercion y eliminacion de nodos, pero ocupa mas memoria.

Se pueden representar los nodos con un elemento y dos punteros; uno al primer hijo por izquierda y, otro, el siguiente hermano por derecha.
```C++
template <class T>
class TreeNodeB
{
public:
	TreeNodeB<T> *firstChild;
	TreeNodeB<T> *nextSibling;
};
```
![[list-tree.png]]
Se pueden crear arboles estrictamente binarios o `Quadtrees` u `Octrees` con expresiones como `(TreeNode<T> *[4]child)` para el segundo caso. La cantidad de hijos en este tipo de arboles es acotada superiormente.

## Recorrido de arboles
Un *recorrido* involucra visitar cada uno de los nodos de manera sistematica. La *visita* involucra algua operacion sobre un nodo, procesarlo, modificarlo, mandarlo a disco.

### Recorrido DFS
En un recorrido _depth-first search_ se visitan todos los nodos recursivamente, entrando primero en profundidad. Para la recursion de este recorrido se una una pila.
```C++
void traverseDFS(TreeNode *node)
{
	if (node == NULL)
		return;
	
	visitPreorder(node);
	
	for (auto childNode : node->children)
		traverseDFS(childNode);
	
	visitPostorder(node);
}
```
En este caso la recursion de realiza en el call stack, pero tambien se podria usar un `stack` de STL. Hay que tener cuidado, con el call stack, de no sobrepasar el stack cuando el arbol sea muy grande. De lo contrario, puede ocurrir un stack overflow.
![[tree.png]]
Para este arbol, el recorrido DFS pre-orden resulta: `ABDCEGFHI`
El recorrido DFS post-orden es: `DBGEHIFCA`

En el recorrido pre-orden se recorre el arbol por subarboles, primero por izquierda y luego por derecha. Se devuelve un nodo cuando se lo alcanza por primera vez. Cuando meto un nodo al call stack lo imprimo, y luego los elimino del call stack para seguir visitando.

En el recorrido post-orden se hace lo mismo pero se devuelve el nodo cuando se lo visita por ultima vez. Primero meto los nodos en el call stack, luego, cuando no tienen mas hijos los visito. Tambien esta el recorrido in-order, que devuelve el nodo cuando se lo visita por segunda vez.

Para las hojas, es util plantear que tienen dos subarboles vacios.

### Recorrido BFS
El _breadth-first search_ visita todos los nodos iterativamente, entrando en anchura. Se comienza por el nodo raiz, bajando nivel por nivel hasta cubrir todo al arbol. Esta iteracion se reliza con una cola, por ejemplo, un `queue` de STL.
```C++
void traverseBFS(TreeNode *root)
{
	if (root == NULL) 
		return;
	
	queue q;
	q.push(root);
	while (!q.empty())
	{
		TreeNode *node = q.pop();
		
		visit(node);
		f (root == NULL) return; queue q; q.push(root); while (!q.empty()) { TreeNode *no
		for (auto childNode : node->children)
			q.push(childNode);
	}
}
```
El nodo se puede visitar cuando se pushea o cuando se popea. Generalmente es mas facil hacerlo cuando se popea.

Para el mismo arbol que se mostro antes el recorrido BFS es: `ABCDEFGHI`
Cuando llego a un nodo, encolo sus hijos. Luego, cuando desencolo un hijo, encolo los hijos de ese.

## Arboles binarios de busqueda
Un arbl binario de busqueda es un arbol binario en el que cada nodo posee un valor llamado _clave_ La clase es unica, no se repite entre nodos. La clave de cada nodo es mayor a la de su subarbol izquierdo y mayor a la de su subarbol derecho.
