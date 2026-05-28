# elaborado por: Alessandro Arias y Gabriel Muñoz
# fecha de elaboracion: mayo 19 de 2026
#  versionn de pyhton: 3.14.3
# hora de ultima actualizacion: 6:55 pm del jueves 21 de mayo 2026
# librerias importadas
import tkinter as tk
from tkinter import messagebox # mensajes emergentes para mostrar información o errores al usuario
from tkinter import ttk  # se importa ttk para usar Combobox, que es una lista desplegable más moderna y estilizada
import funciones as fn # quisimos abreviarla, puesto que poner .funciones en todo lado se hace mas largo todo

def abrirInsertarDonador():
    """
    Crea la subventana con el diseño exacto solicitado: campos de Cédula, Nombre, 
    Fecha de Nacimiento, Tipo de Sangre, Sexo (Radio Buttons), Peso, Teléfono, Correo,
    y los botones Registrar, Limpiar y Regresar.
    """
    ventanaFormulario = tk.Toplevel()
    ventanaFormulario.title("Registrar Nuevo Donador")
    ventanaFormulario.geometry("500x650")
    ventanaFormulario.grab_set()  # Bloquea la ventana principal

    # Título de la subventana
    lblFormulario = tk.Label(ventanaFormulario, text="Formulario de Inscripción", font=("Arial", 14, "bold"))
    lblFormulario.pack(pady=10)

    # Contenedor para alinear correctamente los campos de texto
    marcoCampos = tk.Frame(ventanaFormulario)
    marcoCampos.pack(padx=20, pady=5, fill="x")

    # Campo: Cédula
    tk.Label(marcoCampos, text="Cédula (#-####-####):", font=("Arial", 10)).pack(anchor="w", padx=20)
    campoCedula = tk.Entry(marcoCampos, width=45)
    campoCedula.pack(pady=2, padx=20)

    # Campo: Nombre Completo
    tk.Label(marcoCampos, text="Nombre Completo:", font=("Arial", 10)).pack(anchor="w", padx=20)
    campoNombre = tk.Entry(marcoCampos, width=45)
    campoNombre.pack(pady=2, padx=20)

    # Campo NUEVO: Fecha de Nacimiento
    tk.Label(marcoCampos, text="Fecha de Nacimiento (DD/MM/AAAA):", font=("Arial", 10)).pack(anchor="w", padx=20)
    campoFechaNac = tk.Entry(marcoCampos, width=45)
    campoFechaNac.pack(pady=2, padx=20)

    # Campo: Tipo de Sangre (Lista Desplegable)
    tk.Label(marcoCampos, text="Tipo de Sangre:", font=("Arial", 10)).pack(anchor="w", padx=20)
    tiposSangreOpciones = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
    listaSangre = ttk.Combobox(marcoCampos, values=tiposSangreOpciones, width=42, state="readonly")
    listaSangre.current(0)
    listaSangre.pack(pady=2, padx=20)

    # Campo NUEVO: Sexo (Radio Buttons)
    tk.Label(marcoCampos, text="Sexo:", font=("Arial", 10)).pack(anchor="w", padx=20)
    variableSexo = tk.StringVar(value="Masculino")  # Marcado por omisión como pide la imagen
    
    marcoRadioButtons = tk.Frame(marcoCampos)
    marcoRadioButtons.pack(anchor="w", padx=20, pady=2)
    
    rbMasculino = tk.Radiobutton(marcoRadioButtons, text="Masculino", variable=variableSexo, value="Masculino", font=("Arial", 10))
    rbMasculino.pack(side="left", padx=5)
    
    rbFemenino = tk.Radiobutton(marcoRadioButtons, text="Femenino", variable=variableSexo, value="Femenino", font=("Arial", 10))
    rbFemenino.pack(side="left", padx=5)

    # Campo: Peso
    tk.Label(marcoCampos, text="Peso en kg (50 - 120):", font=("Arial", 10)).pack(anchor="w", padx=20)
    campoPeso = tk.Entry(marcoCampos, width=45)
    campoPeso.pack(pady=2, padx=20)

    # Campo: Teléfono
    tk.Label(marcoCampos, text="Teléfono (####-####):", font=("Arial", 10)).pack(anchor="w", padx=20)
    campoTelefono = tk.Entry(marcoCampos, width=45)
    campoTelefono.pack(pady=2, padx=20)

    # Campo: Correo Electrónico
    tk.Label(marcoCampos, text="Correo Electrónico:", font=("Arial", 10)).pack(anchor="w", padx=20)
    campoCorreo = tk.Entry(marcoCampos, width=45)
    campoCorreo.pack(pady=2, padx=20)

    # Campo: Provincia (
    tk.Label(marcoCampos, text="Provincia de Residencia:", font=("Arial", 10)).pack(anchor="w", padx=20)
    provinciasOpciones = ["1. San José", "2. Alajuela", "3. Cartago", "4. Heredia", "5. Guanacaste", "6. Puntarenas", "7. Limón", "8. Naturalizado"]
    listaProvincia = ttk.Combobox(marcoCampos, values=provinciasOpciones, width=42, state="readonly")
    listaProvincia.current(0)
    listaProvincia.pack(pady=2, padx=20)

    marcoBotones = tk.Frame(ventanaFormulario)
    marcoBotones.pack(pady=20)

    # Botón registrar
    botonRegistrar = tk.Button(
        marcoBotones, text="Registrar", bg="#E0631F", fg="white", font=("Arial", 10, "bold"), width=12,
        command=lambda: ejecutarGuardadoDonador(ventanaFormulario, campoCedula, campoNombre, campoFechaNac, variableSexo, campoTelefono, campoCorreo, listaProvincia, campoPeso, listaSangre))
    botonRegistrar.pack(side="left", padx=10)
    # Botón Limpiar
    botonLimpiar = tk.Button(
        marcoBotones, text="Limpiar", bg="#7D7D7D", fg="white", font=("Arial", 10, "bold"), width=12,
        command=lambda: limpiarFormularioDonador(campoCedula, campoNombre, campoFechaNac, variableSexo, campoTelefono, campoCorreo, listaProvincia, campoPeso, listaSangre))
    botonLimpiar.pack(side="left", padx=10)
    # Botón regresas
    botonRegresar = tk.Button(
        marcoBotones, text="Regresar", bg="#A31D1D", fg="white", font=("Arial", 10, "bold"), width=12,command=ventanaFormulario.destroy)
    botonRegresar.pack(side="left", padx=10) # padx hace que los botones no queden tan pegados entre si, le da un espacio horizontal

