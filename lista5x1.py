def mediaGeometrica(num1, num2, media):
    media = num1 * num2
    media = media ** 0.5
    return media

valor1 = 4
valor2 = 5
resultado = 0

resultado = mediaGeometrica(valor1, valor2, resultado)
print(f"{resultado:.2f}")