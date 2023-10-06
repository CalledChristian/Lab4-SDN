import requests
from requests.auth import HTTPBasicAuth

def get_attachment_points(floodlight_ip, floodlight_port, host_mac):
    url = f'http://{floodlight_ip}:{floodlight_port}/wm/device/?mac={host_mac}'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data and 'devices' in data:
            device_info = data['devices'][0]
            attachment_points = device_info.get('attachmentPoint', [])
            
            if attachment_points:
                attachment_point = attachment_points[0]
                switch_dpid = attachment_point['switchDPID']
                port = attachment_point['port']
                print(switch_dpid) 
                print(port)
                return switch_dpid, port
        else:
            print("No se encontró información para el host.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud: {e}")
    
    return None, None

# Ejemplo de uso:
floodlight_ip = '10.20.12.150'  
floodlight_port = '8080'  
host_mac = 'fa:16:3e:c2:33:d9'  

dpid, port = get_attachment_points(floodlight_ip, floodlight_port, host_mac)

if dpid and port:
    print(f"El host está conectado al switch DPID: {dpid}, puerto: {port}")
