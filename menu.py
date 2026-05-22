# elaborado por: Alessandro Arias y Gabriel Muñoz
# fecha de elaboracion: mayo 19 de 2026
#  versionn de pyhton: 3.14.3
# hora de ultima actualizacion: 6:55 pm del jueves 21 de mayo 2026

# librerias importadas
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importamos ttk para usar Combobox, que es una lista desplegable más moderna y estilizada
import funciones as fn # quisimos abreviarla, puesto que poner .funciones en todo lado se hace mas largo todo

def abrirInsertarDonador():
    """
    Crea una subventana para capturar los datos del nuevo donador
    """
    ventanaFormulario = tk.Toplevel()
    ventanaFormulario.title("Registrar Nuevo Donador")   # crea la ventana para el formulario de registro de donadores
    ventanaFormulario.geometry("450x550")
    ventanaFormulario.grab_set()  # Bloquea la ventana principal mientras esta este abierta

    # Título de la subventana
    lblFormulario = tk.Label(ventanaFormulario, text="Formulario de Inscripción", font=("Arial", 14, "bold"))
    lblFormulario.pack(pady=10)

    # Campo: Cédula
    tk.Label(ventanaFormulario, text="Cédula (#-####-####):", font=("Arial", 10)).pack(anchor="w", padx=40)
    txtCedula = tk.Entry(ventanaFormulario, width=40)      # este es el campo de texto para la cedula, se le asigna a una variable para luego recuperar su valor al momento de guardar el donador
    txtCedula.pack(pady=3)

    # Campo: Nombre Completo
    tk.Label(ventanaFormulario, text="Nombre Completo:", font=("Arial", 10)).pack(anchor="w", padx=40)
    campoNombre = tk.Entry(ventanaFormulario, width=40)
    campoNombre.pack(pady=3)

    # Campo: Teléfono
    tk.Label(ventanaFormulario, text="Teléfono (####-####):", font=("Arial", 10)).pack(anchor="w", padx=40)
    campoTelefono = tk.Entry(ventanaFormulario, width=40)
    campoTelefono.pack(pady=3)

    # Campo: Correo Electrónico
    tk.Label(ventanaFormulario, text="Correo Electrónico:", font=("Arial", 10)).pack(anchor="w", padx=40)
    campoCorreo = tk.Entry(ventanaFormulario, width=40)
    campoCorreo.pack(pady=3)

    # Campo: Provincia (Lista Desplegable)
    tk.Label(ventanaFormulario, text="Provincia de Residencia:", font=("Arial", 10)).pack(anchor="w", padx=40)
    provinciasOpciones = ["1. San José", "2. Alajuela", "3. Cartago", "4. Heredia", "5. Guanacaste", "6. Puntarenas", "7. Limón", "8. Naturalizado"]
    listaProvincia = ttk.Combobox(ventanaFormulario, values=provinciasOpciones, width=37, state="readonly") # aqui se usa el combobox para mostrar la lista de provincias, se le asigna a una variable para luego recuperar su valor al momento de guardar el donador
    listaProvincia.current(0) # selecciona por defecto la provincia de san jose para evitar que al registrarlo el campo quede vacio
    listaProvincia.pack(pady=3)

    # Campo: Peso
    tk.Label(ventanaFormulario, text="Peso en kg (50 - 120):", font=("Arial", 10)).pack(anchor="w", padx=40)
    campoPeso = tk.Entry(ventanaFormulario, width=40)
    campoPeso.pack(pady=3)

    # Campo: Tipo de Sangre (Lista Desplegable)
    tk.Label(ventanaFormulario, text="Tipo de Sangre:", font=("Arial", 12)).pack(anchor="w", padx=40)
    tiposSangreOpciones = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
    listaSangre = ttk.Combobox(ventanaFormulario, values=tiposSangreOpciones, width=37, state="readonly")
    listaSangre.current(0)
    listaSangre.pack(pady=3)

    def ejecutarGuardado(): # revisar ahora
        """
        funcionamiento: Recupera los datos de los campos, llama a la función de inserción para guardar el nuevo donador, y muestra un mensaje al usuario con el resultado de la operación
        """
        cedulaInput = txtCedula.get()
        nombreInput = campoNombre.get()
        telefonoInput = campoTelefono.get()
        correoInput = campoCorreo.get()
        provinciaInput = listaProvincia.get().split(".")[0]
        pesoInput = campoPeso.get()
        sangreInput = listaSangre.get()
        
        exito, mensaje = fn.insertarNuevoDonador(
            cedulaInput, nombreInput, telefonoInput, correoInput, provinciaInput, pesoInput, sangreInput)
        if exito:
            messagebox.showinfo("Operación Exitosa", mensaje, parent=ventanaFormulario)
            ventanaFormulario.destroy() # Cerramos la ventana al completarse exitosamente
        else:
            messagebox.showerror("Error de Validación", mensaje, parent=ventanaFormulario)

    # Botón para Registrar Donador
    botontnRegistrar = tk.Button(ventanaFormulario, text="Registrar Donador", bg="#E0631F", fg="white", font=("Arial", 11, "bold"), width=15, command=ejecutarGuardado) # command hace que al hacer click en el boton se ejecute la funcion ejecutarGuardado, que es la que recupera los datos de los campos y llama a la funcion de insercion para guardar el nuevo donador, ademas de mostrar un mensaje al usuario con el resultado de la operacion
    botontnRegistrar.pack(pady=20) # pady hace que el boton no quede tan pegado al ultimo campo, le da un espacio vertical