def ejecutarGuardadoDonador(ventanaFormulario, campoCedula, campoNombre, campoFechaNac, variableSexo, campoTelefono, campoCorreo, listaProvincia, campoPeso, listaSangre):
    """
    Funcionamiento: Recupera los datos de los campos de la interfaz, llama a la función de inserción 
    para guardar el nuevo donador, y muestra el mensaje detallado del resultado.
    """
    cedulaInput = campoCedula.get().strip()
    nombreInput = campoNombre.get().strip()
    fechaNacInput = campoFechaNac.get().strip()
    sexoInput = variableSexo.get()
    telefonoInput = campoTelefono.get().strip()
    correoInput = campoCorreo.get().strip()
    provinciaInput = listaProvincia.get().split(".")[0]
    pesoInput = campoPeso.get().strip()
    sangreInput = listaSangre.get()
    
    exito, mensaje = fn.insertarNuevoDonador(
        cedulaInput, nombreInput, fechaNacInput, sexoInput, 
        telefonoInput, correoInput, provinciaInput, pesoInput, sangreInput
    )
    
    if exito:
        messagebox.showinfo("Operación Exitosa", mensaje, parent=ventanaFormulario)
        ventanaFormulario.destroy()  # Cierra y regresa al menú principal
    else:
        messagebox.showerror("Error de Validación", mensaje, parent=ventanaFormulario)
    # Botón para Registrar Donador
    botontnRegistrar = tk.Button(ventanaFormulario, text="Registrar Donador", bg="#E0631F", fg="white", font=("Arial", 11, "bold"), width=15, command=lambda: ejecutarGuardadoDonador(ventanaFormulario, campoCedula, campoNombre, campoFechaNac, variableSexo, campoTelefono, campoCorreo, listaProvincia, campoPeso, listaSangre)) # command hace que al hacer click en el boton se ejecute la funcion ejecutarGuardado, que es la que recupera los datos de los campos y llama a la funcion de insercion para guardar el nuevo donador, ademas de mostrar un mensaje al usuario con el resultado de la operacion
    botontnRegistrar.pack(pady=20) # pady hace que el boton no quede tan pegado al ultimo campo, le da un espacio vertical

