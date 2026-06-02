# elaborado por: Alessandro Arias y Gabriel Muñoz
# fecha de elaboracion: mayo 19 de 2026
#  versionn de pyhton: 3.14.3
# hora de ultima actualizacion: 

# LIBRERIAS IMPORTACION
import random
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

nombreArchivoGlobal = ""
def verificarBaseDatos(pNombreArchivo):
    """
    Verifica si existe el archivo intentando abrirlo en modo lectura ("r").
    Si existe, lee el string del diccionario y lo reconstruye usando eval().
    Si da FileNotFoundError, crea el archivo escribiendo un diccionario vacío "{}" en texto.
    """
    global nombreArchivoGlobal, baseDatosDonadores
    nombreArchivoGlobal = pNombreArchivo
    try:
        with open(nombreArchivoGlobal, "r", encoding="utf-8") as pArchivoLectura:
            pContenido = pArchivoLectura.read().strip()
            if pContenido:
                baseDatosDonadores = eval(pContenido)
            else:
                baseDatosDonadores = {}
        return True 
    except FileNotFoundError:
        try:
            with open(nombreArchivoGlobal, "w", encoding="utf-8") as pArchivoEscritura:
                pArchivoEscritura.write("{}") # Escribe un diccionario vacío en el archivo para crear la base de datos inicial
        except Exception:
            pass
        baseDatosDonadores = {}
        return False 

def guardarEnBaseDatos():
    """
    Guarda el estado actual del diccionario global convirtiéndolo a string plano 
    dentro del archivo seleccionado (.py, .txt, etc.).
    """
    global nombreArchivoGlobal, baseDatosDonadores
    if nombreArchivoGlobal:
        try:
            with open(nombreArchivoGlobal, "w", encoding="utf-8") as pArchivoEscritura:
                pArchivoEscritura.write(str(baseDatosDonadores))
        except Exception:
            pass

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
    
    baseDatosDonadores[cedula] = [
        nombre.strip(),         # [0] se guarda el nombre
        tele,                   # [1] El teléfono se guarda tal cual, sin modificar el formato, para mantener la consistencia con la validación
        correo.lower().strip(), # [2]  se guarda el correo. en minúsculas para evitar problemas de mayúsculas en futuras búsquedas o actualizaciones
        provincia,              # [3] se guarda la provincia tal cual
        pesoFlotante,           # [4] se guarda el peso como flotante
        sangre,                 # [5] se guarda el tipo de sangre
        [],                     # [6] Historial de donaciones inicial vacío
        fechaNac,               # [7] se guarda la fecha de nacimiento
        sexo,                   # [8] se guarda el sexo
        1                       # [9] Estado Inicial: 1 = Activo 
    ]
    guardarEnBaseDatos()
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
    
    # --- BORRADO FÍSICO CON .pop() ---
    # Eliminamos por completo la cédula y su lista de datos del diccionario
    baseDatosDonadores.pop(cedula)
    
    # --- ACTUALIZACIÓN DEL ARCHIVO ---
    # Reescribimos el archivo de texto plano para que ya no tenga al usuario
    guardarEnBaseDatos()
    
    return True, "Donador eliminado por completo de la base de datos satisfactoriamente."
TIPOS_SANGRE = ("O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-")

