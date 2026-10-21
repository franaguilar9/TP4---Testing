HALLAZGOS

Comando: ruff check checkout.py (5 errores). El resto salió de la lectura de checkout.py, pedidos.py y api.py, de la prueba de mutación y de pruebas manuales.

H-01 · Cupón oculto DEBUG100 con 100 % de descuento  
Archivo y línea: checkout.py:23  
Categoría: seguridad  
Regla que no cumple: R6 ("Estos son los únicos dos cupones que existen")  
Cómo la encontré: lectura del código  
Severidad: alta

H-02 · except sin tipo esconde los productos inexistentes  
Archivo y línea: checkout.py:48 a 51  
Categoría: manejo de errores  
Regla que no cumple: R1 ("Un producto que no está en el catálogo → PRODUCTO\_INEXISTENTE")  
Cómo la encontré: ruff (E722) y lectura del código  
Severidad: alta

H-03 · date.today() como valor por defecto se evalúa una sola vez  
Archivo y línea: checkout.py:57 (calcular\_descuento) y checkout.py:102 (calcular\_total)  
Categoría: fechas  
Regla que no cumple: R6 ("Si no se recibe fecha, se usa la fecha del día en que se hace la llamada")  
Cómo la encontré: ruff (B008)  
Severidad: media

H-04 · La cantidad 10 se rechaza (\< 10 en vez de \<= 10\)  
Archivo y línea: checkout.py:40  
Categoría: lógica y límites  
Regla que no cumple: R3 ("entre 1 y 10, ambos inclusive")  
Cómo la encontré: mutación (sobrevivientes de la línea 40\) y lectura del código  
Severidad: media

H-05 · El descuento por cantidad empieza en 6, no en 5 (\> 5 en vez de \>= 5\)  
Archivo y línea: checkout.py:60  
Categoría: lógica y límites  
Regla que no cumple: R5 ("5 o más")  
Cómo la encontré: mutación (sobreviviente de la línea 60\) y lectura de la especificación  
Severidad: media

H-06 · import json sin usar  
Archivo y línea: checkout.py:1  
Categoría: code smell  
Regla que no cumple: ninguna  
Cómo la encontré: ruff (F401)  
Severidad: baja

H-07 · Comparación \!= None  
Archivo y línea: checkout.py:63  
Categoría: code smell  
Regla que no cumple: ninguna  
Cómo la encontré: ruff (E711)  
Severidad: baja

H-08 · validar\_item modifica el ítem que recibe  
Archivo y línea: checkout.py:35 (item\["talle"\] \= item\["talle"\].upper())  
Categoría: efectos laterales  
Regla que no cumple: R4 ("Ninguna función modifica el carrito que recibe")  
Cómo la encontré: lectura del código (una asignación sobre el argumento)  
Severidad: media

H-09 · Dinero en float y redondeo incorrecto del medio centavo  
Archivo y línea: checkout.py:12 a 16 (CATALOGO), checkout.py:20 a 24 (CUPONES) y los round(..., 2\) de checkout.py:54, 84 y 117  
Categoría: numéricos  
Regla que no cumple: R7 (importes en Decimal, medio centavo hacia arriba)  
Cómo la encontré: lectura del código y prueba del ejemplo de R7  
Severidad: alta

H-10 · Un talle que no es texto rompe el programa con AttributeError  
Archivo y línea: checkout.py:35 (item\["talle"\].upper())  
Categoría: tipos  
Regla que no cumple: R2 (cualquier otro valor → TALLE\_INVALIDO) y la regla general "ante cualquier dato inválido, CheckoutError, nunca otro tipo de excepción"  
Cómo la encontré: lectura del código y prueba en la terminal  
Severidad: media

H-11 · Se acepta una cantidad no entera (5.5)  
Archivo y línea: checkout.py:40  
Categoría: tipos  
Regla que no cumple: R3 ("incluidos los no enteros → CANTIDAD\_INVALIDA")  
Cómo la encontré: prueba en la terminal con la cantidad 5.5  
Severidad: media

H-12 · El cupón distingue mayúsculas y minúsculas  
Archivo y línea: checkout.py:64 (codigo \= cupon.strip())  
Categoría: strings  
Regla que no cumple: R6 ("No se distingue mayúscula de minúscula y se ignoran los espacios alrededor")  
Cómo la encontré: lectura del código y prueba en la terminal  
Severidad: media

H-13 · Un cupón vacío se trata como cupón inválido  
Archivo y línea: checkout.py:63 (if cupon \!= None:)  
Categoría: strings  
Regla que no cumple: R6 (None, "" o solo espacios equivalen a no usar cupón, no es un error)  
Cómo la encontré: lectura del código y prueba en la terminal  
Severidad: alta