def limpiarFormularioDonador(campoCedula, campoNombre, campoFechaNac, variableSexo, campoTelefono, campoCorreo, listaProvincia, campoPeso, listaSangre):
    """
    Limpia todos los campos del formulario de registro y restablece los valores por defecto.
    """
    campoCedula.delete(0, tk.END)
    campoNombre.delete(0, tk.END)
    campoFechaNac.delete(0, tk.END)
    variableSexo.set("Masculino")
    campoTelefono.delete(0, tk.END)
    campoCorreo.delete(0, tk.END)
    listaProvincia.current(0)
    campoPeso.delete(0, tk.END)
    listaSangre.current(0) # current(0) hace que se seleccione la primera opcion de la lista desplegable

def abrirGenerarDonadores():
    pass # esto es nuevo, esta palabra lo que hace es que no se caiga el codigo, puesto que intentara correr una funcion que todavia no esta implementada

def abrirActualizarDonador():
    pass

def realizarBusquedaParaEliminar(ventanaEliminar, cedulaBuscada, entradaCedula,
                                  botonBuscar, nombreDonador, campoNombre,
                                  fechaNacDonador, campoFechaNac, sexoDonador,
                                  campoSexo, listaJustificacion, botonConfirmar):
    cedulaTexto = cedulaBuscada.get().strip()
    donadorEncontrado = fn.buscarDonadorPorCedula(cedulaTexto)
    if donadorEncontrado is None:
        messagebox.showerror("No Encontrado",
            f"La persona con el número de cédula: {cedulaTexto} no está registrado en la base de datos del Banco de Sangre aún.",
            parent=ventanaEliminar)
        return
    # Verifica que esté activo (índice 9)
    if len(donadorEncontrado) > 9 and donadorEncontrado[9] == 0:
        messagebox.showerror("No Disponible",
            f"El donador con cédula {cedulaTexto} ya fue eliminado del sistema.",
            parent=ventanaEliminar)
        return
    nombreDonador.set(donadorEncontrado[0])
    fechaNacDonador.set(donadorEncontrado[7])
    sexoDonador.set(donadorEncontrado[8])
    campoNombre.config(state="normal")
    campoFechaNac.config(state="normal")
    campoSexo.config(state="normal")
    listaJustificacion.config(state="readonly")
    botonConfirmar.config(state="normal")
    entradaCedula.config(state="disabled")
    botonBuscar.config(state="disabled")

def realizarEliminacionDonador(ventanaEliminar, cedulaBuscada, listaJustificacion):
    cedulaTexto = cedulaBuscada.get().strip()
    if listaJustificacion.current() == -1:
        messagebox.showerror("Error",
            "Debe seleccionar una justificación antes de continuar.",
            parent=ventanaEliminar)
        return
    justificacionTexto = listaJustificacion.get()
    indiceJustificacion = listaJustificacion.current() + 1  # 1 al 7
    confirmacion = messagebox.askyesno(
        "Confirmar eliminación",
        f"¿Está seguro que desea eliminar al donador con cédula {cedulaTexto}?\n\nJustificación:\n{justificacionTexto}",
        parent=ventanaEliminar)
    if confirmacion:
        exito, mensaje = fn.eliminarDonador(cedulaTexto, indiceJustificacion)
        if exito:
            messagebox.showinfo("Éxito", mensaje, parent=ventanaEliminar)
            ventanaEliminar.destroy()
        else:
            messagebox.showerror("Error", mensaje, parent=ventanaEliminar)
    else:
        messagebox.showinfo("Cancelado", "Donador NO eliminado.", parent=ventanaEliminar)

