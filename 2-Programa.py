precioManzana = int(input("Ingresa el precio de la manzana: "))
cantidadManzana = int(input("Cuantas manzanas: "))
descuento = 0


if cantidadManzana > 10:
    descuento = (precioManzana * cantidadManzana) * 0.1
    print(f"""Tienes un descuento del {descuento}  """)

    costoTotal = precioManzana * cantidadManzana
    costoTotal - costoTotal % 10
    print(
        f"""Fueron {cantidadManzana} manzanas
    el precio fue {precioManzana}
    Vas a pagar {precioManzana * cantidadManzana} 
    {costoTotal}
    """
    )


print(
    f"""
Fueron {cantidadManzana} manzanas
el precio fue {precioManzana}
Vas a pagar {precioManzana * cantidadManzana}
      """
)
