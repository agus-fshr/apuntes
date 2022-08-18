# Demanda

## Supply Chain

### Compras

Gestion del aprovisionamiento de insumos y servicios.

### Planning

Planificacion de la demanda, de la produccion y del aprovisionamiento de materiales.

### Manufactura

Fabricacion de los bienes producidos por la empresa.

### Logistica

Almacenamiento y distribucion de los bienes producidos por la empresa.

## Que es el pronostico de la demanda

Es la prediccion de compotamientos futuros de la demanda tomando como base informacion historia. Es fundamental para planificar todas las actividades del negocio (ventas, financieras, operativas, recursos, materiales).

## Pronosticos en la Organizacion

Origina en el marketing porque esta es el area mas cercana a los clientes. Es una parte crucial de los planes de negocios y presupuestos.

El area de finanzas necesita de los pronosticos para proyectar los flujos de efectivo y necesidades de capital.

RRHH lo necesita para prever las necesidades de contratacion y capacitacion de personal.

Operaciones lo necesita para planear los niveles de produccion, compra de servicios y materiales, mano de obra, etc...

## Horizontes de Tiempo

El pronostico de la demanda afecta de maneras distintas a distintas areas de la empresa. Para estudiar como lo hace solemos hablar de 3 plazos de tiempo distintos.

### El Corto Plazo
(menos de 3 meses)
Ventajas de productos individuales. Habla de cuestiones operativas.

### Mediano Plazo
(entre 3 y 18 meses)
Aca se habla de tacticas.
Buscamos estimar ventas de familias de productos (productos agrupados)

### Largo Plazo
(entre 18 meses y 3 anos)
Aca se habla de estrategia de la empresa.

## Horizonte Temporal de los Pronosticos

## Tipos de Pronosticos

### Cualitativos

Se basan en experiencias y opiniones.

#### Jurado/Opinion Ejecutiva

Se basa en la experiencia y conocimientos tecnicos de los altos mandos de la empresa para llegar a un consenso a fin de generar un pronostico

#### Metodo Delphi

Es un proceso iterativo con ciertas reglas mediante el cual se pretende maximizar las ventajas del metodo ejecutivo y respetar el anonimato de sus integrantes.

#### Pronostico del Equipo Comercial - Estimaciones del Personal de ventas

Se agrupa el equipo comercial y revisan la estimacion de ventas esperada y luego se obtiene un pronostico global. Hay que ser cuidadoso con los intereses.

#### Estudio de Mercado

Requiere informacion de los clientes, sobre sus intenciones futuras de compra, preferencias, necesidades, precios maximos, etc...

### Cuantitativos

Se basan en informacion y modelos matematicos.

#### Series de Tiempo

Las obervaciones repetidas de la demanda de un producto o servicio en el orden en que se realizan forman un patron que se conoce como serie de tiempo. Los modelos de series de tiempo predicen bajo la suposicion de que el futuro es una funcion del pasado. Se basa en una secuencia de datos puntuales separados a intervalos iguales.

Puede presentar 5 factores o componentes fundamentales:
- Horizontal: la fluctuacion de los datos en torno de una media constante
- Tendencia: el incremento o decremento sistematico de la media de la serie a traves del tiempo
- Estacional: un patron repetible de incrementos o decrementos de la demanda, dependencia de la hora del dia, la semana, el mes, la temporada.
- Ciclico: una pauta de incrementos o decrementos graduales y menos previsibles de la demanda, los cuales se presentan en el transcurso de periodos mas largos. Esta mas relacionado con ciclos economicos de un pais o del ciclo de vida del producto del ciclo de vida del producto del ciclo de vida del producto del ciclo de vida del producto
- Aleatorio: la variacion imprevisible de la demanda

Las componentes horizontal, de tendencia, estacional y ciclica se combinan en diversos grados para definir el patron fundamental de tiempo de demanda. El quinto, la aleatoriedad, es impredecible y, por lo tanto, no puede pronosticarse. Es un aspecto de la demanda por el que todos los pronosticos resultan equivocados.

# Series de tiempo

## Media Movil

Trabaja con promedios moviles. Esto es la media de las demandas de periodos anteriores. En general, es recomendable si no hay tendencia. Responde mas rapido antes cambios cuanto mas pequeno sea el numero $N$ de periodos considerado.