def abrirEliminarDonador():
    ventanaEliminar = tk.Toplevel()
    ventanaEliminar.title("Eliminar Donador")
    ventanaEliminar.geometry("480x520")
    ventanaEliminar.grab_set()
    cedulaBuscada   = tk.StringVar()
    nombreDonador   = tk.StringVar()
    fechaNacDonador = tk.StringVar()
    sexoDonador     = tk.StringVar()
    tk.Label(ventanaEliminar, text="Eliminar Donador",
             font=("Arial", 14, "bold")).pack(pady=10)
    # Sección búsqueda
    marcoBusqueda = tk.LabelFrame(ventanaEliminar, text=" Buscar Donador ", padx=10, pady=10)
    marcoBusqueda.pack(fill="x", padx=20, pady=5)
    tk.Label(marcoBusqueda, text="Digite la cédula (#-####-####):").pack(anchor="w")
    entradaCedula = tk.Entry(marcoBusqueda, width=35, textvariable=cedulaBuscada)
    entradaCedula.pack(pady=2)
    botonBuscar = ttk.Button(marcoBusqueda, text="Buscar Donador")
    botonBuscar.pack(pady=8)
    # Sección datos 
    marcoDatos = tk.LabelFrame(ventanaEliminar, text=" Datos del Donador ", padx=10, pady=10)
    marcoDatos.pack(fill="x", padx=20, pady=5)
    tk.Label(marcoDatos, text="Nombre Completo:", fg="gray").pack(anchor="w")
    campoNombre = tk.Entry(marcoDatos, width=42, textvariable=nombreDonador, state="disabled")
    campoNombre.pack(pady=2)
    tk.Label(marcoDatos, text="Fecha de Nacimiento:", fg="gray").pack(anchor="w")
    campoFechaNac = tk.Entry(marcoDatos, width=42, textvariable=fechaNacDonador, state="disabled")
    campoFechaNac.pack(pady=2)
    tk.Label(marcoDatos, text="Sexo:", fg="gray").pack(anchor="w")
    campoSexo = tk.Entry(marcoDatos, width=42, textvariable=sexoDonador, state="disabled")
    campoSexo.pack(pady=2)
    marcoJustificacion = tk.LabelFrame(ventanaEliminar,
                                        text=" Justificación de Eliminación",
                                        padx=10, pady=10)
    marcoJustificacion.pack(fill="x", padx=20, pady=5)
    tk.Label(marcoJustificacion, text="Seleccione la razón:").pack(anchor="w")
    justificaciones = [
        "1. Enfermedades infecciosas o crónicas (VIH, Hepatitis, Tuberculosis, etc.)",
        "2. Conductas de riesgo (múltiples parejas, relaciones por dinero o drogas)",
        "3. Factores de salud física (anemia, presión inestable, fiebre reciente)",
        "4. Procedimientos médicos recientes (cirugía, tatuajes, transfusiones)",
        "5. Uso de medicamentos inyectables o fármacos restringidos sin receta",
        "6. Estilo de vida o viajes a zonas endémicas (malaria, dengue)",
        "7. Situaciones especiales (embarazo, lactancia, menstruación)"]

    listaJustificacion = ttk.Combobox(marcoJustificacion, values=justificaciones,
                                       width=50, state="disabled")
    listaJustificacion.pack(pady=5)
    marcoBotones = tk.Frame(ventanaEliminar)
    marcoBotones.pack(pady=15)

    botonConfirmar = tk.Button(
        marcoBotones, text="Confirmar Eliminación",
        bg="#A31D1D", fg="white", font=("Arial", 10, "bold"), width=18,
        state="disabled",
        command=lambda: realizarEliminacionDonador(
            ventanaEliminar, cedulaBuscada, listaJustificacion))
    botonConfirmar.pack(side="left", padx=10)

    botonRegresar = tk.Button(
        marcoBotones, text="Regresar",
        bg="#7D7D7D", fg="white", font=("Arial", 10, "bold"), width=12,
        command=ventanaEliminar.destroy)
    botonRegresar.pack(side="left", padx=10)

    botonBuscar.config(command=lambda: realizarBusquedaParaEliminar(
        ventanaEliminar, cedulaBuscada, entradaCedula, botonBuscar,
        nombreDonador, campoNombre, fechaNacDonador, campoFechaNac,
        sexoDonador, campoSexo, listaJustificacion, botonConfirmar))

    entradaCedula.focus_set()

