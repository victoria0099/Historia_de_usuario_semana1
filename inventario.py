name = input("ingrese producto: ") 
precio = float(input("ingrese precio:"))
cantidad = int(input("ingrese cantidad:"))

if (precio > 0) and (cantidad > 0): 
    costo_total = precio * cantidad
    print("=" * 50)
    print(f'nombre del producto: {name}')
    print(f'precio unitario: {precio}')
    print(f'cantidad de productos: {cantidad}')
    print(f'el costo total de su compra fue de: {costo_total}')
    print("=" * 50)
else:
    print("error, ingrese numeros validos")