H-14 · El cupón y el descuento por cantidad se suman en vez de aplicar el mayor  
Archivo y línea: checkout.py:61, 74 y 82 (descuento \+= ...)  
Categoría: lógica y límites  
Regla que no cumple: R6 ("El cupón no se acumula con el descuento por cantidad. Se calculan los dos y se aplica el mayor")  
Cómo la encontré: lectura del código y prueba en la terminal  
Severidad: alta

H-15 · calcular\_total acepta un carrito vacío  
Archivo y línea: checkout.py:102 (calcular\_total)  
Categoría: lógica y límites  
Regla que no cumple: R4 ("Debe tener al menos un ítem → si no, CARRITO\_VACIO") y el orden de validación de la sección 3  
Cómo la encontré: lectura del código y prueba en la terminal  
Severidad: alta

H-16 · El envío se calcula sobre el subtotal sin descuento  
Archivo y línea: checkout.py:110 (envio \= calcular\_envio(subtotal, zona))  
Categoría: lógica y límites  
Regla que no cumple: R8 ("El envío es gratis si el subtotal ya con el descuento aplicado es de \$60.000 o más")  
Cómo la encontré: lectura del código (qué recibe calcular\_envio)  
Severidad: media

H-17 · Método inexistente (.keys().join) rompe el aviso de zona inválida  
Archivo y línea: checkout.py:93 (ENVIOS.keys().join(', '))  
Categoría: alucinación  
Regla que no cumple: R8 ("Zona que no existe → ZONA\_INVALIDA") y la regla general de que ante datos inválidos solo se lanza CheckoutError  
Cómo la encontré: lectura del código y prueba en la terminal  
Severidad: alta

H-18 · El cupón EGRESADOS2026 vence un día antes (\< en vez de \<=)  
Archivo y línea: checkout.py:72 (if not fecha \< datos\["vence"\]:)  
Categoría: fechas  
Regla que no cumple: R6 ("Válido hasta el 30/11/2026 inclusive")  
Cómo la encontré: lectura del código  
Severidad: media

H-19 · El pedido se confirma antes de calcular los importes (queda un pedido huérfano)  
Archivo y línea: pedidos.py:39 a 50 (INSERT y commit antes de calcular\_total)  
Categoría: efectos laterales  
Regla que no cumple: R10 ("Si eso lanza CheckoutError, el error se propaga y no queda nada guardado: ni el pedido ni sus ítems")  
Cómo la encontré: lectura del código (el commit está antes del cálculo) y prueba con una segunda conexión  
Severidad: alta

H-20 · Los importes se guardan como REAL y se leen con ruido de float  
Archivo y línea: pedidos.py:12 a 15 y 23 (columnas REAL), pedidos.py:55 a 58 y 68 (float(...)), pedidos.py:88 a 91 y 97 (Decimal(...) al leer)  
Categoría: numéricos  
Regla que no cumple: R10 ("Los montos que devuelve obtener\_pedido son idénticos a los que calculó checkout: Decimal, mismo valor, sin ninguna pérdida") y R7  
Cómo la encontré: lectura del código y prueba guardando y leyendo un pedido  
Severidad: alta

H-21 · Inyección SQL en pedidos\_de  
Archivo y línea: pedidos.py:107  
Categoría: seguridad  
Regla que no cumple: R10 ("ningún valor puede alterar la consulta a la base")  
Cómo la encontré: lectura del código (la única consulta armada con f-string) y prueba con un email trucho  
Severidad: alta

H-22 · El precio unitario guardado puede ser el que manda el cliente  
Archivo y línea: pedidos.py:64 (item.get("precio", CATALOGO\[item\["producto"\]\]))  
Categoría: seguridad  
Regla que no cumple: R10 ("precio\_unitario es el precio del catálogo, nunca uno enviado por el cliente") y R1  
Cómo la encontré: lectura del código y prueba guardando un ítem con "precio": 1  
Severidad: alta

H-23 · Falta el commit final: el pedido no es definitivo  
Archivo y línea: pedidos.py:71 (final de guardar\_pedido, antes del return)  
Categoría: efectos laterales  
Regla que no cumple: R10 ("Cuando guardar\_pedido termina, el pedido es definitivo: cualquier otra conexión lo ve completo, con todos sus ítems")  
Cómo la encontré: lectura del código (no hay commit al final) y prueba con una segunda conexión  
Severidad: alta

H-24 · fecha=None explícito rompe con TypeError  
Archivo y línea: checkout.py:72 (calcular\_descuento); guardar\_pedido le pasa fecha=None por defecto (pedidos.py:38 y 50\)  
Categoría: fechas  
Regla que no cumple: R6 ("Si no se recibe fecha, se usa la fecha del día en que se hace la llamada")  
Cómo la encontré: prueba en la terminal con fecha=None  
Severidad: alta