def realizarBusquedaDonador(ventanaActualizar, cedulaBuscada, entradaCedulaBuscar, botonBuscar, nombreDonador, campoNombre, telefonoDonador, campoTelefono, correoDonador, campoCorreo, listaProvincia, pesoDonador, campoPeso, listaSangre, botonConfirmar, tiposSangreOpciones, fechaNacDonador, variableSexoDonador):
    """
    Función encargada de la lógica de búsqueda.
    Recibe los componentes de la interfaz como parámetros para poder interactuar con ellos.
    """
    cedulaAId = cedulaBuscada.get().strip()
    donadorEncontrado = fn.buscarDonadorPorCedula(cedulaAId)
    if donadorEncontrado is None:
        messagebox.showerror("No Encontrado", f"No se encontró ningún donador registrado con la cédula {cedulaAId}.", parent=ventanaActualizar)
        return
    campoNombre.config(state="normal")            
    campoTelefono.config(state="normal")
    campoCorreo.config(state="normal")
    listaProvincia.config(state="readonly")       
    campoPeso.config(state="normal")
    listaSangre.config(state="readonly")
    botonConfirmar.config(state="normal")
    nombreDonador.set(donadorEncontrado[0])         
    telefonoDonador.set(donadorEncontrado[1])
    correoDonador.set(donadorEncontrado[2])    
    try:                                             
        indiceProvincia = int(donadorEncontrado[3]) - 1   
        listaProvincia.current(indiceProvincia)
    except (ValueError, IndexError):
        listaProvincia.current(0)
    pesoDonador.set(str(donadorEncontrado[4]))
    if donadorEncontrado[5] in tiposSangreOpciones:
        listaSangre.set(donadorEncontrado[5])
    if len(donadorEncontrado) > 7:
        fechaNacDonador.set(donadorEncontrado[7])
    if len(donadorEncontrado) > 8:
        variableSexoDonador.set(donadorEncontrado[8])
    entradaCedulaBuscar.config(state="disabled")     
    botonBuscar.config(state="disabled")

def realizarActualizacionDonador(ventanaActualizar, cedulaBuscada, nombreDonador, telefonoDonador, correoDonador, listaProvincia, pesoDonador, listaSangre, fechaNacDonador, variableSexoDonador):
    """
    Funcionamiento: Recupera los datos de las variables de control, llama a la función de 
    actualización y muestra el resultado en pantalla.
    """
    cedulaBuscadaTexto = cedulaBuscada.get().strip() 
    nombreDonadorTexto = nombreDonador.get().strip()
    telefonoDonadorTexto = telefonoDonador.get().strip()
    correoDonadorTexto = correoDonador.get().strip()
    provinciaSeleccionada = listaProvincia.get().split(".")[0].strip()
    pesoDonadorTexto = pesoDonador.get().strip()
    sangreSeleccionada = listaSangre.get().strip()
    fechaNacTexto = fechaNacDonador.get().strip()
    sexoTexto = variableSexoDonador.get().strip()
    exito, mensaje = fn.actualizarDatosDonador(cedulaBuscadaTexto, nombreDonadorTexto, telefonoDonadorTexto, correoDonadorTexto, provinciaSeleccionada, pesoDonadorTexto, sangreSeleccionada, fechaNacTexto, sexoTexto)
    if exito: 
        messagebox.showinfo("Éxito", mensaje, parent=ventanaActualizar) 
        ventanaActualizar.destroy()
    else: 
        messagebox.showerror("Error de Validación", mensaje, parent=ventanaActualizar)

