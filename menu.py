# elaborado por: Alessandro Arias y Gabriel Muñoz
# fecha de elaboracion: mayo 19 de 2026
#  versionn de pyhton: 3.14.3
# hora de ultima actualizacion: 

# librerias importadas
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importamos ttk para usar Combobox, que es una lista desplegable más moderna y estilizada
import funciones as fn # quisimos abreviarla, puesto que poner .funciones en todo lado se hace mas largo todo

def abrirInsertarDonador():
    """
    Crea una subventana (Toplevel) para capturar los datos del nuevo donador
    """
    ventanaFormulario = tk.Toplevel()
    ventanaFormulario.title("Registrar Nuevo Donador")                              # crea la ventana para el formulario de registro de donadores
    ventanaFormulario.geometry("450x550")
    ventanaFormulario.grab_set()  # Bloquea la ventana principal mientras esta este abierta

    # Título de la subventana
    lblFormulario = tk.Label(ventanaFormulario, text="Formulario de Inscripción", font=("Arial", 14, "bold"))
    lblFormulario.pack(pady=10)

    # Campo: Cédula
    tk.Label(ventanaFormulario, text="Cédula (#-####-####):", font=("Arial", 10)).pack(anchor="w", padx=40)
    txtCedula = tk.Entry(ventanaFormulario, width=40)                       # este es el campo de texto para la cedula, se le asigna a una variable para luego recuperar su valor al momento de guardar el donador
    txtCedula.pack(pady=3)

    # Campo: Nombre Completo
    tk.Label(ventanaFormulario, text="Nombre Completo:", font=("Arial", 10)).pack(anchor="w", padx=40)
    txtNombre = tk.Entry(ventanaFormulario, width=40)
    txtNombre.pack(pady=3)

    # Campo: Teléfono
    tk.Label(ventanaFormulario, text="Teléfono (####-####):", font=("Arial", 10)).pack(anchor="w", padx=40)
    txtTelefono = tk.Entry(ventanaFormulario, width=40)
    txtTelefono.pack(pady=3)

    # Campo: Correo Electrónico
    tk.Label(ventanaFormulario, text="Correo Electrónico:", font=("Arial", 10)).pack(anchor="w", padx=40)
    txtCorreo = tk.Entry(ventanaFormulario, width=40)
    txtCorreo.pack(pady=3)

    # Campo: Provincia (Lista Desplegable)
    tk.Label(ventanaFormulario, text="Provincia de Residencia:", font=("Arial", 10)).pack(anchor="w", padx=40)
    provinciasOpciones = ["1. San José", "2. Alajuela", "3. Cartago", "4. Heredia", "5. Guanacaste", "6. Puntarenas", "7. Limón", "8. Naturalizado"]
    cmbProvincia = ttk.Combobox(ventanaFormulario, values=provinciasOpciones, width=37, state="readonly") # aqui se usa el combobox para mostrar la lista de provincias, se le asigna a una variable para luego recuperar su valor al momento de guardar el donador
    cmbProvincia.current(0) # selecciona por defecto la provincia de san jose para evitar que al registrarlo el campo quede vacio
    cmbProvincia.pack(pady=3)

    # Campo: Peso
    tk.Label(ventanaFormulario, text="Peso en kg (50 - 120):", font=("Arial", 10)).pack(anchor="w", padx=40)
    txtPeso = tk.Entry(ventanaFormulario, width=40)
    txtPeso.pack(pady=3)

    # Campo: Tipo de Sangre (Lista Desplegable)
    tk.Label(ventanaFormulario, text="Tipo de Sangre:", font=("Arial", 12)).pack(anchor="w", padx=40)
    tiposSangreOpciones = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
    cmbSangre = ttk.Combobox(ventanaFormulario, values=tiposSangreOpciones, width=37, state="readonly")
    cmbSangre.current(0)
    cmbSangre.pack(pady=3)

    def ejecutarGuardado():
        """
        Recupera las variables de los campos y llama a la función de inserción, mostrando el resultado al usuario.
        """
        cedulaInput = txtCedula.get()
        nombreInput = txtNombre.get()
        telefonoInput = txtTelefono.get()
        correoInput = txtCorreo.get()
        provinciaInput = cmbProvincia.get().split(".")[0]
        pesoInput = txtPeso.get()
        sangreInput = cmbSangre.get()
        
        exito, mensaje = fn.insertarNuevoDonador(
            cedulaInput, nombreInput, telefonoInput, correoInput, provinciaInput, pesoInput, sangreInput)
        if exito:
            messagebox.showinfo("Operación Exitosa", mensaje, parent=ventanaFormulario)
            ventanaFormulario.destroy() # Cerramos la ventana al completarse exitosamente
        else:
            messagebox.showerror("Error de Validación", mensaje, parent=ventanaFormulario)

    # Botón para Registrar Donador
    botontnRegistrar = tk.Button(ventanaFormulario, text="Registrar Donador", bg="#E0631F", fg="white", font=("Arial", 11, "bold"), width=25, command=ejecutarGuardado)
    botontnRegistrar.pack(pady=20) # pady hace que el boton no quede tan pegado al ultimo campo, le da un espacio vertical

