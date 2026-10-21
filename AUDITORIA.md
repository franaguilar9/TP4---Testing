1 · test\_subtotal

Clasificación: tautológico.  
Qué verifica realmente: que calcular\_subtotal devuelva CATALOGO\["buzo"\] \* 2, que es lo mismo que hace el código por dentro (toma el precio del catálogo y multiplica). No compara contra ningún número que salga de la especificación.  
Qué error dejaría pasar: error en los datos del catálogo. Si el catálogo tuviera un precio equivocado, el código y el test darían el mismo resultado equivocado. Además, el catálogo usa float (24999.90) y no Decimal, y el test pasa igual porque compara float con float.

2 · test\_total\_funciona

Clasificación: débil.  
Qué verifica realmente: solo que calcular\_total devuelva algo (assert resultado is not None). No importa si el valor está bien.  
Qué error dejaría pasar: casi cualquiera: negativo, un envío mal calculado, un descuento incorrecto. Mientras no devuelva None, el test pasa

3 · test\_total\_positivo

Clasificación: débil.  
Qué verifica realmente: que resultado\["total"\] \> 0\. No se fija si el número es el correcto.  
Qué error dejaría pasar: un total de \$1 pasaría como correcto, igual que cualquier total positivo equivocado.

4 · test\_cupon\_egresados

Clasificación: tautológico  
Qué verifica realmente: que calcular\_descuento(100000, 1, "EGRESADOS2026", fecha) sea igual a 100000 \* 0.15. El esperado es una cuenta, la misma que hace el código por dentro, no un número escrito.  
Qué error dejaría pasar:  
Un error de cálculo, porque el esperado se calcula igual que el código.  
No esta cerca del limite de expirar: usa 2026-10-01, lejos del borde del 30/11.

5 · test\_envio\_caba

Clasificación: útil pero insuficiente.  
Qué verifica realmente: que calcular\_envio(10000, "CABA") dé 2500\. El valor está escrito a mano, así que no es tautológico.  
Qué error dejaría pasar: casi todo lo demás de R8:  
\- el límite de \$60.000 (\> en vez de \>=), porque prueba con 10.000, lejos del borde;  
\- que el envío se calcule sobre el subtotal con descuento;  
\- la zona inválida (ZONA\_INVALIDA).

6 · test\_descuento\_por\_cantidad

Clasificación: débil (no es "útil" porque no prueba el límite).  
Qué verifica realmente: que con 6 prendas el descuento sea 10000 (10 % de 100.000). El esperado está escrito a mano, eso está bien.  
Qué error dejaría pasar: usa 6, no el límite. Si el código tuviera \> 5 en vez de \>= 5, con 5 prendas no habría descuento y este test seguiría en verde. Tampoco prueba que, entre cupón y cantidad, se aplique el mayor sin sumarlos.

7 · test\_talle\_valido

Clasificación: inútil.  
Qué verifica realmente: que validar\_item no lance ninguna excepción con talle "M". No tiene assert, así que solo puede fallar si el código se rompe con una excepción.  
Qué error dejaría pasar: que validar\_item modifique el ítem, que no haga strip() de los espacios, o que no valide el producto.

8 · test\_no\_explota\_con\_varios\_productos

Clasificación: inútil.  
Qué verifica realmente: nada. Llama a calcular\_total dentro de un try/except Exception: pass, que atrapa cualquier error y lo ignora. No tiene assert.  
Qué error dejaría pasar: absolutamente todos, incluso que calcular\_total lance una excepción. Este test no puede fallar nunca.

PUNTAJE  
python mutar.py \--tests test\_checkout\_ia.py   
Mutando checkout.py contra test\_checkout\_ia.py  (motor: pytest)

Mutantes generados : 29  
Muertos            : 17  
Sobrevivientes     : 12  
Puntaje de mutación: 58.6%

Sobrevivientes — había un error acá y ningún test lo detectó:

  línea  40  '\<' → '\<='              if not (1 \<= item\["cantidad"\] \< 10):  
  línea  40  10 → 11                 if not (1 \<= item\["cantidad"\] \< 10):  
  línea  60  '\>' → '\>='              if cantidad\_prendas \> 5:  
  línea  72  '\<' → '\<='              if not fecha \< datos\["vence"\]:  
  línea  76  '==' → '\!='             elif datos\["tipo"\] \== "fijo":  
  línea  77  '\<' → '\<='              if subtotal \< datos\["minimo"\]:  
  línea  82  '+' → '-'               descuento \+= datos\["valor"\]  
  línea  96  '\>=' → '\>'              if subtotal \>= 60000:  
  línea  96  60000 → 60001           if subtotal \>= 60000:  
  línea 107  '+' → '-'               prendas \= prendas \+ item\["cantidad"\]  
  línea 111  '+' → '-'               total \= subtotal \- descuento \+ envio  
  línea 111  '-' → '+'               total \= subtotal \- descuento \+ envio

Que cubra el 80% no importa, porque los tests están mal hechos, entonces en realidad no cubre nada.