def abrirActualizarDonador():
    """
    Crea una subventana para actualizar los datos de un donador existente.
    """
    ventanaActualizar = tk.Toplevel()
    ventanaActualizar.title("Actualizar Datos de Donador")
    ventanaActualizar.geometry("450x750") 
    ventanaActualizar.grab_set() 
    cedulaBuscada = tk.StringVar()
    nombreDonador = tk.StringVar()
    telefonoDonador = tk.StringVar()
    correoDonador = tk.StringVar()
    pesoDonador = tk.StringVar()
    fechaNacDonador = tk.StringVar()
    variableSexoDonador = tk.StringVar()

    # Diseño del buscador
    lblTitulo = tk.Label(ventanaActualizar, text="Modificar Datos de Donador", font=("Arial", 14, "bold"))
    lblTitulo.pack(pady=10)

    marcoBusqueda = tk.LabelFrame(ventanaActualizar, text=" Buscar Donador ", padx=10, pady=10)
    marcoBusqueda.pack(fill="x", padx=20, pady=5)

    tk.Label(marcoBusqueda, text="Digite la cédula (#-####-####):").pack(anchor="w")
    entradaCedulaBuscar = tk.Entry(marcoBusqueda, width=35, textvariable=cedulaBuscada)
    entradaCedulaBuscar.pack(pady=2)

    botonBuscar = ttk.Button(marcoBusqueda, text="Buscar Donador") 
    botonBuscar.pack(pady=8)

    frmCampos = tk.LabelFrame(ventanaActualizar, text=" Datos del Donador ", padx=10, pady=10)
    frmCampos.pack(fill="both", expand=True, padx=20, pady=5)

    tk.Label(frmCampos, text="Nombre Completo:").pack(anchor="w")
    campoNombre = tk.Entry(frmCampos, width=40, textvariable=nombreDonador, state="disabled") 
    campoNombre.pack(pady=2)

    tk.Label(frmCampos, text="Fecha de Nacimiento (No modificable):", fg="gray").pack(anchor="w")
    campoFechaNac = tk.Entry(frmCampos, width=40, textvariable=fechaNacDonador, state="disabled")
    campoFechaNac.pack(pady=2)

    tk.Label(frmCampos, text="Sexo (No modificable):", fg="gray").pack(anchor="w")
    campoSexo = tk.Entry(frmCampos, width=40, textvariable=variableSexoDonador, state="disabled")
    campoSexo.pack(pady=2)

    tk.Label(frmCampos, text="Teléfono (####-####):").pack(anchor="w")
    campoTelefono = tk.Entry(frmCampos, width=40, textvariable=telefonoDonador, state="disabled")
    campoTelefono.pack(pady=2)

    tk.Label(frmCampos, text="Correo Electrónico:").pack(anchor="w")
    campoCorreo = tk.Entry(frmCampos, width=40, textvariable=correoDonador, state="disabled")
    campoCorreo.pack(pady=2)

    tk.Label(frmCampos, text="Provincia de Residencia:").pack(anchor="w")
    provinciasOpciones = ["1. San José", "2. Alajuela", "3. Cartago", "4. Heredia", "5. Guanacaste", "6. Puntarenas", "7. Limón", "8. Naturalizado"]
    listaProvincia = ttk.Combobox(frmCampos, values=provinciasOpciones, width=37, state="disabled") 
    listaProvincia.pack(pady=2)

    tk.Label(frmCampos, text="Peso en kg (50 - 120):").pack(anchor="w")
    campoPeso = tk.Entry(frmCampos, width=40, textvariable=pesoDonador, state="disabled")
    campoPeso.pack(pady=2)

    tk.Label(frmCampos, text="Tipo de Sangre:").pack(anchor="w")
    tiposSangreOpciones = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
    listaSangre = ttk.Combobox(frmCampos, values=tiposSangreOpciones, width=37, state="disabled")
    listaSangre.pack(pady=2)

    botonConfirmar = ttk.Button(ventanaActualizar, text="Confirmar Cambios", state="disabled") 
    botonConfirmar.pack(pady=15, ipady=2)
    botonBuscar.config(
        command=lambda: realizarBusquedaDonador(
            ventanaActualizar, cedulaBuscada, entradaCedulaBuscar, botonBuscar,
            nombreDonador, campoNombre, telefonoDonador, campoTelefono, correoDonador, campoCorreo,
            listaProvincia, pesoDonador, campoPeso, listaSangre, botonConfirmar, tiposSangreOpciones,
            fechaNacDonador, variableSexoDonador))
    botonConfirmar.config(
        command=lambda: realizarActualizacionDonador(
            ventanaActualizar, cedulaBuscada, nombreDonador, telefonoDonador, correoDonador,
            listaProvincia, pesoDonador, listaSangre, fechaNacDonador, variableSexoDonador))

