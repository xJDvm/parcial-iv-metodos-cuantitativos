from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus

# Leer los datos de entrada
matriz = []
for i in range(10):
    fila = []
    for j in range(10):
        tiempo = int(input(f"Ingrese el tiempo de la ciudad {i+1} a la ciudad {j+1}: "))
        fila.append(tiempo)
    matriz.append(fila)

# Crear un problema de minimización
prob = LpProblem("Programacion_Binaria", LpMinimize)

# Definir las variables de decisión (binarias)
estaciones = [LpVariable(f'estacion_{i}', cat='Binary') for i in range(10)]

# Definir la función objetivo
prob += lpSum(estaciones), "Minimizar_Estaciones"

# Definir las restricciones
for i in range(10):
    prob += lpSum(estaciones[j] for j in range(10) if matriz[i][j] <= 40) >= 1, f"Restriccion_Ciudad_{i}"

# Resolver el problema
prob.solve()

# Mostrar los resultados
print("Estado:", LpStatus[prob.status])
print("Estaciones construidas:")
for i in range(10):
    if estaciones[i].varValue == 1:
        print(f"Ciudad {i} tendrá una estación.")