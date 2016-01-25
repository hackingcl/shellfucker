#!/usr/bin/python
#-*- coding:UTF-8 -*-
import os
import sys
from termcolor import colored
import time
import commands
# verificamos si existe el parametro del directorio
if len(sys.argv) == 1:
	print ""
	print colored(" [-] Ingresa un directorio para analizar","red",attrs=['bold'])
	print ""
	exit()
# Directorio a analizar
directorio = sys.argv[2]
try:
	# Total de archivos
	total = []
	# funcion para crear archivo de resultado
	def crear(nombre):
		# Creamos el archivo con el resultado
		resultado = open(nombre, 'a')
		datos     = ""
		# Recorremos el directorio calculando la suma sha1 de todos los archivos
		for (ruta, ficheros, archivos) in os.walk(directorio):
			try:
				for i in xrange(0,len(archivos)):
					archivo      = ruta + "/" + archivos[i]
					comando      = "sudo sha1sum %s" % archivo
					exec_comando = commands.getstatusoutput(comando)
					datos        += exec_comando[1] + "\n"
					total.append(archivo)
			except IndexError:
				# Verificamos si hubo un error en el index del ciclo
				print colored(" [-] Error en el archivo","red",attrs=['bold'])
				print ""
		# Guardamos el resultado
		resultado.write(datos[:-1])
		resultado.close()
	# Funcion para verificar los archivos nuevos y originales
	def comparar():
		# Abrimos los archivos
		abrir_original = open("original.txt")
		abrir_nuevo    = open("nuevo.txt")
		# Leemos los archivos
		lineas_original = abrir_original.readlines()
		lineas_nuevo    = abrir_nuevo.readlines()
		# Arrays
		original = {}
		nuevo    = {}
		# recorremos el archivo original
		for linea_original in lineas_original:
			line_original = linea_original.split("  ")
			original[line_original[1][:-1]] = line_original[0]
		# recorremos el archivo nuevo
		for linea_nuevo in lineas_nuevo:
			line_nuevo = linea_nuevo.split("  ")
			nuevo[line_nuevo[1][:-1]] = line_nuevo[0]
			# verificamos si existe un archivo nuevo
			if line_nuevo[1][:-1] not in original:
				print ""
				print colored(" [>] Nuevo archivo encontrado: --> ","yellow",attrs=['bold']) + line_nuevo[1][:-1]
				print ""
				print colored(" +---------------------------------+","green",attrs=['bold'])
			# verificamos si se ha modificado algun archivo
			if line_nuevo[1][:-1] in original:
				if original[line_nuevo[1][:-1]] != nuevo[line_nuevo[1][:-1]]:
					print ""
					print colored(" [>] archivo modificado: --> ","red",attrs=['bold']) + line_nuevo[1][:-1]
					print ""
					print colored("     SHA1 original : ","green",attrs=['bold']) + original[line_nuevo[1][:-1]]
					print ""					
					print colored("     SHA1 nuevo    : ","cyan",attrs=['bold']) + nuevo[line_nuevo[1][:-1]]
					print ""
					print colored(" +---------------------------------+","green",attrs=['bold'])
		# Terminamos de mostrar los cambios encontrados
		print ""
		print colored(" [+] No se han encontrado mas cambios","blue",attrs=['bold'])
		print ""
	# Funcion de inicio
	def inicio():
		# Mensaje de inicio
		print colored("""
	      ╔═══╗╔╗      ╔╗ ╔╗  ╔═══╗        ╔╗
	      ║╔═╗║║║      ║║ ║║  ║╔══╝        ║║
	      ║╚══╗║╚═╗╔══╗║║ ║║  ║╚══╗╔╗╔╗╔══╗║║╔╗╔══╗╔═╗
	      ╚══╗║║╔╗║║║═╣║║ ║║  ║╔══╝║║║║║╔═╝║╚╝╝║║═╣║╔╝
	      ║╚═╝║║║║║║║═╣║╚╗║╚╗ ║║   ║╚╝║║╚═╗║╔╗╗║║═╣║║
	      ╚═══╝╚╝╚╝╚══╝╚═╝╚═╝ ╚╝   ╚══╝╚══╝╚╝╚╝╚══╝╚╝
		          v1.0 by @unkndown
		""","blue", attrs=['bold'])
		if sys.argv[1] == "verificar":
			print colored(" [+] Iniciando analisis","yellow",attrs=['bold'])
			print ""
			print colored(" [+] Iniciando nuevo calculo SHA1 de los archivos","yellow",attrs=['bold'])
			print ""
			# Creamos el archivo de resultados
			crear("nuevo.txt")		
			# Estadisticas 
			print colored(" [+] Nuevo calculo terminado","green",attrs=['bold'])
			print ""
			print colored(" [+] Total de los archivos analizados: ","green",attrs=['bold']) + str(len(total))
			print ""
			print colored(" [+] Comparando los resultados ","blue",attrs=['bold'])
			print colored(" +---------------------------------+","green",attrs=['bold'])
		elif sys.argv[1] == "original":
			print colored(" [+] Iniciando analisis","yellow",attrs=['bold'])
			print ""
			print colored(" [+] Iniciando calculo SHA1 de los archivos","yellow",attrs=['bold'])
			print ""
			# Creamos el archivo de resultados
			crear("original.txt")
			# Estadisticas 
			print colored(" [+] Calculo terminado","green",attrs=['bold'])
			print ""
			print colored(" [+] Total de los archivos analizados: ","green",attrs=['bold']) + str(len(total))
			print ""
	# Iniciamos el script
	if __name__ == '__main__':
	    inicio()
	    if sys.argv[1] == "verificar":
	    	comparar()
except KeyboardInterrupt:
	print colored(" [+] Analisis cancelado","red",attrs=['bold'])
	print ""