def generarDonadores(cantidad):
    """
    Registra múltiples donadores de forma automática en la base de datos.
    entrada: cantidad (int): Cuántos donadores generar
    salida: (exitosos, rechazados, mensaje)
    """
    global baseDatosDonadores
    nombresHombre = ["Felipe", "Luis", "Andres", "Jose", "Gabriel",
                     "Alessandro", "Jorge", "Daniel", "Ricardo", "Eduardo"]
    nombresMujer  = ["Maria", "Ana", "Laura", "Sofia", "Valeria",
                     "Daniela", "Lucia", "Camila", "Natalia", "Paola"]
    apellidos     = ["Arias", "Alfaro", "Mora", "Jimenez", "Vargas",
                     "Hernandez", "Rojas", "Gomez", "Castro", "Brenes"]
    dominios      = ["gmail.com", "costarricense.cr", "racsa.go.cr", "ccss.sa.cr"]
    primerosDigitos = [2, 4, 6, 7, 8, 9]
    exitosos   = 0
    rechazados = 0
    registradas = 0
    while registradas < cantidad:
        #  Cédula única 
        while True:
            provincia   = random.randint(1, 8)
            parte1      = random.randint(1000, 9999)
            parte2      = random.randint(1000, 9999)
            cedula      = f"{provincia}-{parte1}-{parte2}"
            if cedula not in baseDatosDonadores:
                break
        #  Nombre 
        esHombre = random.choice([True, False])
        if esHombre:
            nombre = random.choice(nombresHombre)
            sexo   = "Masculino"
        else:
            nombre = random.choice(nombresMujer)
            sexo   = "Femenino"
        apellido1      = random.choice(apellidos)
        apellido2      = random.choice(apellidos)
        nombreCompleto = f"{nombre} {apellido1} {apellido2}"
        #Teléfono
        primero     = random.choice(primerosDigitos)
        resto       = random.randint(0, 9999999)
        telCompleto = f"{primero}{resto:07d}"
        telefono    = f"{telCompleto[:4]}-{telCompleto[4:]}"
        #Correo
        correo = f"{nombre.lower()}{random.randint(1, 999)}@{random.choice(dominios)}"
        #  Fecha: 70% mayores de edad, 30% menores ---
        if random.random() < 0.70:
            anno = random.randint(1950, 2007)
        else:
            anno = random.randint(2010, 2025)
        mes   = random.randint(1, 12)
        dia   = random.randint(1, 28)
        fecha = f"{dia:02d}/{mes:02d}/{anno}"
        #  Peso: 80% válido, 20% inválido 
        if random.random() < 0.80:
            peso = round(random.uniform(50.1, 119.9), 1)
        else:
            peso = round(random.choice([
                random.uniform(20.0, 49.9),
                random.uniform(121.0, 150.0)
            ]), 1)
        # --- Tipo de sangre desde la tupla global ---
        sangre    = random.choice(TIPOS_SANGRE)
        provinciaTxt = str(random.randint(1, 8))
        # --- Determina si es apto ---
        esAptoEdad, _ = validarFechaNacimiento(fecha)
        esAptoPeso    = 50 < peso < 120
        if esAptoEdad and esAptoPeso:
            estado = 1
            exitosos += 1
        else:
            estado = 0
            rechazados += 1
        # --- Guarda con la misma estructura de insertarNuevoDonador ---
        baseDatosDonadores[cedula] = [
            nombreCompleto,  # [0]
            telefono,        # [1]
            correo,          # [2]
            provinciaTxt,    # [3]
            peso,            # [4]
            sangre,          # [5]
            [],              # [6] historial
            fecha,           # [7]
            sexo,            # [8]
            estado           # [9]
        ]
        registradas += 1
    guardarEnBaseDatos()
    mensaje = (f"Generación completada.\n\n"
               f"Donadores aptos registrados: {exitosos}\n"
               f"Donadores no aptos registrados: {rechazados}\n"
               f"────────────────────────\n"
               f"Total generados: {registradas}")
    return exitosos, rechazados, mensaje
