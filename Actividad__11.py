propietarios ={}
cantidad_propietarios = int(input("===¿Cuantos propietarios desea ingresar?: "))
for i in range (cantidad_propietarios):
    print(f"Ingrese Propietario {i+1} ")
    nit = int(input("=== INGRESE NIT ===: "))
    name = input("=== INGRESE NOMBRE COMPLETO ===: ")
    telefono_contacto =int(input("=== INGRESE NUMERO DE TELEFONO ===: "))
    cantidad_vehiculos_posee = int(input"=== INGRESE CANTIDAD DE VEHICULOS QUE POSEE===: ")
    for i in range(cantidad_vehiculos_posee):
        print(f"\n===Por vehiculo que tenga ingrese===")
        print(f"____Datos vehiculo no.{i+1}___")
        placa = int(input("INGRESE PLACA DEL VEHICULO: "))
        marca = input("INGRESE LA MARCA DEL CARRO: ")
        model = int(input("INGRESE MODELO DEL CARRO: "))
        year = int(input("INGRES AÑO DEL CARRO: "))
        estado_impuesto = input("INGRESE ESTADO DEL IMPUESTO(SI O NO): ")


    propietarios[nit] = {
        "name" : name,
        "telefono_contacto" : telefono_contacto,
        "numero_carros" :{

        }

    }