H-25 · except Exception convierte todos los errores en un 500  
Archivo y línea: api.py:53 y 54 (do\_POST) y api.py:67 y 68 (do\_GET)  
Categoría: manejo de errores  
Regla que no cumple: R11 ("Un error nunca puede devolver 500"; los errores de negocio dan 422, el JSON roto 400, datos incompletos 400, fecha inválida 400\) y el formato único de error  
Cómo la encontré: lectura del código y requests reales contra el servidor  
Severidad: alta

H-26 · Los montos viajan como números JSON en vez de texto  
Archivo y línea: api.py:18 (json.dumps(cuerpo, default=float))  
Categoría: numéricos  
Regla que no cumple: R11 ("Los montos viajan siempre como texto, nunca como número JSON")  
Cómo la encontré: requests reales contra el servidor  
Severidad: alta

H-27 · GET de un pedido inexistente responde 200 con null  
Archivo y línea: api.py:64 a 66 (do\_GET)  
Categoría: manejo de errores  
Regla que no cumple: R11 (pedido que no existe → 404 PEDIDO\_INEXISTENTE)  
Cómo la encontré: requests reales contra el servidor  
Severidad: media

H-28 · La fecha llega como texto y no se convierte (todo POST con fecha da 500\)  
Archivo y línea: api.py:41 (datos.get("fecha") se pasa tal cual a guardar\_pedido)  
Categoría: tipos  
Regla que no cumple: R11 (la fecha viaja como texto AAAA-MM-DD; si no tiene ese formato → 400 FECHA\_INVALIDA)  
Cómo la encontré: requests reales contra el servidor  
Severidad: alta

TABLA DE HALLAZGOS (de la más grave a la menos grave)

| \# | Archivo:línea | Categoría | Regla | Cómo la encontré | Severidad |
| :---- | :---- | :---- | :---- | :---- | :---- |
| H-21 | pedidos.py:107 | seguridad | R10 | lectura \+ prueba | alta |
| H-01 | checkout.py:23 | seguridad | R6 | lectura | alta |
| H-22 | pedidos.py:64 | seguridad | R10, R1 | lectura \+ prueba | alta |
| H-14 | checkout.py:61, 74, 82 | lógica y límites | R6 | lectura \+ prueba | alta |
| H-09 | checkout.py:12-24, 54, 84, 117 | numéricos | R7 | lectura \+ prueba | alta |
| H-20 | pedidos.py:12-15, 23, 55-58, 68, 88-91, 97 | numéricos | R10, R7 | lectura \+ prueba | alta |
| H-02 | checkout.py:48-51 | manejo de errores | R1 | ruff E722 \+ lectura | alta |
| H-19 | pedidos.py:39-50 | efectos laterales | R10 | lectura \+ prueba | alta |
| H-23 | pedidos.py:71 | efectos laterales | R10 | lectura \+ prueba | alta |
| H-28 | api.py:41 | tipos | R11 | requests reales | alta |
| H-25 | api.py:53-54, 67-68 | manejo de errores | R11 | lectura \+ requests | alta |
| H-26 | api.py:18 | numéricos | R11 | requests reales | alta |
| H-24 | checkout.py:72 | fechas | R6 | prueba en terminal | alta |
| H-15 | checkout.py:102 | lógica y límites | R4 | lectura \+ prueba | alta |
| H-17 | checkout.py:93 | alucinación | R8 | lectura \+ prueba | alta |
| H-13 | checkout.py:63 | strings | R6 | lectura \+ prueba | alta |
| H-03 | checkout.py:57, 102 | fechas | R6 | ruff B008 | media |
| H-04 | checkout.py:40 | lógica y límites | R3 | mutación \+ lectura | media |
| H-05 | checkout.py:60 | lógica y límites | R5 | mutación \+ lectura | media |
| H-08 | checkout.py:35 | efectos laterales | R4 | lectura | media |
| H-10 | checkout.py:35 | tipos | R2 | lectura \+ prueba | media |
| H-11 | checkout.py:40 | tipos | R3 | prueba en terminal | media |
| H-12 | checkout.py:64 | strings | R6 | lectura \+ prueba | media |
| H-16 | checkout.py:110 | lógica y límites | R8 | lectura | media |
| H-18 | checkout.py:72 | fechas | R6 | lectura \+ CASOS.md | media |
| H-27 | api.py:64-66 | manejo de errores | R11 | requests reales | media |
| H-06 | checkout.py:1 | code smell | ninguna | ruff F401 | baja |
| H-07 | checkout.py:63 | code smell | ninguna | ruff E711 | baja |

