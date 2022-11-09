//Compilar el archivo a js               npx tsc nombreDelArchivo.ts
//Crear el archivo de configuracion      npx tsc --init

//DESCARGAR @TYPES/ LA LIBRERIA QUE VAS A USAR

//---------------------------UNKNOWN
//Se le pueden asignar valores pero no tipos
//tampoco llamar sus metodos. ej:  unStr.method123()
let unStr: unknown;
const str: string = unStr as string; //Tipado Explicito

//---------------------------ANY
//Desabilita los checkeos de ts
//es basicamente tratar a la variable como en js

//---------------------------ARRAY
const numArr: number[] = [5, 6, 8, 54, 32, 9, 8];
const strArr: string[] = ['hola', 'como', 'estas', '?'];
const loMismoPeroConUnaSyntaxisRara: Array<number> = [5, 6, 8, 54, 32, 9, 8];

//---------------------------TUPLE
//Son arrays pero con cantidades fijas
const tuple: [string, number] = ['Lucas', 82];

//---------------------------OBJECTS
//Clases basicamente
interface Persona {
	nombre: string;
	apellido: string;
	edad?: number; //? significa que es opcional
}

const juan: Persona = {
	nombre: 'Juan',
	apellido: 'Moldes',
	edad: 20,
};

interface Estudiante extends Persona {
	isActivo: boolean;
}

const jim: Estudiante = {
	nombre: 'Jim',
	apellido: 'Loy',
	edad: 22,
	isActivo: true,
};

//---------------------------CLASS
//Las variables (propiedades) de las clases son publicas (se pueden usar desde afuera)
//las privadas solo se pueden usar dentro de la clase (como el getEdad)
//las protegidas solo las pueden usar la  misma clase y sus hijas
class Person {
	nombre: string; //publica
	private edad: number; //privada
	protected email: string; //protegida
	constructor(nombre: string, edad: number, email: string) {
		this.nombre = nombre;
		this.edad = edad;
		this.email = email;
	}
	getEdad() {
		return this.edad;
	}
}

//---------------------------FUNCTIONS
//function nameFunction(parameterOne: typeOne, ...): typeReturn
function suma(a: number, b: number): number {
	return a + b;
}
const result = suma(5, 4);

//Type void son las funciones que no retornan nada (que no tinen return)
function consolea(): void {
	console.log('alsda');
}

//Type never son funciones que cortan la ejecucion, son para errores
function thorwError(msg: string): never {
	throw new Error(msg);
}

//El Narrowing te da la posibilidad de poner un or en el type de las variables
function suma2(a: number | string, b: number | string): number | string | void {
	if (typeof a === 'number' && typeof b === 'number') return a + b;
	if (typeof a === 'string' && typeof b === 'string') return a + b;
}

//Generic Function
//para Array
const arrNum = [1, 5, 2];
const arrStr = ['1', '5', '2'];
function firstElement<T>(arr: T[]): T {
	return arr[0];
}
const casoNum = firstElement(arrNum); //typado implicito
const casoStr = firstElement<string>(arrStr); //typado explicito
//para object
function merge<U extends object, V extends object>(obj1: U, obj2: V) {
	return {
		...obj1,
		...obj2,
	};
}
merge({ name: 'hoas' }, { age: 92 });

//Function overload
//Las formas distintas que uno tiene para llamar functions
/*
function sume(a: number,b: string): string;
function sume(a: string,b: string): string;
function sume(a: string,b: number): string;
function sume(a: number,b: number): number {
	return a + b;
}
*/
