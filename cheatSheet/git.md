# Git

### Branch

```bash
git branch #Muestra todas las ramas disponibles
git branch --show-current #Muestra la rama actual (en la que estas)
git branch nombreDeRama #Crear la rama "nombreDeRama"
git branch -d nombreDeRama #Eliminar la rama
git branch -D nombreDeRama #Eliminar la rama sin inportar si se mergeo antes o no
```

### Checkout

```bash
git checkout nombreDeRama #Movernos a la rama "nombreDeRama"
git checkout -b nombreDeRama #Crear una rama y nos movemos a ella a la vez
git switch nombreDeRama #Movernos a la rama "nombreDeRama" de la forma actual (es lo mismo pero bue)
git switch -c nombreDeRama #Crear una rama y nos movemos a ella a la vez
```

### Merge

```bash
git merge nombreDeRama #Une la rama "nombreDeRama" a la rama en la que estamos (osea, solo se altera la rama en la que estamos)
git merge --no-ff nombreDeRama #Deja un commit con todos los cambios que se realizaron
```

### Remote

```bash
git remote prune origin --dry-run #Muestra las ramas que se van a borrar (por estar descolgadas, osea, porque ya se mergearon y fueron borradas en el repo remoto pero vos tenes una copia fruta en tu repo local)
git remote prune origin	#Borra todas las ramas no utilizadas
git remote add origin HTTPS/SSH #Para subir un proyecto a un repo remoto (osea empesaste en el local y lo subiste despues)
git remote -v #Para saber cuales repos remotos estan enlazados con el repo local
```

### Log

```bash
git log #Muestra los commits
git log "archivo.txt"	#ver historia del archivo.
git log --oneline #Muestra todos los commits
git log --oneline --decorate --all --graph #Muestra todos los commits pero cortitos de info, mas legible
```

### Blame

```bash
git blame direccionDelArchivo	#Muestra quien modifico ese archivo (hay propiedades para hacer más especifica la busqueda como en que linea(-L 5,10), ignore espacios en blanco (-w),etc)
```

### Clone

```bash
git clone repo #Traerte un repo desde github
git clone --depth=N repo #Especifica la cantidad de commits que quieres clonar del repo (N = 1,2,etc)
```

### Pull

```bash
git pull #Actualiza el repo local con los cambios del repo remoto
git pull --unshallow #Para traerte todo el historial de un repo clonado con --depth
```

### Stash

```bash
git stash	#Los cambios no commitiados son guardados en un almacen temporal
git stash list #Muestra todos los stash guardados
git stash pop	#Trae el ultimo stash guardado
git stash apply N #Lo mismo que pop pero lo concerva guardado en el almacen tambien (N es el numero del stash en el almacen)
git stash drop N #Elimina el stash numero N
git stash clear	#Limpia todo el almacen
```

### Cherry

```bash
git cherry-pick SHA-1 #Agarra uno o varios commits de otra rama para aplicarlos a esta(si son varios hay que listarlos,separados por espacios uno a uno)
git checkout SHA-1 -- nombreDelArchivo #Recupera un archivo del commit indicado
```
