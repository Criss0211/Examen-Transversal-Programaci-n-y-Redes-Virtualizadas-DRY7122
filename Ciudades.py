import openrouteservice

client = openrouteservice.Client(
    key="eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImRhNDA4MzA2MzhlMzQ3MjY4NWZmODRiYzNmOTg0ZGEwIiwiaCI6Im11cm11cjY0In0="
)

def obtener_coordenadas(ciudad):
    geocode = client.pelias_search(text=ciudad)
    if geocode['features']:
        coords = geocode['features'][0]['geometry']['coordinates']
        return coords 
    else:
        print(f" No se pudo localizar la ciudad: {ciudad}")
        return None

def calcular_ruta(origen, destino, transporte):
    try:
        ruta = client.directions(
            coordinates=[origen, destino],
            profile=transporte,
            format='geojson',
            language='es'
        )
        props = ruta['features'][0]['properties']['segments'][0]
        distancia_km = props['distance'] / 1000
        distancia_millas = distancia_km * 0.621371
        duracion_min = props['duration'] / 60
        pasos = props['steps']

        print(f"\n Distancia: {distancia_km:.2f} km / {distancia_millas:.2f} millas")
        print(f" Duración estimada: {duracion_min:.2f} minutos")
        print(" Instrucciones del viaje:")
        for paso in pasos:
            print("-", paso['instruction'])

    except Exception as e:
        print(" Error al calcular la ruta:", str(e))


if __name__ == '__main__':
    while True:
        print("\n--- Cálculo de ruta  ---")
        origen_txt = input("Ingrese ciudad de origen (o 's' para salir): ")
        if origen_txt.lower() == 's':
            print(" Fin del programa.")
            break

        destino_txt = input("Ingrese ciudad destino: ")
        transporte = input("Medio de transporte (driving-car, cycling-regular, foot-walking): ").strip()

        coord_origen = obtener_coordenadas(origen_txt)
        coord_destino = obtener_coordenadas(destino_txt)

        if coord_origen and coord_destino:
            calcular_ruta(coord_origen, coord_destino, transporte)
