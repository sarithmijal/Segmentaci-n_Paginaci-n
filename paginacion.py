# Configuración de la paginación
tamaño_pagina = 4096  # Tamaño de cada página en bytes
memoria_fisica = 8192  # Tamaño de la memoria física en bytes

# Función para traducir dirección lógica a dirección física
def traducir_direccion_logica_a_fisica(direccion_logica):
    numero_pagina = direccion_logica // tamaño_pagina
    desplazamiento = direccion_logica % tamaño_pagina

    if numero_pagina < memoria_fisica / tamaño_pagina:
        direccion_fisica = numero_pagina * tamaño_pagina + desplazamiento
        return direccion_fisica
    else:
        raise Exception("Acceso a una página fuera de los límites de la memoria física")

# Uso de la función de traducción
direccion_logica = 2048  # Dirección lógica a traducir
direccion_fisica_resultante = traducir_direccion_logica_a_fisica(direccion_logica)
print(f"Dirección física resultante: {direccion_fisica_resultante}")
