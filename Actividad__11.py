propietarios ={}
cantidad_propietarios = int(input("===¿Cuantos propietarios desea ingresar?: "))
for i in range (cantidad_propietarios):
    print(f"Ingrese Propietario {i+1} ")
    nit = input("=== INGRESE NIT ===: ")
    name = input("=== INGRESE NOMBRE COMPLETO ===: ")
    telefono_contacto =int(input("=== INGRESE NUMERO DE TELEFONO ===: "))
    cantidad_vehiculos_posee = int(input("=== INGRESE CANTIDAD DE VEHICULOS QUE POSEE===: "))

    for i in range(cantidad_vehiculos_posee):
        print(f"\n===Por vehiculo que tenga ingrese===")
        print(f"____Datos vehiculo no.{i+1}___")
        placa = input("INGRESE PLACA DEL VEHICULO: ")
        marca = input("INGRESE LA MARCA DEL CARRO: ")
        model = input(f"INGRESE  EL MODELO DE SU CARRO => {marca} <= \n(===EJEMPLO===: TOYOTA: COROLLA, FORD: RAPTOR, NISSAN:ROGUE ETC..... ): ")
        year = int(input("INGRES AÑO DEL CARRO: "))
        estado_impuesto = input("¿PAGO EL IMPUESTO? (SI O NO): ")


    propietarios[nit] = {
        "name" : name,
        "telefono_contacto" : telefono_contacto,
        "numero_carros" :{
            'placa' : placa,
            'marca' : marca,
            'model' : model,
            'year'  : year,
            'estado_impuesto' : estado_impuesto
        }

    }
print(f"\n=====LISTADO DE PROPIETARIOS REGISTRADOS=====")
for nit, data in propietarios.items():
    for i in data:
        print(f"\n===NIT===: {nit}")
        print(f"===NOMBRE===: {name}")
        print(f"===TELEFONO DE CONTACTO: {telefono_contacto}")
        print(f"\n______Vehiculos :______")
        print(f"___PLACA: {nit['placa']}")
        print(f"___MARCA: {nit['marca']}")
        print(f"___MODELO: {nit['model']}")
        print(f"___AÑO: {nit['yaer']}")
        print(f"___IMPUESTO: {nit['estado_impuesto']}")

print(f"\n=======Busqueda de propietario por identificacion========")
buscado = input("Ingrese su identificacion (NIT): ")
if buscado in propietarios:
    propietario = propietarios[buscado]
    print(f"\n_____PROPIETARIO ENCONTRADO_____")
    pagados = 0
    no_pagados = 0
    if estado_impuesto == "si":
        pagados += 1
    else:
        no_pagados +=1

         print(f"===TOTAL DE VEHICULOS CON IMPUESTOS PAGADOS: {nit["estado_impuesto", pagados] ")
         print(f"===TOTAL DE VEHICULOS SIN PAGAR: {nit["estado_impuesto"]}")
