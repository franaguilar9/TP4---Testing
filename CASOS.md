R1) 

| Partición | Limites | Caso  | Esperado | Nivel |
| :---- | :---- | :---- | :---- | :---- |
| Producto minuscula | No tiene | buzo | Precio del catalogo (24.999,90) | unitario |
| producto mayúscula | No tiene | BUZO | PRODUCTO\_INEXISTENTE | unitario |
| producto una mayus | No tiene | Buzo | PRODUCTO\_INEXISTENTE | unitario |
| producto no esta en el catalogo | No tiene | jean | PRODUCTO\_INEXISTENTE | unitario |
| Precio no esta en el catalogo | No tiene | buzo con “precio”: 1 | 24999.90 | unitario |
| producto vacio | no tiene | “ ” / None | PRODUCTO\_INEXISTENTE | unitario |

R2)

| Partición | Limites | Caso  | Esperado | Nivel |
| :---- | :---- | :---- | :---- | :---- |
| Talles Validos | XS, XXL | XS, S, M, L, XL y XXL | Ningun error | unitario |
| Talle Invalido | No tiene | XXXXL | TALLE\_INVALIDO | unitario |
| Talle vacio | No tiene | None / “” | TALLE\_INVALIDO | unitario |
| Talle con espacios | No tiene | “   m” / “m   “ | Ningun error | unitario |
| Talles validos en minusculas | No tiene | xs, s, m, l, xl y xxl | Ningun error | unitario |
| talles validos con mayus y minus | No tiene | xXL | Ningun error | unitario |
| Talle solo espacios | No tiene | “  “ | TALLE\_INVALIDO | unitario |
| Tipo equivocado | No tiene | 40 | TALLE\_INVALIDO | unitario |

R3)

| Partición | Limites | Caso  | Esperado | Nivel |
| :---- | :---- | :---- | :---- | :---- |
| Cantidad valida: 1 \<= X \<= 10 (enteros)  | 1, 10 | 1 | Ningun error | Unitario |
| Cantidad invalida (limite) | No tiene | 0 | CANTIDAD\_INVALIDA | unitario |
| Cantidad invalida (decimal) | No tiene | 5.5 | CANTIDAD\_INVALIDA  | unitario  |
| Cantidad valida: 1 \<= X \<= 10 (enteros)  | 1, 10 | 10 | Ningun error | Unitario |
| Cantidad invalida (limite) | No tiene | 11 | CANTIDAD\_INVALIDA | unitario |
| Cantidad invalida (negativa) | No tiene | \-3 | CANTIDAD\_INVALIDA | unitario |

R4)

| Partición | Limites | Caso  | Esperado | Nivel |
| :---- | :---- | :---- | :---- | :---- |
| Carrito Valido. \>0 | 1 | calcular\_total(\[buzo M x1\], "CABA")  | Ningun error | Unitario |
| Carrito invalido \<= 0 | 0 | calcular\_total(\[\], "CABA")  | CARRITO\_VACIO | Unitario |
| No se modifica el carrito recibido  | no tiene | carrito \[{"producto":"buzo","talle":" m ","cantidad":1}\]; llamar a calcular\_total y comparar con una copia hecha antes | el carrito queda idéntico a la copia  | unitario |

R5) 

| Partición | Limites | Caso  | Esperado | Nivel |
| :---- | :---- | :---- | :---- | :---- |
| Un ítem con cantidad 5 o mas | 5 | \[buzo x5\]  | 12.499,95 DESCUENTO  | unitario |
| Dos items de 3 y 2 | No tiene | \[buzo x3, remera x2\]  | 9.899,87  DESCUENTO | unitario |
| Dos items de 2 y 2 | NO tiene | \[buzo x2, remera x2\]  | No aplica descuento | unitario |

R6)

