# ==========================================
# SISTEMA DE ORIENTACIÓN Y REGISTRO - UPN
# ==========================================

# Función sin retorno (Requerimiento 4)
def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar nueva solicitud")
    print("2. Mostrar resumen de solicitudes")
    print("3. Salir")
    print("----------------------")

# Función con retorno para validar texto obligatorio (Requerimiento 6)
def validar_texto_obligatorio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("Error: Este campo no puede estar vacío.")
        else:
            return valor

# Función con retorno para validar código de estudiante (Requerimiento 2)
def validar_codigo_estudiante():
    while True:
        codigo = input("Ingrese código de estudiante (mínimo 5 caracteres): ").strip()
        if len(codigo) >= 5: # Longitud mínima definida
            return codigo
        else:
            print("Error: El código debe tener al menos 5 caracteres.")

# Función con retorno para validar tipo de consulta (Requerimiento 3)
def validar_tipo_consulta():
    tipos_validos = ["matricula", "pagos", "constancia", "plataforma", "otro"]
    while True:
        tipo = input(f"Ingrese tipo de consulta {tipos_validos}: ").lower().strip()
        if tipo in tipos_validos:
            return tipo
        else:
            print("Error: Tipo de consulta no válido. Intente de nuevo.")

# Función con retorno para asignar prioridad (Requerimiento 5)
def calcular_prioridad(tipo_consulta):
    # Prioridad Alta para matrícula y pagos, Baja para el resto
    if tipo_consulta in ["matricula", "pagos"]:
        return "Alta"
    else:
        return "Baja"

# Función para mostrar el resumen (Requerimiento 7)
def mostrar_resumen(solicitudes):
    print("\n--- RESUMEN DE SOLICITUDES REGISTRADAS ---")
    if not solicitudes:
        print("No hay solicitudes registradas.")
    else:
        for i, sol in enumerate(solicitudes, 1):
            print(f"\nSolicitud #{i}")
            print(f"Código: {sol['codigo']}")
            print(f"Nombre: {sol['nombre']}")
            print(f"Tipo: {sol['tipo']}")
            print(f"Descripción: {sol['descripcion']}")
            print(f"Prioridad: {sol['prioridad']}")
    print("-----------------------------------------")

# ==========================================
# PROGRAMA PRINCIPAL (Requerimiento 9 y 10)
# ==========================================
def main():
    # Estructura básica para guardar las solicitudes (Requerimiento 10)
    lista_solicitudes = [] 
    contador_solicitudes = 0
    meta_solicitudes = 3

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            if contador_solicitudes >= meta_solicitudes:
                print("Ya se han registrado las 3 solicitudes mínimas para esta ejecución.")
                continue

            print(f"\n--- Registrando solicitud #{contador_solicitudes + 1} ---")
            
            # Recolección de datos usando funciones (Requerimiento 8: paso de parámetros)
            codigo = validar_codigo_estudiante()
            nombre = validar_texto_obligatorio("Ingrese nombre del estudiante: ")
            tipo = validar_tipo_consulta()
            descripcion = validar_texto_obligatorio("Ingrese descripción breve: ")
            
            # Cálculo de prioridad
            prioridad = calcular_prioridad(tipo)

            # Almacenar en la estructura (Diccionario dentro de una Lista)
            nueva_solicitud = {
                "codigo": codigo,
                "nombre": nombre,
                "tipo": tipo,
                "descripcion": descripcion,
                "prioridad": prioridad
            }
            lista_solicitudes.append(nueva_solicitud)
            contador_solicitudes += 1
            print("Muy bien. Solicitud registrada exitosamente.")

        elif opcion == "2":
            mostrar_resumen(lista_solicitudes)

        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
