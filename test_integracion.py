from datetime import date
from decimal import Decimal

import pytest

import pedidos
from checkout import CheckoutError

HOY_VIGENTE = date(2026, 10, 1)


@pytest.fixture
def ruta(tmp_path):
    return str(tmp_path / "tienda.db")


@pytest.fixture
def con(ruta):
    conexion = pedidos.conectar(ruta)
    pedidos.crear_esquema(conexion)
    yield conexion
    conexion.close()


def item(producto="buzo", talle="M", cantidad=1, **extra):
    return {"producto": producto, "talle": talle, "cantidad": cantidad, **extra}


def contar(ruta, tabla):
    assert tabla in ("pedidos", "items")
    otra = pedidos.conectar(ruta)
    try:
        return otra.execute(f"SELECT COUNT(*) FROM {tabla}").fetchone()[0]
    finally:
        otra.close()


def test_un_id_inexistente_devuelve_none(con):
    assert pedidos.obtener_pedido(con, 999) is None


def test_un_error_de_checkout_no_deja_ni_pedido_ni_items_guardados(con, ruta):
    carrito = [item(talle="XXXL")]

    with pytest.raises(CheckoutError):
        pedidos.guardar_pedido(con, "ana@mail.com", carrito, "CABA")

    assert contar(ruta, "pedidos") == 0
    assert contar(ruta, "items") == 0


def test_los_montos_guardados_son_decimal_e_identicos_a_los_calculados(con):
    carrito = [item(producto="remera")]

    pedido_id = pedidos.guardar_pedido(con, "ana@mail.com", carrito, "CABA", "EGRESADOS2026", HOY_VIGENTE)
    pedido = pedidos.obtener_pedido(con, pedido_id)

    assert type(pedido["subtotal"]) is Decimal
    assert type(pedido["descuento"]) is Decimal
    assert type(pedido["envio"]) is Decimal
    assert type(pedido["total"]) is Decimal
    assert pedido["subtotal"] == Decimal("11999.50")
    assert pedido["descuento"] == Decimal("1799.93")
    assert pedido["envio"] == Decimal("2500.00")
    assert pedido["total"] == Decimal("12699.57")


def test_el_precio_unitario_es_el_del_catalogo_aunque_el_cliente_envie_otro(con):
    carrito = [item(producto="buzo", precio=1)]

    pedido_id = pedidos.guardar_pedido(con, "ana@mail.com", carrito, "CABA")
    pedido = pedidos.obtener_pedido(con, pedido_id)

    assert float(pedido["items"][0]["precio_unitario"]) == 24999.9
