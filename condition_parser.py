import re

# def extraer_variables(condicion):
#     # Extraer los nombres de las variables
#     variables = re.findall(r"\(([a-zA-Z_][a-zA-Z0-9_]*)", condicion)
#
#     return variables
#
# # Prueba de la función
# condicion = "(comunidad > 0.5) and (correo > 0.5)"
# variables = extraer_variables(condicion)
# print(variables)


def parsear_condicion(condicion):
    # Extraer las partes de la condición
    partes = re.findall(r"\(([a-zA-Z_][a-zA-Z0-9_]*\s*[<>]=?\s*\d+.\d+)\)", condicion)

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

# Prueba de la función
condicion = "(comunidad > 0.5) and (correo > 0.5)"
objetos = parsear_condicion(condicion)
print(objetos)