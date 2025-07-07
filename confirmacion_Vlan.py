def tipos_vlan(vlan_id):
    if 1 <= vlan_id <= 1005:
        return "Vlan Corresponde a una Normal (Rango 1-1005)"
    elif 1006 <= vlan_id <= 4094:
        return "Vlan Corresponde a una extendida (rango 1006-4094)"
    else:
        return " Vlan fuera Del Rango Permitido"
    
if __name__ == "__main__":
    while True:
        entrada = input("ingrese el número de VLAN,(o's' para salir):")
        if entrada.lower()== "s":
            print("Saliendo Del Programa")
            break
        if entrada.isdigit():
            vlan = int(entrada)
            print(tipos_vlan(vlan))
        else:
            print("Error, Ingrese solo numero")