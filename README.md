reto: ¿Qué vendedor genera más dinero?
Aprenderemos
merge() → conectar datos groupby() + agg() → resumir y analizar Columnas derivadas → crear indicadores
PASO 1 — Tenemos los vendedores
PASO 2 — Tenemos los productos vendidos
PASO 3 — Conectamos las tablas
Explícalo así:
"La primera tabla sabe quién es el vendedor. La segunda sabe qué producto vendió. El id es nuestro puente."
merge() = conectar información.
PASO 4 — Creamos un nuevo indicador
Ahora preguntamos:
¿Cuánto dinero generó cada venta?
Obtendremos:
vendedor
producto
cantidad
precio
total
Sofía
Audífonos
2
$120.000
$240.000
Mateo
Smartwatch
1
$350.000
$350.000
Sofía
Teclado Gamer
3
$180.000
$540.000
Valentina
Cámara Web
2
$250.000
$500.000
Mateo
Mouse Gamer
4
$90.000
$360.000
La explicación:
"La columna total no existía. La construimos utilizando cantidad × precio. Por eso es una columna derivada."
Columna derivada = crear información nueva a partir de datos existentes. PASO 5 — Analizamos por vendedor
Ahora el gerente pregunta:
¿Cuánto dinero generó cada vendedor?
Resultado:
vendedor
ventas_totales
promedio_venta
Sofía
$780.000
$390.000
Mateo
$710.000
$355.000
Valentina
$500.000
$500.000
Y AQUÍ VIENE EL RETO
Diles a los estudiantes:
"El gerente ahora quiere saber cuál fue el producto que tuvo el precio más alto en cada vendedor. ¿Qué debemos agregar al agg()?"
La respuesta:
LA IDEA QUE DEBEN RECORDAR
