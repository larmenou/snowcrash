encoded_hex = "66346b6d6d36707c3d827f70826e838244428344757b7f8c890a"
encoded_bytes = bytes.fromhex(encoded_hex)

flag = ""
for i in range(len(encoded_bytes)):
    decoded_value = encoded_bytes[i] - i
    if 0 <= decoded_value <= 255:
        flag_char = chr(decoded_value)
        flag += flag_char
    else:
        print(f"Valeur hors plage a l'index {i}: {decoded_value}")

print("Flag :", flag)

