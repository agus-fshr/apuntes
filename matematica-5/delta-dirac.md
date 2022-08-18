# El Problema de la Division

Dada una funcion generalizada $f(t)$ y una funcion analitica $g(t)$ hallar una funcion generalizada $x(t)$ tal que $g(t)x(t) = f(t)$

Planteo $g(t)x(t) = 0$ y veo que puede haber diferentes casos

1. $g$ tiene un unico cero de orden $n$ en $t_0$

$$ \Rightarrow x(t) = \sum_{k=0}^{n-1} C_k \delta^{(n)}(t-t_0) $$

2. $g$ tiene ceros $t_k$ de orden $n_k$ y $\nexists \lim_{k \to \pm \infty} t_k$

$$ x(t) = \sum_{k \in \mathbb{Z}}x_k(t) $$
$$ x_k(t) = C_k \delta^{(n_k - 1)}(t-t_0) $$

*esta parte esta dudosa, seria mejor leer los archivos de Rafa*

## Ejemplo

Resolver el problema de la division para $(t^2-4)x(t) = 4 \delta^{\prime\prime}(t-3)$

1. Solucion general de la homogenea
$$ (t^2-4)x_k(t) = 0 $$

Los ceros son $t_1 = 2$; $n_1 = 1$ y $t_2 = -2$; $n_2 = 1$. Entonces
$$ x_k(t) = A\delta(t-2) + B\delta(t+2) $$

Para resolver la particular, propongo $x_p$ como una combinacion lineal de derivadas de $\delta(t)$

Nota: $h(t)\delta^{\prime}(t-t_0) = h(t_0)\delta^{\prime}(t-t_0) - h^{\prime}(t_0)\delta(t-t_0)$

Generalizado, $$<h(t)\delta^{(n)}(t-t_0), \phi(t)> = <\delta^{(n)}(t-t_0), h(t)\phi(t)>$$
$$ <\delta^{(n)}(t-t_0), h(t)\phi(t)> = (-1)^n <\delta(t-t_0), (h(t)\phi(t))^{(n)}> $$
$$  (h(t)\phi(t))^{(n)} = \sum^{n}_{k=0} nCk (-1)^{n-k}h^{n-k}(t) \delta^{(k)}(t-t_0)$$

Volviendo a la resolucion del ejemplo...

$$x_p = C\delta^{\prime\prime}(t-3) + D\delta(t-3) + E\delta^{\prime}(t-3)$$

Ahora me queda calcular $h(t)$ por cada uno de esos terminos usando el resultado que anote arriba para calcular el producto de $h(t)$ por las sucesivas derivadas de $\delta$. No lo escribo porque es muy cuentoso.
