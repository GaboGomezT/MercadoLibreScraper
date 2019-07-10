import numpy as np
import matplotlib.pyplot as plt


np_prices = np.loadtxt('prices.out')
promedio_precios = np.mean(np_prices)
print(f"Promedio de precios: {promedio_precios}")

mediana_precios = np.median(np_prices)
print(f"Mediana de precios: {mediana_precios}")

std_precios = np.std(np_prices)
print(f"Desviación Estándar de precios: {std_precios}")

min_value = np.min(np_prices)
print(f"Valor Mínimo: {min_value}")

max_value = np.max(np_prices)
print(f"Valor Mínimo: {max_value}")

plt.plot(np_prices)
plt.ylabel('Precio en Pesos')
plt.show()

plt.hist(np_prices, 50, facecolor='blue', alpha=0.5)
plt.show()
