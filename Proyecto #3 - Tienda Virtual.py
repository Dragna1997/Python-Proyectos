'''
Crea un Programa que Simule una Tienda Virtual Simple, con las Siguientes
Especificaciones.

- Muestra un Catálogo de Productos Disponibles con sus Nombres y Precios.
- El Usuario Deberá Tener la Opción de Agregar Productos al Carrito.
- El Usuario Deberá Tener la Opción de Ver lo que hay en el Carrito.
- El Usuario Deberá Tener la Opción de Realizar el Pago y Salir.
'''
print("Bienvenido a la Tienda Virtual")

catalogo = {
    "Camiseta": 20,
    "Jeans": 40,
    "Zapatos": 60,
    "Sombrero": 10
    }

carrito = []

while True:
    print("\nMenú: ")
    print("1. Agregar Productos al Carrito")
    print("2. Var Carrito")
    print("3. Realizar el Pago y Salir")

    opcion = input("Seleccione una Opción: ")

    if opcion == "1":
        print("\nProductos Disponibles: ")
        [print(f"• {producto} ${precio}") for producto, precio in catalogo.items()]
        producto = input("Ingrese el Nombre del Producto que Desea Agregar: ").title()

        if producto in catalogo:
            carrito.append(producto)
            print(f"Producto '{producto}' agregado al carrito.")

    elif opcion == "2":
        print("\nCarrito: ")
        for producto in set(carrito):
            cantidad = carrito.count(producto)
            precio_unitario = catalogo[producto]
            print(f"{cantidad} {producto} - ${precio_unitario} c/u")

    elif opcion == "3":
        total_a_pagar = sum(catalogo[producto] for producto in carrito)
        print(f"Total a Pagar: ${total_a_pagar}")

        try:

            monto_pagado = float(input("Ingrese el Monto con el que Pagará: "))
            cambio = monto_pagado - total_a_pagar

            if cambio >= 0:
                mensaje_cambio = f"Su Cambio es: ${round(cambio, 2)}" if cambio > 0 else "¡Exacto! No se requiere cambio"
                print(f"Gracias por su Compra. {mensaje_cambio}")
                break
            else:
                print("El Monto Ingresado es Insuficuente. Por Favor, Ingrese un Monto Válido.")

        except Exception as e:
            print("Monto Invalido. Por Favor, Ingrese un Monto Valido.")

    else:
        print("Opcion no Valida. Por Favor, Seleccione una Opción Valida.")

input("Presiona Enter para salir")
