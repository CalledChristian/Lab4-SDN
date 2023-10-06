import requests

def get_route(floodlight_ip, floodlight_port, dpid_origen, puerto_origen, dpid_destino, puerto_destino, topology_name=None):
    url = f'http://{floodlight_ip}:{floodlight_port}/wm/topology/route/{dpid_origen}/{puerto_origen}/{dpid_destino}/{puerto_destino}'
    
    if topology_name:
        url += f'?topology={topology_name}'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if 'route' in data:
            route = data['route']
            return route
        else:
            print("No se encontró una ruta entre los puntos de conexión especificados.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud: {e}")
    
    return None

# Ejemplo de uso:
floodlight_ip = '10.20.12.150'  # Reemplaza con la dirección IP de tu controlador Floodlight
floodlight_port = '8080'  # Reemplaza con el puerto de tu controlador Floodlight
dpid_origen = '00:00:00:00:00:01'  # Reemplaza con el DPID de origen
puerto_origen = '1'  # Reemplaza con el puerto de origen
dpid_destino = '00:00:00:00:00:02'  # Reemplaza con el DPID de destino
puerto_destino = '2'  # Reemplaza con el puerto de destino

ruta = get_route(floodlight_ip, floodlight_port, dpid_origen, puerto_origen, dpid_destino, puerto_destino)

if ruta:
    print("Ruta encontrada:")
    for hop in ruta:
        switch_dpid = hop['switch']
        switch_port = hop['port']
        print(f"Switch DPID: {switch_dpid}, Puerto: {switch_port}")
