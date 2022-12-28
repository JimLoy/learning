# Bash

### Basic

```bash
COMANDO --help #Muestra las flags que se le puede aplicar al comando
alias COMANDO=' ' #Guarda un comando hasta que se muera la terminal
sudo #Da permisos de super administrador (superuser do)
clear #Limpia la terminal

pwd #Directorio actual
ls #Directoriolista de directorios/archivos que hay en el directorio en donde estas
cd DIRECTORIO #Mover entre directorios
cd - #Devuelve al directorio en el que estabas

touch NOMBRE			#Crea un archivo vacio
mkdir NOMBRE			#Crea un directorio (-p para concatenar nombres, carpeta inception)

cat ARCHIVO #Abre el contenido del archivo
less ARCHIVO #Muestra el contenido del archivo en partes (se sale con q, se baja con SPACE)
```

### Symbols

```bash
.   #Es el directorio actual
..  #Directorio anterior
~		#El directorio de tu usuario
CMD1 | CMD2	#(pipe)indica que la salida del CMD1 lo va a procesar el CMD2
echo "hola" > p.txt		#Remplaza el texto del archivo p (y lo crea si es que no exixtia) por hola
echo "hola" >> p.txt		#Agrega el texto hola al archivo p
```

### Echo

```bash
echo "sahgdf"	#Devuelve lo escrito
```

### Move

```bash
mv ORIGEN DESTINO		#Mueve el archivo o carpeta del origen al destino (tambien puede cambiarle el nombre)
```

### Remove

```bash
rm ARCHIVO			#Borra el archivo
rm ARCHIVO -i       #Pregunta si estas seguro de borrar
rm -r DIRECTORIO	#Borra el directorio y todo su contenido
```

### Copy

```bash
cp ORIGEN DESTINO		  #Copia un archivo desde el origen al destino
cp -r ORIGEN DESTINO	  #Copia directorios
```

### Find

```bash
find DIRECTORIO -name NOMBRE     #Busca el archivo o carpeta desde donde se indica hasta sus hijos
find DIRECTORIO -iname NOMBRE	 #No le importa las mayusculas
```

https://explainshell.com/explain?cmd=pwd