def ejecutarInsercionLugar(ventanaLugar):
    """
    Función independiente que se ejecuta al dar clic en el botón 'Insertar'.
    Lee los componentes directamente desde los atributos guardados en la ventana.
    """
    # aqui se recuperan los componentes de la pantalla guardados previamente
    listaProvinciaLugar = ventanaLugar.listaProvinciaLugar
    campoNuevoLugar = ventanaLugar.campoNuevoLugar
    
    # aqui se obtienen los valores ingresados por el usuario
    provinciaInput = listaProvinciaLugar.get().split(".")[0] 
    nuevoLugarInput = campoNuevoLugar.get()
    
    # aqui se llama funciones.py para guardar en el diccionario
    exito, mensaje = fn.insertarLugarDonacion(provinciaInput, nuevoLugarInput)
    if exito:
        messagebox.showinfo("Éxito", mensaje, parent=ventanaLugar)
        campoNuevoLugar.delete(0, tk.END) # Limpia la caja de texto para registrar otro hospital
    else:
        messagebox.showerror("Error de Validación", mensaje, parent=ventanaLugar)
        
def abrirInsertarLugar():
    """
    Funcionamiento: Crea la subventana para registrar un nuevo lugar de donación según la provincia.
    """
    ventanaLugar = tk.Toplevel()
    ventanaLugar.title("Insertar Lugar de Donación")
    ventanaLugar.geometry("450x350")
    ventanaLugar.grab_set() # Bloquea la ventana de atrás

    # Título de la subventana
    lblTituloLugar = tk.Label(ventanaLugar, text="Registrar Centro de Donación", font=("Arial", 14, "bold"))
    lblTituloLugar.pack(pady=15)

    # Marco contenedor visual
    marcoLugar = tk.LabelFrame(ventanaLugar, text=" Datos del Lugar ", padx=15, pady=15)
    marcoLugar.pack(fill="both", expand=True, padx=25, pady=5)

    # Selección de provincia
    tk.Label(marcoLugar, text="Seleccione la Provincia:", font=("Arial", 10)).pack(anchor="w")
    provinciasOpciones = ["1. San José", "2. Alajuela", "3. Cartago", "4. Heredia", "5. Guanacaste", "6. Puntarenas", "7. Limón", "8. Naturalizado"]
    
    # Guardamos el combobox como un atributo directo de la ventana
    ventanaLugar.listaProvinciaLugar = ttk.Combobox(marcoLugar, values=provinciasOpciones, width=37, state="readonly")
    ventanaLugar.listaProvinciaLugar.current(0) 
    ventanaLugar.listaProvinciaLugar.pack(pady=5)

    # Área de texto para el nuevo lugar
    tk.Label(marcoLugar, text="Nombre del Nuevo Lugar (Hospital, Clínica, etc):", font=("Arial", 10)).pack(anchor="w", pady=(10, 0))
    
    # Guardamos el entry como un atributo directo de la ventana
    ventanaLugar.campoNuevoLugar = tk.Entry(marcoLugar, width=40)
    ventanaLugar.campoNuevoLugar.pack(pady=5)

    # Contenedor horizontal para los botones de abajo
    marcoBotones = tk.Frame(ventanaLugar)
    marcoBotones.pack(pady=15)

    # Botón Insertar: Llama de forma tradicional pasando la ventana como argumento
    botonInsertar = tk.Button(marcoBotones,text="Insertar", bg="#E0631F", fg="white", font=("Arial", 11, "bold"), width=12, command=lambda: ejecutarInsercionLugar(ventanaLugar))
    botonInsertar.pack(side="left", padx=10)
    # Botón Salir que cierrra de una vez la ventana
    botonSalirLugar = tk.Button(marcoBotones, text="Salir", bg="#707070", fg="white", font=("Arial", 11, "bold"), width=12, command=ventanaLugar.destroy)
    botonSalirLugar.pack(side="left", padx=10)
    ventanaLugar.campoNuevoLugar.focus_set()

