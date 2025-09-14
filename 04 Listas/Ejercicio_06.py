# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).
lista_num=[1,2,3,4,5,6,7]
nueva_list= lista_num[-1:] + lista_num[:-1]

print(f"Lista original: {lista_num}")
print(f"Lista rotada: {nueva_list}")