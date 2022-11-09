#Son funciones que se ejecutan en una sola linea y es anonima, porque haces cosas chicas
function_grads = lambda grads=40 : grads * 1.8 + 32
                #lambda params : function's body >>> retorna automaticamente el resultado

print(function_grads(10))