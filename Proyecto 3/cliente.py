# PROYECTO 3

# DESCRIPCIÓN: Cliente que probará el correcto funcionamiento de
# la implementación de la aplicación de mensajeria ALGOGRAM

# AUTORES: Jesus Kauze y David Segura
# EMAILS: 12-10273@usb.ve y 13-11341@usb.ve

from usuario import Usuario
from registro_usuarios import RegistroUsuarios
from prueba import h1
#from chat import Chat
#from conversaciones import Conversaciones


Registro = RegistroUsuarios()
Registro.crearTabla(1000)
while True:
	print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*\n"+
		"* ALGOGRAM by David&Kauze           *\n"+
		"* (1) Registrarse                   *\n"+
		"* (2) Iniciar sesión                *\n"+
		"* (3) Cargar usuarios               *\n"+
		"* (4) Eliminar usuario              *\n"+
		"* (5) Cargar caritas                *\n"+
		"*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
	opcion = input("~~~~> INTRODUCIR OPCIÓN: ")
	if int(opcion) == 1:
		print("~~~~REGISTRARSE~~~~")
		nombre = input("> Nombre: ")
		contrasena = input("> Contraseña: ")
		telefono = input("> Teléfono: ")
		p = Usuario()
		error = True
		if p.crearUsuario(nombre,contrasena,telefono,None) == True:
			validar = Registro.agregarUsuario(p)
		else:
			error = False
		if error == False:
			print(">>> Usuario no creado.")
		else:
			if validar == False:
				print(">>> ERROR: Ya existe un usuario registrado con ese nombre.")
			else:
				print(">>> Usuario creado.")
		continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
	elif int(opcion) == 2:
		print("~~~~INICIAR SESIÓN~~~~")
		nombre = input("> Nombre: ")
		contrasena = input("> Contraseña: ")
		key = h1(nombre) % len(Registro.tablaRU)

		lista = Registro.tablaRU[key]
		menu = False
		while lista != None:
			if lista.element.nombre == nombre:
				if lista.element.password == contrasena:
					menu = True
					while True:
						print(">>> SESIÓN: "+lista.element.nombre+" <<<\n"
							"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"+
							"| (1) Agregar Contacto              |\n"+
							"| (2) Eliminar Contacto             |\n"+
							"| (3) Mostrar Contactos             |\n"+
							"| (4) Ver Conversación              |\n"+
							"| (5) Enviar Mensaje                |\n"+
							"| (6) Mostrar Caritas               |\n"+
							"| (7) Mostrar Usuarios Registrados  |\n"+
							"| (8) Cerrar Sesión                 |\n"
							"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
						opcion = input("~~~~> INTRODUCIR OPCIÓN: ")
				else:
					print(">>> ERROR: CONTRASEÑA INCORRECTA")
			else:
				lista = lista.next
		if menu == True:
			pass
		else:
			print(">>> ERROR: USUARIO NO ENCONTRADO")
			continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")
	else:
		print(">>> ERROR: Opción Inválida")
		continuar = input("~~~~~~~~PRESIONE ENTER PARA CONTINUAR~~~~~~~~")