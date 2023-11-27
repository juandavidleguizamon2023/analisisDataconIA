import re 

def validar_correo(correo):
    if str(correo).strip() == "nan" :
        return 0  # Correo vacío o nulo
    else:
        correo = str(correo).strip()
        # Patrón de expresión regular
        patron = r'^[a-zA-Z0-9._%+-ñáéíóúÑÁÉÍÓÚ]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        try:
            beforeAt = correo.split('@')[0]
        except IndexError:
            beforeAt = '0'
        try:
            afterAt = correo.split('@')[1]
        except IndexError:
            afterAt = '0'

        if (
            re.match(patron, correo) and                 # Correo válido según el formato general
            not correo.startswith(('.', '_', '{', '|', '*', '#', '$', '%', '&', '!', '-','@')) and  # No comienza con caracteres especiales
            not correo.endswith(('.', '_', '{', '|', '*', '#', '$', '%', '&', '!', '-','@')) and    # No termina con caracteres especiales
            not beforeAt.isdigit() and                    # No solo contiene dígitos
            len(afterAt) > 8 and                        # Longitud del dominio mayor a 9
            len(beforeAt) > 2 and                       # Longitud del texto antes del @ mayor a 3
            len(beforeAt) < 25 and                       # Longitud del texto antes del @ mayor a 3
            not all(c == beforeAt[0] for c in beforeAt) and  # No todos los caracteres son iguales antes del @
            beforeAt != "fepos" and                     # No es igual a "fepos" antes del @
            "notiene" not in beforeAt and               # No contiene la palabra "notiene" antes del @        
            "notengo" not in beforeAt and               # No contiene la palabra "notengo" antes del @        
            "sincorreo" not in beforeAt and               # No contiene la palabra "notengo" antes del @        
            "hotmail" not in beforeAt and               # No contiene la palabra "notengo" antes del @        
            "gmail" not in beforeAt and               # No contiene la palabra "notengo" antes del @        
            not re.search(r'(\w)\1{2,}', beforeAt)    # No permite más de 3 caracteres consecutivos repetidos
            #and len(re.findall(r'[a-zA-Z]', beforeAt)) > len(beforeAt) * 0.5  # No permite la mayoría de caracteres antes del @ sean números
        ):
            return 1  # Correo válido
        else:
            return 0  # Correo mal diligenciado o ficticio