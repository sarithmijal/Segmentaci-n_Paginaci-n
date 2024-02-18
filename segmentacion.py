# Definición de segmentos y sus tamaños
segmento_codigo = {"base": 0, "limite": 4095}  # Segmento de código de 0 a 4095 bytes
segmento_datos = {"base": 8192, "limite": 12287}  # Segmento de datos de 8192 a 12287 bytes

# Función para traducir dirección lógica a dirección física
def traducir_direccion_logica_a_fisica_con_segmentacion(direccion_logica, segmentos):
    for segmento in segmentos:
        if segmento["base"] <= direccion_logica <= segmento["limite"]:
            direccion_fisica = direccion_logica - segmento["base"]
            return direccion_fisica + segmento["base"]

    raise Exception("Dirección lógica no pertenece a ningún segmento")

# Uso de la función de traducción con segmentación
direccion_logica = 9000  # Dirección lógica a traducir
direccion_fisica_resultante = traducir_direccion_logica_a_fisica_con_segmentacion(direccion_logica, [segmento_codigo, segmento_datos])
print(f"Dirección física resultante: {direccion_fisica_resultante}")
