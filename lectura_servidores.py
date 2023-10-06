import yaml

# Abrimos el archivo YAML para lectura con la funcion open() , y 'r':read
with open('datos.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Verificamos si 'servidores' está en el archivo YAML
if 'servidores' in data:
    # Recorre la lista de servidores e imprime sus nombres
    for servidor in data['servidores']:
        if 'nombre' in servidor:
            print("Nombre del servidor:", servidor['nombre'])
        else:
            print("Nombre del servidor no encontrado en la entrada.")
else:
    print("No se encontró la lista de servidores en el archivo YAML.")