$$ MM = \frac{\sum (\text{demanda de periodos anteriores})}{N} $$

Tambien se pueden usar promedios moviles ponderados. Estos se utilizan cuando se desea dar mayor peso a los datos mas recientes. Generalmente, cuando hay una tendencia en la serie de tiempo.

$$ MMP = \frac{\sum (\text{ponderacion para el periodo }n)(\text{demanda en el periodo }n)}{\sum \text{ponderaciones}} $$

La gran desventaja de este modelo es que al aumentar el numero de periodos estudiados, disminuye la sensibilidad a los cambios.

## Suavizamiento Exponencial

Es un caso especial de pronostico de media movil ponderada, donde ahora los factores de ponderacion disminuyen exponencialmente, dandole mas peso a periodos recientes.

Para esto se necesita una constante de alisado ($a$), que se elige de forma subjetiva. Varia entre cero y uno.

Lo que tiene de bueno es que necesita una cantidad reducida de datos historicos.

$$ \text{Nuevo Pronostico }= \text{ pronostico del periodo anterior } + a text{ (demanda real del periodo anterior - pronostico del periodo anterior)} $$

$$ F_t = F_{t-1} + a(D_{t-1}-F_{t-1}) $$

Para demandas con mucha variacion, son mas efectivos los valores de $a$ altos. Asi el pronostico da mayor importante a la demanda reciente.

## Holt-Winters

## Estacionalidad

No hay metodo de pronostico para la estacionalidad. Si se puede estacionalizar el pronostico.

1. Para cada ano, se calcula la demanda promedio por estacion
2. Para cada ano, se divide la demanda real correspondiente a una estacion sobre la demanda promedio por estacion obtenida en el paso 1.
3. Calcular el indice estacional promedio para cada estacion usando los resultados del paso 2. Hay que sumar los indicies estacionales de cada ano para cada estacion y dividirlos sobre el numero de anos que abarquen datos.
4. Estimar la demanda anual de todo el ano proximo utilizando el metodo que considere apropiado.
5. Dividir la demanda de todo el ano sobre el numero de estacion y luego multiplicarlo por el indice estacional promedio.

## Regresion Lineal

El objetivo del analisis de regresion lineal es pronosticar la demana a partir de una o mas causas. Para tratar la relacion entre la demanda y la variable independiente vamos a hacer uso de un coeficiente de correlacion $r$.

Si este se acerca a $1$ o a $-1$, podremos afirmar que se trata de una relacion fuerte.

# Error de Pronostico

Si el objetivo es analizar que tan bien han sido hechos los pronosticos, podemos trabajar con **errores de pronosticos**. Son calculos de desviacion en el tiempo con relacion a la demanda real.

## Error Acumulado (CFE)

$$ \text{CFE } = \sum (D_t - F_t) $$

## Error Absoluto Medido (MAD)

Mide la dispersion dl error de pronostico o dicho de otra forma, la medicion del tmano del error en unidades. Es el valor absoluto de la diferencia entre la demanda real y el pronostico, dividido sobre el numero de periodos.

$$ \text{MAD}=\frac{\sum |\text{Real - Pronostico}|}{n} $$

## Error Cuadratico Medio (MSE)

Este, castiga aquellos periodos donde la diferencia fue mas alta a comparacion de otros.

$$\text{MSE} = \frac{\sum (\text{Errores de pronostico})^2}{n}$$

## Error absoluto porcentual medio

Es el mejorcito, pero esta mal la formula asi que despues la agrego.

## Errores de Pronostico

### Senal de Rastreo

Para monitorear pronosticos. Se utiliza el concepto de TS: nos permite detectar cuando un metodo esta dejando de ser confiable. Si los errores es dispersan en forma aleatoria, no hay nada mal con el metodo.

Se suele fijar el limite de $\pm 3,75$ como limite de una senal de rastreo.

Falta la formula de senal de rastreo aca.


















# Kahoot

1. Cuantos metodos cuantitativos damos -> 4
2. Cosas que bajan y suben -> tendencia
3. Cuantas cosas afectan la exponencial -> 5
4. Cuantos periodos se tienen en cuenta -> corto medio y largo plazo
