continuar = int(input("""
Qué desea hacer el día de hoy?                  
1. Ingresar un nuevo producto
2. Salir del programa
                  
"""))



while continuar != 2 or continuar == 1:
        name = input("ingrese producto: ") 
    
        while True:
                try:
                    precio = float(input("ingrese precio:"))
                    break
                except ValueError:
                       print("Ingresa un número.")
                
        while True:
                try:
                    cantidad = int(input("ingrese cantidad:"))
                    break
                except ValueError:
                    print("Ingresa un número.")
        
    
        if precio > 0 and cantidad > 0:
            costo_total = precio * cantidad
            print("=" * 50)
            print(f'nombre del producto: {name}')
            print(f'precio unitario: {precio}')
            print(f'cantidad de productos: {cantidad}')
            print(f'el costo total de su compra fue de: {costo_total}')
            print("=" * 50)
        else:
            print("El precio no puede ser menor o igual a 0.")
        continuar = int(input("""
Qué desea hacer el día de hoy?                  
1. Ingresar un nuevo producto
2. Salir del programa                 
       """))


