# elaborado por: Alessandro Arias y Gabriel Muñoz
# fecha de elaboracion: mayo 19 de 2026
#  versionn de pyhton: 3.14.3
# hora de ultima actualizacion: 

# LIBRERIAS IMPORTACION
import re
import os 

# Esta parte es en donde se guardaran los datos, se instalo la bibloteca os para verificar que si existan los datos en el archivo.xs
baseDatosDonadores = {}
lugaresDonacionProvincia = {
    "1": ["Hospital México", "Hospital San Juan de Dios", "El Banco Nacional de Sangre"],
    "2": ["Hospital San Rafael de Alajuela", "Hospital de San Ramón", "Hospital del Cantón Norteño"],
    "3": ["Hospital Max Peralta"],
    "4": ["Hospital San Vicente de Paúl"],
    "5": ["Hospital La Anexión en Nicoya", "Hospital Enrique Baltodano de Liberia"],
    "6": ["Hospital Monseñor Sanabria"],
    "7": ["Hospital Tony Facio", "Hospital de Guápiles"],
    "8": ["Registro de Naturalizaciones (San José)"]
}

def verificarBaseDatos():
    """
    Verifica si existe el archivo de base de datos persistente.
    """
    return os.path.exists("donadores.dat") # (esto genuinamente lo vi en un tutorial de datos en py, y creo que sera necesario)

def validarCedula(cedulaTexto):
    """
    Valida formato #-####-#### donde el primer dígito no es 0
    """
    patronCedula = r"^[1-9]-\d{4}-\d{4}$"
    return bool(re.match(patronCedula, cedulaTexto))

def validarTelefono(telefonoTexto):
    """
    Valida formato ####-#### donde el primer dígito no es 0, 1, 3, 5
    """
    patronTelefono = r"^[246789]\d{3}-\d{4}$"
    return bool(re.match(patronTelefono, telefonoTexto))

def validarCorreo(correoTexto):
    """
    Valida dominios específicos que se le pide al usuario
    """
    patronCorreo = r"^[a-zA-Z0-9._%+-]+@(costarricense\.cr|racsa\.go\.cr|ccss\.sa\.cr|gmail\.com)$"
    return bool(re.match(patronCorreo, correoTexto))

def validarNombre(nombreTexto):
    """
    Valida que el nombre no esté vacío y contenga solo letras y espacios
    """
    textoLimpio = nombreTexto.strip()
    if not textoLimpio:
        return False
    return all(caracter.isalpha() or caracter.isspace() for caracter in textoLimpio)

def insertarNuevoDonador(cedula, nombre, tele, correo, provincia, peso, sangre):
    """
    Agrega un donador al diccionario global si pasa las validaciones y no está repetido.
    Retorna (True, "Mensaje éxito") o (False, "Mensaje de error")
    """
    global baseDatosDonadores
    # Validaciones de formato
    if not validarCedula(cedula):
        return False, "La cédula debe tener el formato #-####-#### (el primer dígito no puede ser 0)."
    if cedula in baseDatosDonadores:
        return False, f"El donador con la cédula {cedula} ya se encuentra registrado."
    if not validarNombre(nombre):
        return False, "El nombre completo solo debe contener letras y espacios."
    if not validarTelefono(tele):
        return False, "El teléfono debe tener el formato ####-#### (no puede iniciar con 0, 1, 3 o 5)."
    if not validarCorreo(correo):
        return False, "El correo electrónico debe pertenecer a los dominios autorizados:\n@gmail.com, @costarricense.cr, @racsa.go.cr o @ccss.sa.cr"
    try:
        pesoFlotante = float(peso)
        if not (50 <= pesoFlotante <= 120):
            return False, "El peso del donador debe estar estrictamente entre los 50 y 120 kg."
    except ValueError:
        return False, "El peso debe ser un número valido por ejemplo: '67.7'"
    # 3. Aqui es en donde se guardan los datos en el diccionario global
    baseDatosDonadores[cedula] = [
    nombre.strip(),
    tele,
    correo.lower().strip(),
    provincia,
    pesoFlotante,
    sangre,
    [] ]
    return True, "Donador registrado exitosamente en el sistema."

def buscarDonadorPorCedula(cedulaTexto):
    """
    Busca una cédula en el diccionario global y retorna los datos del donador si existe, o None si no se encuentra
    """
    global baseDatosDonadores
    if cedulaTexto in baseDatosDonadores:
        return baseDatosDonadores[cedulaTexto]
    return None

def actualizarDatosDonador(cedula, nombre, tele, correo, provincia, peso, sangre):
    """
    Funcionamiento: Valida y actualiza los datos de un donador existente ademas de que mantiene el historial de donaciones intacto
    entrdas: cedula, nombre, telefono, correo, provincia, peso y sangre
    salida: (True, "Mensaje de éxito") o (False, "Mensaje de error")
    """
    global baseDatosDonadores
    if cedula not in baseDatosDonadores:
        return False, "Error interno: El donador ya no se encuentra en el sistema."
    if not validarNombre(nombre):
        return False, "El nombre completo solo debe contener letras y espacios."
    if not validarTelefono(tele):
        return False, "El teléfono debe tener el formato ####-#### (no puede iniciar con 0, 1, 3 o 5)."
    if not validarCorreo(correo):
        return False, "El correo electrónico debe pertenecer a los dominios autorizados:\n@gmail.com, @costarricense.cr, @racsa.go.cr o @ccss.sa.cr"
    try:
        pesoFlotante = float(peso)
        if not (50 <= pesoFlotante <= 120):
            return False, "El peso del donador debe estar estrictamente entre los 50 y 120 kg."
    except ValueError:
        return False, "El peso debe ser un número valido por ejemplo: '67.7'"
    historialPrevio = baseDatosDonadores[cedula][6] # justo aqui, se preserva el historial y se le asigna una variable para despues actualizar el diccionario sin perder informacion
    baseDatosDonadores[cedula] = [ # aqui se actualizan los datos del donador y se mantiene el historial intacto
        nombre.strip(),
        tele,
        correo.lower().strip(),
        provincia,
        pesoFlotante,
        sangre,
        historialPrevio 
    ]
    
    return True, "Los datos del donador han sido actualizados exitosamente."