def abrirGenerarDonadores():
    pass # esto es nuevo, esta palabra lo que hace es que no se caiga el codigo, puesto que intentara correr una funcion que todavia no esta implementada

def abrirActualizarDonador():
    pass

def abrirEliminarDonador(): # q
    pass

def realizarBusquedaDonador(ventanaActualizar, cedulaBuscada, entradaCedulaBuscar, btnBuscar, nombreDonador, campoNombre, telefonoDonador, campoTelefono, correoDonador, campoCorreo, listaProvincia, pesoDonador, campoPeso, listaSangre, btnConfirmar, tiposSangreOpciones):
    """
    Función independiente encargada de la lógica de búsqueda.
    Recibe los componentes de la interfaz como parámetros para poder interactuar con ellos.
    """
    cedulaAId = cedulaBuscada.get().strip()
    donadorEncontrado = fn.buscarDonadorPorCedula(cedulaAId)

    if donadorEncontrado is None:
        messagebox.showerror("No Encontrado", f"No se encontró ningún donador registrado con la cédula {cedulaAId}.", parent=ventanaActualizar)
        return
    campoNombre.config(state="normal")            # .config hace que el campo de texto se vuelva editable
    campoTelefono.config(state="normal")
    campoCorreo.config(state="normal")
    listaProvincia.config(state="readonly")        # aqui readonly hace que solo se pueda leer y seleciconar de una lista
    campoPeso.config(state="normal")
    listaSangre.config(state="readonly")
    btnConfirmar.config(state="normal")
    nombreDonador.set(donadorEncontrado[0])         # aqui se asignan los valores del donador encontrado a las variables que estan vinculadas a los campos de texto
    telefonoDonador.set(donadorEncontrado[1])
    correoDonador.set(donadorEncontrado[2])
    try:                                             # aqui se hace un intento de convertir la provincia del donador encontrado a un indice para seleccionarlo en la lista desplegable, si por alguna razon no se puede hacer esto (por ejemplo, si el valor de la provincia no es un numero o no esta en el formato esperado), se selecciona por defecto la primera opcion de la lista 
        indiceProvincia = int(donadorEncontrado[3]) - 1   
        listaProvincia.current(indiceProvincia)
    except (ValueError, IndexError):
        listaProvincia.current(0)
    pesoDonador.set(str(donadorEncontrado[4]))
    if donadorEncontrado[5] in tiposSangreOpciones:
        listaSangre.set(donadorEncontrado[5])
    entradaCedulaBuscar.config(state="disabled")     # aqui se bloquea la barra de búsqueda superior para evitar que se busque otro donador
    btnBuscar.config(state="disabled")

def realizarActualizacionDonador(ventanaActualizar, cedulaBuscada, nombreDonador, telefonoDonador, correoDonador, listaProvincia, pesoDonador, listaSangre):
    """
    Funcinamiento: Recupera los datos de los campos, llama a la función de actualización para modificar el donador, y muestra un mensaje al usuario con el resultado de la operación
    Entradas: ventanaActualizar (para mostrar mensajes), cedulaBuscada (para identificar el donador a actualizar), nombreDonador, telefonoDonador, correoDonador, listaProvincia, pesoDonador, listaSangre (para obtener los nuevos datos del donador)
    Salida: Muestra un mensaje de éxito o error dependiendo del resultado de la actualización
    """
    cedulaInput = cedulaBuscada.get().strip() # se obtiene la cedula del donador a actualizar, se le hace strip para eliminar espacios al inicio o final, lo cual puede causar problemas al buscar el donador en el diccionario global
    nombreInput = nombreDonador.get()
    telefonoInput = telefonoDonador.get()
    correoInput = correoDonador.get()
    provinciaInput = listaProvincia.get().split(".")[0]
    pesoInput = pesoDonador.get()
    sangreInput = listaSangre.get()
    exito, mensaje = fn.actualizarDatosDonador(cedulaInput, nombreInput, telefonoInput, correoInput, provinciaInput, pesoInput, sangreInput)
    if exito: # si la actualización fue exitosa, se muestra un mensaje de éxito y se cierra la ventana de actualización, de lo contrario, se muestra un mensaje de error y la ventana permanece abierta para que el usuario pueda corregir los datos
        messagebox.showinfo("Éxito", mensaje,parent=ventanaActualizar) # showinfo muestra mensaje de informaciion, en este caso se usa para mostrar el mensaje de exito
        ventanaActualizar.destroy()                         # se cierra la ventana de actualización al completar exitosamente la actualización del donador
    else:
        messagebox.showerror("Error", mensaje,parent=ventanaActualizar)

