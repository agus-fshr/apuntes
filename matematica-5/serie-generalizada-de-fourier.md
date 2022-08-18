# Serie de Fourier
## Introduccion: Motivacion

Sea $x: \mathbb{R} \to \mathbb{K}$ periodica de periodo $T$.

Para $\sin(\frac{2 \pi k t}{T})$ hallar los valores $b_k$ tales que que la serie de Fourier aproxime a $x(t)$ lo mejor posible.

$$ S_n(t) = \sum_{k=1}^n b_k \sin({\frac{2 \pi k t}{T}}) $$

Comienzo por definir el error. Quiero hacer que sea el menor posible.

$$ H(b_1, b_2, b_3, ..., b_n) = \int_0^T[x(t) - S_n(t)]^2 dt $$

A esto que acabo de definir le tengo que buscar los puntos criticos, para quedarme con los minimos de la funcion. Por lo tanto, derivo con respecto a b_j.

$$ 0 = \frac{d}{db_j} \int_0^T[x(t) - S_n(t)]^2 dt $$

$$ 0 = \int^T_0 x(t)-\sum^n_{k=1}b_k \sin({\frac{2 \pi k t}{T}})(-2\sin({\frac{2 \pi k t}{T}})) dt $$

$$ 0 = -2 \int^T_0 x(t) \sin({\frac{2\pi j t}{T}}) dt + 2\sum^n_{k=1}b_k\int^T_0 \sin({\frac{2\pi kt}{T}})\sin({\frac{2\pi jt}{T}})$$

$$ 0 = -2 \int^T_0 x(t)\sin({\frac{2\pi jt}{T}}) + 2\frac{T}{2}b_j $$

$$ b_j = \frac{2}{T} \int^T_0 x(t)\sin({\frac{2\pi jt}{T}})$$


Todo esto tiene el objetivo de mostrar que son dos cosas distintas aproximar puntualmente que aproximar generalmente.

## Conceptos y Generalidades
La idea subyacente de las series generalizadas de Fourier es la de aproximar, no la de representar como sumatoria como si es en las series de Taylor. Para aproximar requerimos una nocion de lo que es la distancia, la norma, y para esto un producto interno. Entonces estamo trabajando en un K-espacio vectorial con producto interno.

Si imagino un subespacio $S_n = gen{\phi_1, \phi_2, ..., \phi_n}$ y un vector $v \notin \mathcal{V}$, aproximar a $v$ por proyeccion ortogonal al subespacio $S_n$ es lo mismo que hicimos antes con hallar los coeficientes de Fourier.

Lo que estoy buscando es que $<v - P_{S_n}(v), \phi_k> = 0$ para cada $k$ de la base del subespacio.

$$ P_{S_n}(v) = \sum_{k=1}^n C_k\phi_k $$

$$ <v-\sum_{k=1}^n C_k\phi_k, \phi_j> = 0 \forall j \Rightarrow C_j = \frac{<v, \phi_j>}{<\phi_j, \phi_j>} $$

# Definicion
(sin demostracion)

$$ C_k = \frac{<v, \phi_k>}{||\phi_k||^2} $$

$$ v \sim \sum^\infty_{k=1} C_k \phi_k $$

Nota: desigualdad de Bessel $$ ||v||^2 \leq \sum^\infty_{k=1} |C_k|^2 ||\phi_k||^2 $$

# Series de Fourier de Senales en Tiempo Discreto Periodicas

Supongamos alguna funcion $x: \mathbb{Z} \to K$ periodica de periodo $N$. Con $x$ tengo asociados ${x(0), x(1), ..., x(N-1)}$. Si pienso en $\mathcal{V}={x:{0,1,...,N-1} \to K}$

Puedo caracterizar a $x$ como la n-upla de su codominio, el cual pertenecera a $\mathbb{C}^N$.

$(\mathbb{C}^N, <,>)$ es un espacio de Hilbert, definiendo el producto interno $$ <a,b> = \sum_{k=0}^{N-1}a_kb_k^*$$
