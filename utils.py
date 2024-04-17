import re
"""
 IMPORTANTE: 
 En las reglas evaluadas se asume que 0 es la clase phishing y 1 la clase legitima.
"""
def evaluar_reglas(reglas, variables):
    # p = eval("(comunidad <= 0.5) and (saludo > 0.5) and (correo <= 0.5) and (factura > 0.5)", {}, variables)
    reglasPhishingCubiertas = []
    reglasLegitCubiertas = []
    reglaMayorProbabilidad = -1
    for id, regla in enumerate(reglas):
        if eval(regla["condicion"], {}, variables):
            if regla['clase'] == '1':
                reglasLegitCubiertas.append(id)
            else:
                reglasPhishingCubiertas.append(id)

            if reglaMayorProbabilidad == -1:
                reglaMayorProbabilidad = id
            elif float(regla['probabilidad']) > float(reglas[reglaMayorProbabilidad]['probabilidad']):
                reglaMayorProbabilidad = id

    return reglasPhishingCubiertas,reglasLegitCubiertas,reglaMayorProbabilidad

# # Definición de las reglas
#(comunidad <= 0.5) and (saludo <= 0.5) and (investigador <= 0.5) and (caso <= 0.5) and (correo <= 0.5) and (factura <= 0.5) and (clic <= 0.5) and (día <= 0.5) and (responda <= 0.5) and (instituto <= 0.5) and (evento <= 0.5) and (ciencia <= 0.5) and (banco <= 0.5) and (almacenamiento <= 0.5) and (favor <= 0.5) and (cuenta <= 0.5) and (suma <= 0.5)
# reglas = ["(comunidad > 0.5) and (correo > 0.5)"]
#
# # Definición de las variables
# variables = {"comunidad": 0.6, "correo": 0.7, "juan": 0.9}
#
# # Prueba de la función
# resultado = evaluar_reglas(reglas, variables)
# print(f"Clase: {resultado}")

#---------------------------------------------------------------------------

def parsear_condicion(condicion):
    # Extraer las partes de la condición
    # partes = re.findall(r"\(([a-zA-Z_][a-zA-Z0-9_]*\s*[<>]=?\s*\d+.\d+)\)", condicion)
    partes = re.findall(r"\(([a-zA-Z_ñÑ][a-zA-Z0-9_áéíóúÁÉÍÓÚñÑ]*\s*[<>]=?\s*\d+\.\d+)\)", condicion)

    # Crear una lista para almacenar los objetos
    objetos = []

    # Para cada parte de la condición
    for parte in partes:
        # Dividir la parte en el nombre de la variable, el operador y el valor
        variable, operador, valor = re.split(r"([<>]=?)", parte)

        # Crear un objeto con el nombre de la variable, el operador y el valor
        objeto = {
            "variable": variable.strip(),
            "operador": operador.strip(),
            "valor": float(valor.strip())
        }

        # Añadir el objeto a la lista
        objetos.append(objeto)

    return objetos

#-----------------------------------------------------------------------------

def parse_rule(regla):
    # Extraer la condición
    condicion = re.search(r"if (.*) then", regla).group(1).strip()

    # Extraer la clase
    clase = re.search(r"class: (\d)", regla).group(1).strip()

    # Extraer la probabilidad
    probabilidad = re.search(r"proba: (\d+.\d+)%", regla).group(1).strip()

    # Extraer el número de muestras
    # muestras = re.search(r"based on (\d+) samples", regla).group(1).strip()
    muestras = re.search(r"based on ([\d,]+) samples", regla).group(1).replace(',', '').strip()

    # Almacenar las variables en un objeto
    objeto = {
        "condicion": condicion,
        "clase": clase,
        "probabilidad": probabilidad,
        "muestras": muestras
    }

    return objeto