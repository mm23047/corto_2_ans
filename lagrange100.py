import numpy as np  # Importamos NumPy para trabajar con arreglos numéricos

# Esta función realiza interpolación de Lagrange global usando todos los puntos conocidos
def lagrange_interpolation100(x_values, y_values, x_points):
    
    # Función interna que calcula la base de Lagrange L_i(x)
    def lagrange_basis(i, x):
        basis = 1  # Inicializamos el producto a 1
        for j in range(len(x_values)):
            if j != i:  # Saltamos cuando j == i
                # Multiplicamos los factores del producto de L_i(x)
                basis *= (x - x_values[j]) / (x_values[i] - x_values[j])
        return basis  # Devolvemos L_i(x)

    y_interp = []  # Lista para guardar los valores interpolados y(x)

    # Iteramos sobre cada x donde queremos interpolar
    for x in x_points:
        y = 0  # Inicializamos y(x) en 0
        # Calculamos y(x) como la suma de y_i * L_i(x)
        for i in range(len(x_values)):
            y += y_values[i] * lagrange_basis(i, x)
        y_interp.append(y)  # Guardamos el resultado interpolado

    return x_points, y_interp  # Retornamos los puntos x y sus valores y interpolados