def abrirReportes():
    pass

def iniciarPrograma():
    ventanaPrincipal = tk.Tk()
    ventanaPrincipal.title("Banco de Sangre - Sistema de Información")
    ventanaPrincipal.geometry("500x450") 
    
    existeBaseDatos = fn.verificarBaseDatos() # Aqui se verifica si existe la base de datos, lo cual segun tkinter hace que los botones puedan funcionar
    estadoBloqueado = tk.NORMAL if existeBaseDatos else tk.DISABLED

    lblTitulo = tk.Label(ventanaPrincipal, text="Menú Principal", font=("Arial", 16, "bold"))
    lblTitulo.pack(pady=15)

    btnInsertarDonador = tk.Button(ventanaPrincipal, text="1. Insertar donador", width=35, command=abrirInsertarDonador) # command hace que al hacer click en el boton se ejecute la funcion abrirInsertarDonador, que es la que crea la ventana para insertar un nuevo donador
    btnInsertarDonador.pack(pady=5)

    btnGenerarDonadores = tk.Button(ventanaPrincipal, text="2. Generar donadores", width=35, command=abrirGenerarDonadores)
    btnGenerarDonadores.pack(pady=5)

    btnActualizarDonador = tk.Button(ventanaPrincipal, text="3. Actualizar datos del donador", width=35,  command=abrirActualizarDonador)
    btnActualizarDonador.pack(pady=5)

    btnEliminarDonador = tk.Button(ventanaPrincipal, text="4. Eliminar donador", width=35, command=abrirEliminarDonador)
    btnEliminarDonador.pack(pady=5)

    btnInsertarLugar = tk.Button(ventanaPrincipal, text="5. Insertar lugar de donación por provincia", width=35, command=abrirInsertarLugar)
    btnInsertarLugar.pack(pady=5)

    btnReportes = tk.Button(ventanaPrincipal, text="6. Reportes", width=35,  command=abrirReportes)
    btnReportes.pack(pady=5)

    btnSalir = tk.Button(ventanaPrincipal, text="7. Salir", width=35, command=ventanaPrincipal.quit) # por ejemplo, el command de aqui hace que al hacer click en el boton se ejecute la funcion quit de la ventana principal, lo que hace que se cierre el programa
    btnSalir.pack(pady=15)

    ventanaPrincipal.mainloop() #  esto hace que la ventana se mantenga siempre abierta

if __name__ == "__main__": # Esta linea de codigo hace que si este archivo es ejecutado directamente, se ejecute la funcion iniciarPrograma, pero si este archivo es importado como un modulo en otro archivo, no se ejecute iniciarPrograma automaticamente, lo cual es util para evitar que al importar este modulo se abra la ventana del menu principal sin querer
    iniciarPrograma() # se investigo porque el del hacer esto, lo cual hace lo del comentario de arriba

