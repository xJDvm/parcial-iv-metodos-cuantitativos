# Importar la biblioteca de PuLP
from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, LpStatus, PULP_CBC_CMD

# Función para leer la función objetivo
def leer_funcion_objetivo():
    tipo = input("Ingrese el tipo de problema (max/min): ").strip().lower()
    num_variables = int(input("Ingrese el número de variables: "))
    coeficientes = []
    for i in range(num_variables):
        coef = int(input(f"Ingrese el coeficiente de x{i+1} en la función objetivo: "))
        coeficientes.append(coef)
    return tipo, coeficientes

# Función para leer las restricciones
def leer_restricciones(num_variables):
    restricciones = []
    num_restricciones = int(input("Ingrese el número de restricciones: "))
    for i in range(num_restricciones):
        coeficientes_restriccion = []
        for j in range(num_variables):
            coef = int(input(f"Ingrese el coeficiente de x{j+1} en la restricción {i+1}: "))
            coeficientes_restriccion.append(coef)
        rhs = int(input(f"Ingrese el lado derecho de la restricción {i+1}: "))
        restricciones.append((coeficientes_restriccion, rhs))
    return restricciones

# Crear el problema
tipo, coeficientes = leer_funcion_objetivo()
if tipo == 'max':
    prob = LpProblem("Problema_Programacion_Entera", LpMaximize)
elif tipo == 'min':
    prob = LpProblem("Problema_Programacion_Entera", LpMinimize)
else:
    raise ValueError("Tipo de problema no reconocido. Use 'max' o 'min'.")

# Definir variables (enteras)
variables = [LpVariable(f'x{i+1}', lowBound=0, cat='Integer') for i in range(len(coeficientes))]

# Definir la función objetivo
prob += sum(coef * var for coef, var in zip(coeficientes, variables)), "Función Objetivo"

# Leer y definir las restricciones
restricciones = leer_restricciones(len(coeficientes))
for i, (coeficientes_restriccion, rhs) in enumerate(restricciones):
    prob += sum(coef * var for coef, var in zip(coeficientes_restriccion, variables)) <= rhs, f"Restriccion_{i+1}"

# Resolver el problema
prob.solve(PULP_CBC_CMD(msg=0))

# Mostrar el estado del problema
print(f"Estado: {LpStatus[prob.status]}")

# Mostrar los valores óptimos de las variables
for var in variables:
    print(f"{var.name} = {var.varValue}")

# Mostrar el valor óptimo de la función objetivo
print(f"Valor óptimo de la función objetivo: {prob.objective.value()}")