import numpy as np  # Importamos NumPy para trabajar con vectores y funciones matemáticas

# Función para interpolar usando Lagrange por bloques
def lagrange_interpolation(x_values, y_values, new_x, window_size=5):
    
    new_y = []  # Lista donde se guardarán los resultados interpolados

    # Recorremos cada valor de x en el que se desea interpolar
    for x in new_x:
        # Calculamos la distancia entre este x y todos los puntos conocidos
        distances = np.abs(x_values - x)

        # Obtenemos los índices de los 'window_size' puntos más cercanos
        closest_indices = np.argsort(distances)[:window_size]

        # Seleccionamos los x e y correspondientes a los puntos más cercanos
        x_near = x_values[closest_indices]
        y_near = y_values[closest_indices]

        # Inicializamos la interpolación en 0
        y_interp = 0

        # Construimos el polinomio de Lagrange usando solo los puntos más cercanos
        for i in range(window_size):
            xi, yi = x_near[i], y_near[i]
            li = 1  # Esta será la base L_i(x)

            # Calculamos L_i(x) como producto de (x - xj) / (xi - xj) para j ≠ i
            for j in range(window_size):
                if i != j:
                    li *= (x - x_near[j]) / (xi - x_near[j])

            # Sumamos la contribución de este término a la interpolación
            y_interp += yi * li

        # Guardamos el resultado interpolado
        new_y.append(y_interp)

    return new_y  # Devolvemos todos los valores y interpolados
