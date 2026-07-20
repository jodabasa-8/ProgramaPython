
# ---------------------------------------------------------
# Nombre del estudiante: Jose David Barrera Salgado
# Programa: Ingeniería de Sistemas
# Curso: Fundamentos de Programación (213022)
# Código Fuente: Autoría Propia
# Problema Seleccionado: Problema 2 - Fase 5 (POA)
# ---------------------------------------------------------

def calcular_precio_final(producto, categoria_objetivo, umbral_precio):
    precio_base = producto[2]
    categoria = producto[1]
    
    # Evalúa si cumple la categoría y supera el precio umbral
    if categoria.lower() == categoria_objetivo.lower() and precio_base > umbral_precio:
        descuento = precio_base * 0.15  # 15% de descuento
        precio_final = precio_base - descuento
        return precio_final, descuento
    else:
        return precio_base, 0.0


def mostrar_informe_menu():
    # Matriz con los 6 productos requeridos [Nombre, Categoría, Precio Base]
    menu = [
        ["Bife de Chorizo", "Carnes", 35000],
        ["Hamburguesa Artesanal", "Comida Rapida", 22000],
        ["Pechuga a la Plancha", "Carnes", 28000],
        ["Limonada Cerezada", "Bebidas", 12000],
        ["Lomo al Trapo", "Carnes", 42000],
        ["Flan de Leche", "Postres", 10000]
    ]
    
    CATEGORIA_PROMO = "Carnes"
    UMBRAL_PROMO = 25000
    
    print("\n=========================================================================")
    print("         RESTAURANTE EL BUEN SABOR - CONSULTA DE PROMOCIONES")
    print("=========================================================================")
    print(f"PROMOCION VIGENTE: 15% Dcto en '{CATEGORIA_PROMO}' con precio mayor a ${UMBRAL_PROMO:,}")
    print("-------------------------------------------------------------------------")
    print(f"{'PRODUCTO':<25} | {'CATEGORIA':<15} | {'P. BASE':<10} | {'P. FINAL':<10} | {'ESTADO'}")
    print("-------------------------------------------------------------------------")
    
    # Recorrido completo de la matriz
    for producto in menu:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]
        
        precio_final, ahorro = calcular_precio_final(producto, CATEGORIA_PROMO, UMBRAL_PROMO)
        
        if ahorro > 0:
            estado = "15% DCTO APLICADO"
        else:
            estado = "PRECIO REGULAR"
            
        print(f"{nombre:<25} | {categoria:<15} | ${precio_base:<9} | ${precio_final:<9.0f} | {estado}")
        
    print("=========================================================================\n")


if __name__ == "__main__":
    mostrar_informe_menu()