| Partición | Limites | Caso  | Esperado | Nivel |
| :---- | :---- | :---- | :---- | :---- |
| EGRESADOS2026 (mayus o minuscula) | Fecha \= 30/11 | calcular\_descuento(subtotal, cantidad\_prendas, cupon=EGrESADOS2026, fecha=30/11/2026) | Descuento aplicado | Unitario |
| EGRESADOS2026 pasada la fecha |  | calcular\_descuento(subtotal, cantidad\_prendas, cupon=EGrESADOS2026, fecha=1/12/2026) | CUPON\_VENCIDO | Unnitario |
| BIENVENIDA valido | Subtotal \< 20000  | calcular\_descuento(subtotal \= 20000, cantidad\_prendas, cupon=Bienvenida, fecha=1/12/2026) | Beneficio 3000 pesos | Unitario |
| Bienvenida no valida | 19999 | calcular\_descuento(subtotal \= 19999, cantidad\_prendas, cupon=Bienvenida, fecha=1/12/2026) | CUPON\_MINIMO\_NO\_ALCANZADO | Unitario |
| Descuento por cantidad y descuento |  | calcular\_descuento(subtotal \= 249999, cantidad\_prendas \= 10 (buzos) , cupon=Bienvenida, fecha=1/12/2026) | Se elige el descuento mas grande. En este caso por cantidad de prendas | Unitario |
| Descuento \> Subtotal. Es imposible ya que un producto solo ya es mas grande que el 15% del mismo o 3000 pesos |  |  |  |  |
| No se recibe fecha |  | calcular\_descuento(subtotal \= 249999, cantidad\_prendas \= 10 (buzos) , cupon=Bienvenida, fecha=None) | fecha \= 18/10/2026 (supuesto hoy)  | Unitario |
| No hay cupón |  | calcular\_descuento(subtotal \= 24999, cantidad\_prendas \= 1 (buzos) , cupon=None / “” / “  “, fecha=1/10/2026) | Ningun error. No se usa cupón | Unitario |
| Con espacios |  | calcular\_descuento(subtotal \= 24999, cantidad\_prendas \= 1 (buzos) , cupon=”  egresados2026  ”, fecha=1/10/2026) | Descuento: 3.749,85 | Unitario |
| Cupon no existe |  | calcular\_descuento(subtotal \= 24999, cantidad\_prendas \= 1 (buzos) , cupon=”NO EXISTE“, fecha=1/10/2026) | CUPON\_INVALIDO  | Unitario |

R7)

| Partición | Limites | Caso  | Esperado | Nivel |
| :---- | :---- | :---- | :---- | :---- |
| Redondeo para arriba |  | 15 % de \$11.999,50 \= \$1.799,925  | 1799,93 | Unitario |
| Redondeo para abajo |  | 1500,49 | 1500.00 | Unitario |
| Todos los datos decimal |  | calcular\_total (subtotal, descuento, envío y total) | Ningun error | Unitario |

R8)

| Partición | Limites | Caso  | Esperado | Nivel |
| :---- | :---- | :---- | :---- | :---- |
| Envío pago: base \< 60.000  | 59.999,99 | calcular\_envio(59999.99, CABA) | 2500.00 | Unitario |
|  Envío gratis: base ≥ 60.000 | 60000 | calcular\_envio(60000, CABA) | 0.00 | Unitario |
|  Zona en minúscula  | \- | calcular\_envio(1000, “gba”) | 4000.00 | Unitario |
| Interior |  | calcular\_envio(1000, “interior”) | 6500 | Unitario |
| Zona que no existe |  | calcular\_envio(1000, “LA BOMBONERA”) | ZONA\_INVALIDA | Unitario |

R9)

| Partición | Caso | Esperado | Nivel |
| ----- | ----- | ----- | ----- |
| 1° carrito vacío gana a zona | \[\] \+ zona "MARTE" | CARRITO\_VACIO | unitario |
| 1° carrito vacío gana a cupón | \[\] \+ cupón "NOEXISTE" | CARRITO\_VACIO | unitario |
| 2° ítem gana a cupón | cantidad 0 \+ cupón "NOEXISTE" | CANTIDAD\_INVALIDA | unitario |
| Dentro del ítem: producto antes que talle | producto "jean" \+ talle "XXXL" | PRODUCTO\_INEXISTENTE | unitario |
| Dentro del ítem: talle antes que cantidad | talle "XXXL" \+ cantidad 0 | TALLE\_INVALIDO | unitario |
| Los ítems se revisan en el orden en que aparecen | ítem 1 con cantidad 0, ítem 2 con producto "jean" | CANTIDAD\_INVALIDA | unitario |
| 3° cupón gana a zona | cupón "NOEXISTE" \+ zona "MARTE" | CUPON\_INVALIDO | unitario |
| 3° cupón vencido gana a zona | EGRESADOS2026 con fecha 01/12/2026 \+ zona "MARTE" | CUPON\_VENCIDO | unitario |
| 4° solo zona inválida | todo válido \+ zona "MARTE" | ZONA\_INVALIDA | unitario |