def abrirActualizarDonador():
    """
    funcionamiento: Crea una subventana para actualizar los datos de un donador existente. Permite buscar al donador por cédula, mostrar sus datos actuales en campos editables, y confirmar los cambios para actualizar la información del donador.
    entradas: ninguna, pero dentro de la función se crean variables y componentes de la interfaz para manejar la actualización de datos del donador
    salida: la ventana de actualización
    """
    ventanaActualizar = tk.Toplevel()
    ventanaActualizar.title("Actualizar Datos de Donador")
    ventanaActualizar.geometry("450x650")
    
    # se declaran las variables para mostar en el menu
    cedulaBuscada = tk.StringVar()
    nombreDonador = tk.StringVar()
    telefonoDonador = tk.StringVar()
    correoDonador = tk.StringVar()
    pesoDonador = tk.StringVar()

    # esta es la parte de diseño del submenu
    lblTitulo = tk.Label(ventanaActualizar, text="Modificar Datos de Donador", font=("Arial", 14, "bold"))
    lblTitulo.pack(pady=10)

    marcoBusqueda = tk.LabelFrame(ventanaActualizar, text=" Buscar Donador ", padx=10, pady=10)
    marcoBusqueda.pack(fill="x", padx=20, pady=5)

    tk.Label(marcoBusqueda, text="Digite la cédula (#-####-####):").pack(anchor="w")
    entradaCedulaBuscar = tk.Entry(marcoBusqueda, width=35, textvariable=cedulaBuscada)
    entradaCedulaBuscar.pack(pady=2)

    btnBuscar = ttk.Button(marcoBusqueda, text="Buscar Donador")
    btnBuscar.pack(pady=8)

    # aqui se le muestra al usuario los campos de datos del donador, los cuales puede modificar a gusto de el
    frmCampos = tk.LabelFrame(ventanaActualizar, text=" Datos Modificables ", padx=10, pady=10)
    frmCampos.pack(fill="both", expand=True, padx=20, pady=5)

    tk.Label(frmCampos, text="Nombre Completo:").pack(anchor="w")
    campoNombre = tk.Entry(frmCampos, width=40, textvariable=nombreDonador, state="disabled") # se pone state en disable para que el usuario no pueda escrir nada sin antes poner el numero de cedula del donador
    campoNombre.pack(pady=2)

    tk.Label(frmCampos, text="Teléfono con el siguiente formato: (####-####):").pack(anchor="w")
    campoTelefono = tk.Entry(frmCampos, width=40, textvariable=telefonoDonador, state="disabled")
    campoTelefono.pack(pady=2)

    tk.Label(frmCampos, text="Correo Electrónico:").pack(anchor="w")
    campoCorreo = tk.Entry(frmCampos, width=40, textvariable=correoDonador, state="disabled")
    campoCorreo.pack(pady=2)

    tk.Label(frmCampos, text="Provincia de Residencia:").pack(anchor="w")
    provinciasOpciones = ["1. San José", "2. Alajuela", "3. Cartago", "4. Heredia", "5. Guanacaste", "6. Puntarenas", "7. Limón", "8. Naturalizado"]
    listaProvincia = ttk.Combobox(frmCampos, values=provinciasOpciones, width=37, state="disabled") # se usa combobox para mostrar la lista de provincias
    listaProvincia.pack(pady=2)

    tk.Label(frmCampos, text="Peso en kg (50 - 120):").pack(anchor="w")
    campoPeso = tk.Entry(frmCampos, width=40, textvariable=pesoDonador, state="disabled")
    campoPeso.pack(pady=2)

    tk.Label(frmCampos, text="Tipo de Sangre:").pack(anchor="w")
    tiposSangreOpciones = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
    listaSangre = ttk.Combobox(frmCampos, values=tiposSangreOpciones, width=37, state="disabled")
    listaSangre.pack(pady=2)

    # boton de confirmar cambios
    btnConfirmar = ttk.Button(ventanaActualizar, text="Confirmar Cambios", state="disabled")
    btnConfirmar.pack(pady=15, ipady=2)

    # se usa lambda para crear una funcion anonima que congela la ejecucion ,de lo contrario, python ejecutaria la busqueda de inmediato al abrir la ventana
    btnBuscar.config(
        command=lambda: realizarBusquedaDonador(
            ventanaActualizar, cedulaBuscada, entradaCedulaBuscar, btnBuscar,
            nombreDonador, campoNombre, telefonoDonador, campoTelefono, correoDonador, campoCorreo,
            listaProvincia, pesoDonador, campoPeso, listaSangre, btnConfirmar, tiposSangreOpciones
        )
  )

    btnConfirmar.config(
        command=lambda: realizarActualizacionDonador(
            ventanaActualizar, cedulaBuscada, nombreDonador, telefonoDonador, correoDonador,
            listaProvincia, pesoDonador, listaSangre
        )
    )

    entradaCedulaBuscar.focus_set()

def abrirInsertarLugar():
    pass

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
