## Documentation

Keyloger App, has been developed in python, it has the purpose of capturing OS keyboard (Windows, Linux and Mac), it has direct connection with a Cloudinary account, so it is necessary to have an active account of this application, it is also worth noting that an automatic copy is made every hour of the content captured in the keystrokes to this web in a . txt file, it is also important to note that when executing the main file main.py, if it is the first time, it will create an .env where your Cloudinary credentials will be stored, after saving the credentials, you must run the main file again, where it will only indicate that a file has been created correctly, as this will be generated in the createClient folder, which must be downloaded to the client device.

## Clone

clone with HTTPS
```
    git clone https://github.com/JCarlosQM/keylogerApp.git
```

clone with SSH
```
    git clone git@github.com:JCarlosQM/keylogerApp.git
```
## Requeriments


You must have a cloudinary account and a folder with the name 'PruebaKey'.

Subsequently install the requirements package

```
    pip install -r requeriments.txt
```
## Use

If this is the first time you run the program, you must run it twice, the first time to set cloudinary credentials and the second time to create the file for the client.
```
    python main.py
```
Afterwards, it is important to access the createClient folder, where you will have two files, which must be downloaded to the client machine

After getting the files on the client, it is necessary to execute the file 'cliente.py'.

#### Windows

To make the process run in the background you should run

```
pythonw cliente.py
```
#### Linux y mac
For the process to continue running despite closing the initialized console and running in the background 

```
nohup pyton3 cliente.py &
```

## Screenshots

When running the first time

![App Screenshot](https://res.cloudinary.com/dj1afzhnv/image/upload/v1708572560/Images_Cloud/ia6h8lmy8y7fwgivlfsh.png)

When running for the second time

![App Screenshot](https://res.cloudinary.com/dj1afzhnv/image/upload/v1708572631/Images_Cloud/t3fgskgtp9q6ydsvbpkz.png)

Resource to be generated, which must be obtained with everything and folder for the client.

![App Screenshot](https://res.cloudinary.com/dj1afzhnv/image/upload/v1708572779/Images_Cloud/tkuxhk4iukjnzdun9fmz.png)


## Licence


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)