R10)

| Partición | Limites | Caso | Esperado | Nivel |
| ----- | ----- | ----- | ----- | ----- |
| Ítem inválido en un carrito de 2  | 1.er ítem válido, 2.º inválido  | guardar\_pedido(con, "ana@mail.com", \[remera M x1, remera XXXL x1\], "CABA")  | lanza CheckoutError con TALLE\_INVALIDO; la tabla pedidos tiene 0 filas y items tiene 0 filas (contadas con otra conexión) | Integración |
| Cupón inexistente | — | guardar\_pedido(con, "ana@mail.com", \[remera M x1\], "CABA", "NOEXISTE") | CUPON\_INVALIDO; 0 pedidos y 0 ítems | integración |
| Zona inexistente | — | guardar\_pedido(con, "ana@mail.com", \[remera M x1\], "MARTE") | ZONA\_INVALIDA; 0 pedidos y 0 ítems | integración |
| Carrito vacío | 0 ítems | guardar\_pedido(con, "ana@mail.com", \[\], "CABA") | CARRITO\_VACIO; 0 pedidos y 0 ítems | integración |
| Pedido visible desde otra conexión (2) |  | guardar\_pedido(con, "ana@mail.com", \[remera M x1, remera XL x1\], "CABA"); después obtener\_pedido(otra, id) | trae el pedido con sus 2 ítems y el total | integración |
| Montos idénticos y Decimal (3) |  | guardar\_pedido(con, "ana@mail.com", \[remera M x1\], "CABA", "EGRESADOS2026", 2026-10-01); después obtener\_pedido(otra, id) | subtotal Decimal("11999.50"), descuento Decimal("1799.93"), envío Decimal("2500.00"), total Decimal("12699.57"); los cuatro son Decimal | integración |
| Precio del catálogo (4) |  | guardar\_pedido(con, "ana@mail.com", \[buzo M x1 con "precio": 1\], "CABA"); leer el pedido | precio\_unitario \== Decimal("24999.90") | integración |
| Datos normalizados (5) |  | guardar\_pedido(con, " aNa@MAIL.com ", \[remera " m " x1\], " caba ", " egresados2026 ", 2026-10-01); leer el pedido | email "ana@mail.com", zona "CABA", cupón "EGRESADOS2026", talle "M" | integración |

R11)

| Partición | Limites | Caso | Esperado | Nivel |
| ----- | ----- | ----- | ----- | ----- |
| Get del pedido |  | POST /api/v1/pedidos con remera M x1, CABA, EGRESADOS2026, fecha "2026-11-30"  Luego GET /api/v1/pedidos/1 | {     "id": 1,     "email": "ana@mail.com",     "zona": "CABA",     "cupon": "EGRESADOS2026",               "subtotal": "11999.50",     "descuento":”1799.93",     "envio": "2500.00",     "total":"12699.57",     "items": \[         {"producto": "remera", "talle": "M", "cantidad": 1,          "precio\_unitario": "11999.50"},     \], }  | E2E |
| Error Talle invalido |  | POST /api/v1/pedidos con remera XXXL x1, CABA, EGRESADOS2026, fecha "2026-11-30"   | {"error": {"code": "TALLE\_INVALIDO", "message": "Talle inválido: 'XXXL'"}}  | E2E |
| Error falta zona |  | POST /api/v1/pedidos con remera XL x1, None, EGRESADOS2026, fecha "2026-11-30"   | DATOS\_INCOMPLETOS  | E2E |
| Pedido inexistente |  | GET /api/v1/pedidos/999 | PEDIDO\_INEXISTENTE  | E2E |
| Ruta inexistente |  | GET /api/v1/pedidos/buenos/dias/gente | RUTA\_INEXISTENTE  | E2E |

