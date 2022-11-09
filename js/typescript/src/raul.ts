import raules from './raules.json';
import { PersonRaul } from './type';

const raul: PersonRaul[] = raules as PersonRaul[];
//si esto da error hay que agregar esto (as PersonRaul[]) al final para forzar el tipo
console.log(raul);
