totalManzana = int(input("Cuantas manzanas: "))
precioManzana = int(input("Precio de las manzanas: "))
nombre = input("Cual es tu nombre: ")
descuento20 = 0
descuento10 = 0

if nombre.lower() == "Christian" or totalManzana == 18:
    descuento20 = (totalManzana * precioManzana) * 0.20
    print(
        f"Fueron {totalManzana} manzanas con un precio de {precioManzana} y un descuento de {descuento20} y el total fue {(totalManzana * precioManzana) - descuento20}"
    )
elif totalManzana > 10:
    descuento10 = (totalManzana * precioManzana) * 0.10
    print(
        f"Fueron {totalManzana} manzanas con un precio de {precioManzana} y un descuento de {descuento10} y el total fue {(totalManzana * precioManzana) - descuento10}"
    )
else:
    print(
        f"Fueron {totalManzana} manzanas con un precio de {precioManzana} y el total fue {(totalManzana * precioManzana) - descuento20}"
    )
