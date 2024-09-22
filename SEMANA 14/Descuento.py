def calcular_descuento(cantidad_total, porcentaje_descuento=20):
    # Cálculo del descuento basado en la cantidad total y el porcentaje
    descuento = (cantidad_total * porcentaje_descuento) / 100
    return descuento

# Ejecución de la función
cantidad1 = 250
descuento1 = calcular_descuento(cantidad1)  # Llamada con el porcentaje predeterminado
cantidad_final1 = cantidad1 - descuento1  # Cálculo de la cantidad después del descuento

cantidad2 = 120
porcentaje2 = 25
descuento2 = calcular_descuento(cantidad2, porcentaje2)  # Llamada con un porcentaje específico
cantidad_final2 = cantidad2 - descuento2  # Cálculo de la cantidad después del descuento

# Presentación de los resultados
print(f"Descuento 1: {descuento1:.2f}, Cantidad final 1: {cantidad_final1:.2f}")
print(f"Descuento 2: {descuento2:.2f}, Cantidad final 2: {cantidad_final2:.2f}")