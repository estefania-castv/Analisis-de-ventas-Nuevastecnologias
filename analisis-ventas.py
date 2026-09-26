import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# 🚀 MASTERCLASS: UNIÓN, AGREGACIÓN Y COLUMNAS DERIVADAS
# ============================================================

print("=" * 70)
print("       📊 ANÁLISIS DE VENTAS DE UNA TIENDA")
print("=" * 70)


# ============================================================
# 1️⃣ DATOS DE VENDEDORES
# ============================================================

vendedores = pd.DataFrame({
    "id": [1, 2, 3],
    "vendedor": [
        "Sofía",
        "Mateo",
        "Valentina",
    ],
    "ciudad": [
        "Medellín",
        "Bogotá",
        "Cali",
    ]
})

print("\n👥 TABLA DE VENDEDORES")
print(vendedores)


# ============================================================
# 2️⃣ DATOS DE VENTAS
# ============================================================

ventas = pd.DataFrame({
    "id": [1, 2, 1, 3, 2],
    "producto": [
        "Audífonos",
        "Smartwatch",
        "Teclado Gamer",
        "Cámara Web",
        "Mouse Gamer",
    ],
    "cantidad": [2, 1, 3, 2, 4],
    "precio": [
        120000,
        350000,
        180000,
        250000,
        90000,
    ]
})

print("\n🛒 TABLA DE VENTAS")
print(ventas)


# ============================================================
# 3️⃣ COLUMNA DERIVADA: TOTAL DE LA VENTA
# ============================================================

ventas["total"] = ventas["cantidad"] * ventas["precio"]

print("\n💰 COLUMNA DERIVADA: TOTAL")
print(ventas)


# ============================================================
# 4️⃣ MERGE INNER
# ============================================================

print("\n" + "=" * 70)
print("🔗 1. MERGE INNER")
print("=" * 70)

ventas_completas = pd.merge(
    vendedores,
    ventas,
    on="id",
    how="inner"
)

print(ventas_completas)


# ============================================================
# 5️⃣ MERGE LEFT
# ============================================================

print("\n" + "=" * 70)
print("🔗 2. MERGE LEFT")
print("=" * 70)

ventas_left = pd.merge(
    vendedores,
    ventas,
    on="id",
    how="left"
)

print(ventas_left)


# ============================================================
# DIFERENCIA INNER vs LEFT
# ============================================================

print("""
💡 INNER:
   Conserva únicamente los registros que tienen coincidencia
   en las dos tablas.

💡 LEFT:
   Conserva TODOS los registros de la tabla izquierda
   y busca información en la tabla derecha.

🎯 IDEA PARA LOS ESTUDIANTES:

INNER = "Dame solamente los que coinciden"

LEFT  = "No me borres ninguno de la izquierda"
""")


# ============================================================
# 6️⃣ GROUPBY
# ============================================================

print("\n" + "=" * 70)
print("📦 3. GROUPBY: ¿CUÁNTO VENDE CADA VENDEDOR?")
print("=" * 70)

ventas_vendedor = ventas_completas.groupby(
    "vendedor"
)["total"].sum()

print(ventas_vendedor)


# ============================================================
# 7️⃣ GROUPBY + AGG
# ============================================================

print("\n" + "=" * 70)
print("📊 4. GROUPBY + AGG")
print("=" * 70)

resumen_vendedores = ventas_completas.groupby(
    "vendedor"
).agg(
    ventas_totales=("total", "sum"),
    promedio_venta=("total", "mean"),
    cantidad_productos=("cantidad", "sum"),
    ventas_realizadas=("producto", "count"),
    venta_maxima=("total", "max"),
)

print(resumen_vendedores)


# ============================================================
# 8️⃣ COLUMNA DERIVADA: TICKET PROMEDIO
# ============================================================

resumen_vendedores["ticket_promedio"] = (
    resumen_vendedores["ventas_totales"]
    / resumen_vendedores["ventas_realizadas"]
)

print("\n" + "=" * 70)
print("💳 5. COLUMNA DERIVADA: TICKET PROMEDIO")
print("=" * 70)

print(resumen_vendedores)


# ============================================================
# 9️⃣ RANKING DE VENDEDORES
# ============================================================

resumen_vendedores["ranking"] = (
    resumen_vendedores["ventas_totales"]
    .rank(
        ascending=False,
        method="dense"
    )
    .astype(int)
)

print("\n" + "=" * 70)
print("🏆 6. RANKING DE VENDEDORES")
print("=" * 70)

ranking = resumen_vendedores.sort_values(
    "ranking"
)

print(ranking)


# ============================================================
# 🔟 PARTICIPACIÓN EN LAS VENTAS
# ============================================================

total_empresa = resumen_vendedores["ventas_totales"].sum()

resumen_vendedores["participacion_%"] = (
    resumen_vendedores["ventas_totales"]
    / total_empresa
    * 100
)

print("\n" + "=" * 70)
print("📈 7. PARTICIPACIÓN EN LAS VENTAS")
print("=" * 70)

print(
    resumen_vendedores[
        [
            "ventas_totales",
            "participacion_%"
        ]
    ]
)


# ============================================================
# 1️⃣1️⃣ RETO DEL PDF: PRODUCTO CON PRECIO MÁS ALTO POR VENDEDOR
# ============================================================

print("\n" + "=" * 70)
print("🏅 8. PRODUCTO CON PRECIO MÁS ALTO POR VENDEDOR")
print("=" * 70)

idx_precio_max = ventas_completas.groupby("vendedor")["precio"].idxmax()

producto_top = ventas_completas.loc[
    idx_precio_max,
    ["vendedor", "producto", "precio"]
].set_index("vendedor")

print(producto_top)

resumen_vendedores["producto_top"] = producto_top["producto"]
resumen_vendedores["precio_top"] = producto_top["precio"]


# ============================================================
# 1️⃣2️⃣ RESULTADO FINAL
# ============================================================

print("\n" + "=" * 70)
print("🎯 RESULTADO FINAL PARA LA GERENCIA")
print("=" * 70)

resultado = resumen_vendedores.sort_values(
    "ventas_totales",
    ascending=False
)

print(resultado)


# ============================================================
# 1️⃣3️⃣ MENSAJE FINAL
# ============================================================

vendedor_top = resultado.index[0]
venta_top = resultado.iloc[0]["ventas_totales"]

print("\n" + "=" * 70)
print("💡 INSIGHT")
print("=" * 70)

print(
    f"El vendedor con mayor volumen de ventas es {vendedor_top}, "
    f"con ventas por ${venta_top:,.0f}."
)

print("""
🎓 LO IMPORTANTE:

merge()
   ↓
UNIR información

groupby()
   ↓
AGRUPAR información

agg()
   ↓
RESUMIR información

Columnas derivadas
   ↓
CREAR nuevos indicadores

idxmax()
   ↓
ENCONTRAR el registro máximo dentro de cada grupo

rank()
   ↓
COMPARAR y ordenar

📊 DATOS → INFORMACIÓN → INSIGHT → DECISIÓN
""")


# ============================================================
# 1️⃣4️⃣ GRÁFICA DE VENTAS POR VENDEDOR
# ============================================================

plt.figure(figsize=(8, 5))
plt.bar(resultado.index, resultado["ventas_totales"], color="skyblue")
plt.title("Ventas totales por vendedor")
plt.xlabel("Vendedor")
plt.ylabel("Ventas totales ($)")
plt.tight_layout()
plt.show()