#!/usr/bin/python
import requests
from prettytable import PrettyTable

# DEFINE VARIABLES
controller_ip = '10.20.12.150' 
target_api = '/wm/core/controller/switches/json' 
headers = {'Content-type': 'application/json','Accept': 'application/json'}
url = f'http://{controller_ip}:8080{target_api}'
response = requests.get(url=url, headers=headers)

if response.status_code == 200:
    # SUCCESSFUL REQUEST
    print('SUCCESSFUL REQUEST | STATUS: 200')
    data = response.json()
    table = PrettyTable(data[0].keys())
    for row in data:
        table.add_row(row.values())
    print(table)
else:
    # FAILED REQUEST
    print(f'FAILED REQUEST | STATUS: 200 {response.status_code}')

# FOR QUESTION 1h
# COMPLETE FOR PRINT ALL FLOWS PER SWITCH PID
# FIRST YOU NEED TO ASK USER INPUT A SWITCH PID
# AFTERWARD, BY USING THIS SWITCH PID, YOU SHOULD ASK THE PERTINENT API FOR GET ALL FLOWS PER SWITCH PID AND PRINT THEM (AS ABOVE CODE)

# Definimos la API para obtener los flow entries de un switch según su DPID
flows_api = '/wm/core/switch/{dpid}/flow/json'

try:
    # Pedimos al usuario que ingrese el DPID del switch
    dpid_input = input("Ingresa el DPID del switch para ver sus flow entries (entradas de flujo) (p. ej., 00:00:f4:d3:0f:01): ")
            
    # Definimos la URL completa para obtener los flow entries del switch seleccionado
    flows_url = f'http://{controller_ip}:8080{flows_api.replace("{dpid}", dpid_input)}'
    
    # Realizamos la solicitud GET para obtener los flow entries del switch
    response = requests.get(flows_url)
    
    # Verificamos si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
        flows_data = response.json()
        print(f"Entradas de flujo del switch DPID {dpid_input}:")
        print(flows_data)
    else:
        print(f"Error en la solicitud de entradas de flujo: Código {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

