# https://www.youtube.com/watch?v=TI_Fd3GyReM&list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj&index=17

monto = float(input("Igrese el monto para saber el descuento -> "))
descuento = float(input("Porcentaje de descuent -> "))

print(f"monto original: ${monto:.2f} Monto con descuento: ${monto - monto*descuento/100:.2f}")