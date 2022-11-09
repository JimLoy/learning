//Aca se deben guardar todos los tipos del proyecto.
//El nombre del archivo es obligatorio.

type Id = number;
type Name = 'raul';
type Age = number;

//Usar type cuando sean valores fijos e interface para objetos que van a extenderse (por las dudas a los objetos interface y al resto type)

export interface PersonRaul {
	id: Id;
	name: Name;
	age: Age;
}

//export type PersonRaulJuventud = Pick<PersonRaul, 'id' | 'name'>
//or
export type PersonRaulJuventud = Omit<PersonRaul, 'age'>;