def abrirGenerarDonadores():
    pass # esto es nuevo, esta palabra lo que hace es que no se caiga el codigo, puesto que intentara correr una funcion que todavia no esta implementada

def abrirActualizarDonador():
    pass

def abrirEliminarDonador():
    pass

def abrirInsertarLugar():
    pass

def abrirReportes():
    pass

def iniciarPrograma():
    ventanaPrincipal = tk.Tk()
    ventanaPrincipal.title("Banco de Sangre - Sistema de Información")
    ventanaPrincipal.geometry("500x450")
    
    existeBaseDatos = fn.verificarBaseDatos()
    estadoBloqueado = tk.NORMAL if existeBaseDatos else tk.DISABLED

    lblTitulo = tk.Label(ventanaPrincipal, text="Menú Principal", font=("Arial", 16, "bold"))
    lblTitulo.pack(pady=15)

    btnInsertarDonador = tk.Button(ventanaPrincipal, text="1. Insertar donador", width=35, command=abrirInsertarDonador) # command hace que al hacer click en el boton se ejecute la funcion abrirInsertarDonador, que es la que crea la ventana para insertar un nuevo donador
    btnInsertarDonador.pack(pady=5)

    btnGenerarDonadores = tk.Button(ventanaPrincipal, text="2. Generar donadores", width=35, command=abrirGenerarDonadores)
    btnGenerarDonadores.pack(pady=5)

    btnActualizarDonador = tk.Button(ventanaPrincipal, text="3. Actualizar datos del donador", width=35, state=estadoBloqueado, command=abrirActualizarDonador)
    btnActualizarDonador.pack(pady=5)

    btnEliminarDonador = tk.Button(ventanaPrincipal, text="4. Eliminar donador", width=35, state=estadoBloqueado, command=abrirEliminarDonador)
    btnEliminarDonador.pack(pady=5)

    btnInsertarLugar = tk.Button(ventanaPrincipal, text="5. Insertar lugar de donación por provincia", width=35, command=abrirInsertarLugar)
    btnInsertarLugar.pack(pady=5)

    btnReportes = tk.Button(ventanaPrincipal, text="6. Reportes", width=35, state=estadoBloqueado, command=abrirReportes)
    btnReportes.pack(pady=5)

    btnSalir = tk.Button(ventanaPrincipal, text="7. Salir", width=35, command=ventanaPrincipal.quit) # por ejemplo, el command de aqui hace que al hacer click en el boton se ejecute la funcion quit de la ventana principal, lo que hace que se cierre el programa
    btnSalir.pack(pady=15)

    ventanaPrincipal.mainloop()

if __name__ == "__main__":
    iniciarPrograma() 
