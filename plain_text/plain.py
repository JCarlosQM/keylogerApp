import os
import platform

def format_text(texto):
    # Dividir el texto en líneas
    lineas = texto.split('\n')

    # Concatenar líneas consecutivas hasta encontrar un "BackSpace"
    lineas_concatenadas = []
    for i in range(len(lineas)):
        if "Return" in lineas[i]:
            lineas_concatenadas.append("\n")
        elif "Shift_R" in lineas[i]:
            continue
        else:
            try:
                texto = lineas[i].split(" - ")[1]
            except IndexError:
                continue
            else:
                texto = texto.replace("space", " ")
                simbolos = {
                  "BackSpace": " <- ",                 # @
                  "double_quote": "\U00002022",  # comilla doble (" ")
                  "at": u"\u0040",                 # @
                  "numbersign": u"\u0023",        # #
                  "dollar": u"\u0024",             # $ 
                  "comma": u"\u002C",             # ,
                  "percent": u"\u0025",            # %
                  "ampersand": u"\u0026",          # &
                  "period": u"\u002E",               # .
                  "asterisk": u"\u002A",               #
                  "parenleft": u"\u0028",   # (
                  "parenright": u"\u0029",  # ) 
                  "minus": u"\u002D",             # -
                  "underscore": u"\u005F",         # _
                  "equal": u"\u003D",         # =
                  "plus": u"\u002B",               # +
                  "bracketleft": u"\u005B",  # [
                  "bracketright": u"\u005D",  # ]
                  "braceleft": u"\u007B",  # {
                  "braceright": u"\u007D",  # }
                  "backslash": u"\u005C",           # \
                  "vertical_line": u"\u007C",       # |
                  ":colon": u"\u003A",              # :
                  "less": u"\u003C",          # <
                  "greater_than": u"\u003E",        # >
                  "question": u"\u003F",       # ?
                  "/forward_slashes": u"\u002F",    # /
                  "exclam": u"\u0021",    # !
                  "backspace": u"\u0008",           # Retroceso (BackSpace)
                  "ctrl_a": u"\u001B\u005B\u0041",  # Ctrl+[A (control + letra A)
              }
                for tecla, simbolo in simbolos.items():
                    texto = texto.replace(tecla, simbolo)
                lineas_concatenadas.append(texto)

    # Devolver el texto formateado
    texto_formateado = ' '.join(lineas_concatenadas)
    
    return texto_formateado


if __name__ == "__main__":
    path_direct = (os.getcwd())
    sistem_function = platform.system()

    print(sistem_function)

    new_path = os.path.join(os.path.dirname(path_direct), "createClient")
    os.chdir(new_path)

    if sistem_function == 'Linux' or sistem_function == 'Darwin':
        with open('.upload_content.txt', 'r') as archivo:
            texto = archivo.read()
    elif sistem_function == 'Windows':
        with open('upload_content.txt', 'r', encoding='utf-8') as archivo:
            texto = archivo.read()

    

    print(format_text(texto))