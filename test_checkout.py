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