def generarReporteDonantesProvinicia(provinciaNúmero):
    """
    Genera un reporte HTML de donantes activos de una provincia, ordenados por nombre.
    entrada: Número de la provincia
    salida: (True, "mensaje") o (False, "mensaje")
    """
    global baseDatosDonadores
    nombresProvincia = {
        "1": "San José", "2": "Alajuela", "3": "Cartago",
        "4": "Heredia", "5": "Guanacaste", "6": "Puntarenas",
        "7": "Limón", "8": "Naturalizado"
    }
    # filtra solo los activos de esa provincia
    lista = []
    for cedula, datos in baseDatosDonadores.items():
        if datos[3] == provinciaNúmero and datos[9] == 1:
            lista.append((cedula, datos))
    if not lista:
        return False, "Reporte no creado. No hay donantes activos en esa provincia."
    lista.sort(key=lambda x: x[1][0]) # ordena por nombre
    nombreProv = nombresProvincia.get(provinciaNúmero, "Desconocida")
    fechaHora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # construye las filas de la tabla
    filas = ""
    for cedula, datos in lista:
        filas += f"<tr><td>{cedula}</td><td>{datos[0]}</td><td>{datos[7]}</td><td>{datos[1]}</td><td>{datos[2]}</td></tr>"
    # arma el HTML
    html = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>Donantes por Provincia</title></head>
<body>
<h2>Reporte: Donantes por Provincia</h2>
<p>Provincia: {nombreProv}</p>
<p>Generado el: {fechaHora}</p>
<table border="1" cellpadding="5" cellspacing="0">
<tr><th>Cedula</th><th>Nombre Completo</th><th>Fecha Nacimiento</th><th>Telefono</th><th>Correo</th></tr>
{filas}
</table>
</body>
</html>"""
    try:
        nombreArchivo = f"reporte_provincia_{nombreProv}.html"
        with open(nombreArchivo, "w", encoding="utf-8") as archivo:
            archivo.write(html)
        return True, f"Reporte creado satisfactoriamente.\nArchivo: {nombreArchivo}"
    except Exception as e:
        return False, f"Reporte no creado. Error: {str(e)}"

def generarReportePorRangoEdad(edadInicial, edadFinal=None):
    """
    Genera un reporte HTML de donantes activos en un rango de edad.
    entrada: edadInicial (int), edadFinal (int) opcional
    salida: (True, "mensaje") o (False, "mensaje")
    """
    global baseDatosDonadores
    annoActual = 2026
    mesActual = 5

    def calcularEdad(fechaNac):
        try:
            dia, mes, anno = map(int, fechaNac.split("/"))
            edad = annoActual - anno
            if mesActual < mes:
                edad -= 1
            return edad
        except:
            return -1

    lista = []
    for cedula, datos in baseDatosDonadores.items():
        if datos[9] != 1:
            continue
        edad = calcularEdad(datos[7])
        if edadFinal is None:
            if edad == edadInicial:
                lista.append((cedula, datos))
        else:
            if edadInicial <= edad <= edadFinal:
                lista.append((cedula, datos))
    if not lista:
        return False, "Reporte no creado. No hay donantes en ese rango de edad."
    lista.sort(key=lambda x: x[1][0])
    fechaHora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if edadFinal is None:
        rango = f"{edadInicial} años"
    else:
        rango = f"{edadInicial} a {edadFinal} años"
    filas = ""
    for cedula, datos in lista:
        filas += f"<tr><td>{cedula}</td><td>{datos[0]}</td><td>{datos[7]}</td><td>{datos[1]}</td><td>{datos[2]}</td></tr>"
    html = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>Donantes por Rango de Edad</title></head>
<body>
<h2>Reporte: Donantes por Rango de Edad</h2>
<p>Rango: {rango}</p>
<p>Generado el: {fechaHora}</p>
<table border="1" cellpadding="5" cellspacing="0">
<tr><th>Cedula</th><th>Nombre Completo</th><th>Fecha Nacimiento</th><th>Telefono</th><th>Correo</th></tr>
{filas}
</table>
</body>
</html>"""
    try:
        nombreArchivo = f"reporte_edad_{rango.replace(' ', '_')}.html"
        with open(nombreArchivo, "w", encoding="utf-8") as archivo:
            archivo.write(html)
        return True, f"Reporte creado satisfactoriamente.\nArchivo: {nombreArchivo}"
    except Exception as e:
        return False, f"Reporte no creado. Error: {str(e)}"

