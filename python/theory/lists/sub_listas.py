lista = ['python','JavaScript','Rust','Node','Go']

sub_lista = lista[0:3] #['python','JavaScript','Rust']
#sub_lista = lista[0:10000] toma todos los valores sin romper
print(sub_lista)

#[start:end:skip] todos son opcionales
#lista[1:] toma desde el indice 1 para adelante
#lista[:4] toma todos los valores hasta el indice 3
#lista[0:3:2] el dos son los saltos (osea uno si y otro no)


lista2 = lista[::-1] #la misma lista pero invertido el orden