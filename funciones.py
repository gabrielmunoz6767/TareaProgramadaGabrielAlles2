# elaborado por: Alessandro Arias y Gabriel Muñoz
# fecha de elaboracion: mayo 19 de 2026
#  versionn de pyhton: 3.14.3
# hora de ultima actualizacion: 

# LIBRERIAS IMPORTACION
import re
from datetime import datetime

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
    "8": ["Registro de Naturalizaciones (San José)"]}

def verificarBaseDatos():
    """
    Verifica si existe el archivo de base de datos persistente.
    """
    try:
        # Intentamos abrir el archivo en modo lectura
        archivo = open("donadores.dat", "r")
        archivo.close() # Lo cerramos de inmediato si tuvo éxito
        return True
    except FileNotFoundError:
        # Si da este error específico, significa que el archivo no existe
        return False

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

def validarFechaNacimiento(fechaTexto):
    """
    Valida que el formato sea DD/MM/AAAA, que sea una fecha real 
    y que la persona sea mayor de edad (>= 18 años) en mayo de 2026.
    Retorna: (True, "Mensaje éxito") o (False, "Mensaje error")
    """
    patronFecha = r"^\d{2}/\d{2}/\d{4}$"
    if not bool(re.match(patronFecha, fechaTexto)):
        return False, "La fecha de nacimiento debe tener el formato DD/MM/AAAA."
    try:
        dia, mes, anno = map(int, fechaTexto.split("/"))
        fechaNac = datetime(anno, mes, dia)
    except ValueError:
        return False, "La fecha ingresada no es una fecha válida en el calendario."
    annoActual = 2026
    mesActual = 5
    edad = annoActual - anno
    if mesActual < mes:
        edad -= 1
    if edad >= 18:
        return True, "Dado su fecha de nacimiento usted ya puede ser donador."
    else:
        return False, "Dado su fecha de nacimiento usted aún no puede ser donador."

def insertarNuevoDonador(cedula, nombre, fechaNac, sexo, tele, correo, provincia, peso, sangre):
    """
    Agrega un donador al diccionario global si pasa las validaciones y no está repetido.
    Retorna (True, "Mensaje éxito") o (False, "Mensaje de error")
    """
    global baseDatosDonadores
    if not validarCedula(cedula):
        return False, "La cédula debe tener el formato #-####-#### (el primer dígito no puede ser 0)."
    if cedula in baseDatosDonadores:
        return False, f"El donador con la cédula {cedula} ya se encuentra registrado."
    if not validarNombre(nombre):
        return False, "El nombre completo solo debe contener letras y espacios."
    esMayor, mensajeEdad = validarFechaNacimiento(fechaNac)
    if not esMayor:
        return False, mensajeEdad
    if not validarTelefono(tele):
        return False, "El teléfono debe tener el formato ####-#### (no puede iniciar con 0, 1, 3 o 5)."
    if not validarCorreo(correo):
        return False, "El correo electrónico debe pertenecer a los dominios autorizados:\n@gmail.com, @costarricense.cr, @racsa.go.cr o @ccss.sa.cr"
    try:
        pesoFlotante = float(peso)
        if pesoFlotante < 50:
            return False, "Usted debe pesar más de 50 kgms para poder ser donador."
        if pesoFlotante > 120:
            return False, "Dado su sobre peso, no es posible donar sangre."
    except ValueError:
        return False, "El peso debe ser un número válido, por ejemplo: '67.7'"
    baseDatosDonadores[cedula] = [nombre.strip(),tele,correo.lower().strip(),provincia,pesoFlotante,sangre,[],fechaNac,sexo]
    lugares = lugaresDonacionProvincia.get(provincia, ["Centro de salud local"])
    lugaresTexto = ", ".join(lugares)
    mensajeExito = f"""Donador registrado exitosamente.
1. {mensajeEdad}
2. Dado que usted nació en la provincia de: {provincia}, usted podría donar en: {lugaresTexto}.
3. Usted posee un peso adecuado, correcto para ser donador de sangre.
4. Conoce tu tipo de sangre: {sangre}."""
    if sangre in ["A+", "A-"]:
        mensajeExito += "\n5. Le recomendamos ver el video de: 'Particularidades de la sangre tipo A: Responde diferente al estrés según la ciencia'."
    return True, mensajeExito

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
    Funcionamiento: Valida y actualiza los datos de un donador existente manteniendo el historial.
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
        if pesoFlotante < 50:
            return False, "Usted debe pesar más de 50 kgms para poder ser donador."
        if pesoFlotante > 120:
            return False, "Dado su sobre peso, no es posible donar sangre."
    except ValueError:
        return False, "El peso debe ser un número valido por ejemplo: '67.7'"
        
    historialPrevio = baseDatosDonadores[cedula][6]
    baseDatosDonadores[cedula] = [ nombre.strip(),tele,correo.lower().strip(),provincia,pesoFlotante,sangre,historialPrevio]
    return True, "Usted posee un peso adecuado, correcto para ser donador de sangre.\n\nLos datos del donador han sido actualizados exitosamente."

def insertarLugarDonacion(provinciaNumero, nuevoLugar):
    """
    Funcionamiento: Valida y agrega un nuevo lugar de donación a la lista de una provincia sin duplicados.
    """
    global lugaresDonacionProvincia
    lugarLimpio = nuevoLugar.strip()
    if not lugarLimpio:
        return False, "El nombre del lugar de donación no puede estar vacío."
    if provinciaNumero not in lugaresDonacionProvincia:
        return False, "La provincia seleccionada no es válida."
    for lugarExistente in lugaresDonacionProvincia[provinciaNumero]:
        if lugarExistente.lower().strip() == lugarLimpio.lower():
            return False, f"El lugar '{lugarLimpio}' ya se encuentra registrado para esta provincia."
    lugaresDonacionProvincia[provinciaNumero].append(lugarLimpio)
    return True, f"'{lugarLimpio}' ha sido agregado exitosamente a la lista de centros de donación."
def eliminarDonador(cedula, justificacion):
    global baseDatosDonadores
    if cedula not in baseDatosDonadores:
        return False, f"La persona con el número de cédula: {cedula} no está registrado en la base de datos del Banco de Sangre aún."
    baseDatosDonadores[cedula][9]  = 0             # estado = inactivo
    baseDatosDonadores[cedula][10] = justificacion  # justificación
    return True, "Donador eliminado satisfactoriamente."