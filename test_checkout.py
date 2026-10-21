from datetime import date
from decimal import Decimal

import pytest

from checkout import (
    CheckoutError,
    calcular_descuento,
    calcular_envio,
    calcular_subtotal,
    calcular_total,
    validar_item,
)

HOY_VIGENTE = date(2026, 10, 1)


def item(producto="buzo", talle="M", cantidad=1, **extra):
    return {"producto": producto, "talle": talle, "cantidad": cantidad, **extra}


def codigo_de_error(funcion, *args):
    with pytest.raises(CheckoutError) as error:
        funcion(*args)
    return error.value.code


def test_cantidad_cero_es_invalida():
    assert codigo_de_error(validar_item, item(cantidad=0)) == "CANTIDAD_INVALIDA"


def test_gana_el_mayor_descuento_cupon():
    descuento = calcular_descuento(100000, 6, "EGRESADOS2026", date(2026, 10, 1))
    assert descuento == 15000.0


def test_con_5_prendas_se_aplica_el_10_por_ciento():
    descuento = calcular_descuento(10000, 5)
    assert descuento == 1000

def test_el_cupon_debug100_no_existe():
    with pytest.raises(CheckoutError) as error:
        calcular_descuento(10000, 2, "DEBUG100")
    assert error.value.code == "CUPON_INVALIDO"

def test_cupon_minuscula_valido():
    descuento = calcular_descuento(10000, 4, "egresados2026", date(2026, 10, 1))
    assert descuento == 1500


def test_calcular_envio_marte_falla_y_lanza_zona_invalida():
    with pytest.raises(CheckoutError) as error:
        calcular_envio(60000, "MARTE")
    assert error.value.code == "ZONA_INVALIDA"


def test_cantidad_once_debe_ser_invalida():
    with pytest.raises(CheckoutError) as error:
        validar_item({"producto": "buzo", "talle": "M", "cantidad": 11})
    assert error.value.code == "CANTIDAD_INVALIDA"

def test_un_carrito_vacio_lanza_carrito_vacio():
    with pytest.raises(CheckoutError) as error:
        calcular_total([], "CABA")
    assert error.value.code == "CARRITO_VACIO"


def test_envio_sobre_subtotal_con_descuento():
    resultado = calcular_total([
        {"producto": "buzo", "talle": "M", "cantidad": 2},
        {"producto": "remera", "talle": "M", "cantidad": 1},
    ],"CABA", "BIENVENIDA", date(2026, 10, 1))
    assert resultado["envio"] == 2500
    assert resultado["total"] == 61499.3

def test_gana_el_mayor_descuento_cantidadprendas():
    descuento = calcular_descuento(100000, 5, "BIENVENIDA")
    assert descuento == 10000.0

def test_cantidad_once_debe_ser_invalida():
    with pytest.raises(CheckoutError) as error:
        validar_item({"producto": "buzo", "talle": "M", "cantidad": 11})
    assert error.value.code == "CANTIDAD_INVALIDA"

def test_funciona_dia_en_que_vence():
    descuento = calcular_descuento(100000, 5, "EGRESADOS2026", date(2026, 11, 30))
    assert descuento == 15000.0

def test_cupon_valido_precio_minimo():
    descuento = calcular_descuento(20000, 1, "BIENVENIDA", date(2026, 11, 30))
    assert descuento == 3000.0

def test_envio_gratis_a_partir_de_60000():
    assert calcular_envio(60000, "CABA") == 0

def test_descuento_bien_aplicado_en_el_resultado():
    resultado = calcular_total([
        {"producto": "buzo", "talle": "M", "cantidad": 4},
        {"producto": "remera", "talle": "M", "cantidad": 1},
    ],"CABA", "BIENVENIDA", date(2026, 10, 1))
    assert resultado["descuento"] == 11199.91

def test_talle_que_no_existe():
    with pytest.raises(CheckoutError) as error:
        validar_item({"producto": "buzo", "talle": "XXXL", "cantidad": 8})
    assert error.value.code == "TALLE_INVALIDO"


def test_cupon_minimo_no_alcanzado():
    with pytest.raises(CheckoutError) as error:
        calcular_descuento(10000, 2, "BIENVENIDA", date(2026, 11, 30))
    assert error.value.code == "CUPON_MINIMO_NO_ALCANZADO"


def test_cupon_vencido():
    with pytest.raises(CheckoutError) as error:
        calcular_descuento(10000, 2, "EGRESADOS2026", date(2026, 12, 30))
    assert error.value.code == "CUPON_VENCIDO"

def test_producto_no_existe():
    with pytest.raises(CheckoutError) as error:
        calcular_subtotal([
        {"producto": "pantalon", "talle": "M", "cantidad": 4}])
    assert error.value.code == "PRODUCTO_INEXISTENTE"

def test_el_precio_sale_del_catalogo_aunque_el_cliente_mande_otro():
    subtotal = calcular_subtotal([
        {"producto": "buzo", "talle": "M", "cantidad": 1, "precio": 1}])
    assert subtotal == 24999.9

def test_cantidad_10_es_valida():
    assert validar_item({"producto": "buzo", "talle": "M", "cantidad": 10}) is None



def test_total_respeta_la_fecha_recibida_y_rechaza_cupon_vencido():
    carrito = [item()]
    fecha = date(2026, 12, 1)
    assert codigo_de_error(calcular_total, carrito, "CABA", "EGRESADOS2026", fecha) == "CUPON_VENCIDO"


def test_total_aplica_cupon_en_el_ultimo_dia_de_vigencia():
    carrito = [item()]

    resultado = calcular_total(carrito, "CABA", "EGRESADOS2026", date(2026, 11, 30))
    assert Decimal(str(resultado["descuento"])) == Decimal("3749.99")
