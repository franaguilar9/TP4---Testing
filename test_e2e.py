import json
import threading
import urllib.error
import urllib.request

import pytest

import api

RUTA = "/api/v1/pedidos"


@pytest.fixture
def url(tmp_path):
    servidor = api.crear_servidor(str(tmp_path / "tienda.db"), 0)
    threading.Thread(target=servidor.serve_forever, kwargs={"poll_interval": 0.05}, daemon=True).start()
    yield f"http://127.0.0.1:{servidor.server_address[1]}"
    servidor.shutdown()
    servidor.server_close()


def pedir(url, metodo, ruta, cuerpo=None, crudo=None):
    datos = crudo if crudo is not None else (json.dumps(cuerpo).encode() if cuerpo is not None else None)
    req = urllib.request.Request(url + ruta, data=datos, method=metodo,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            return r.status, json.loads(r.read() or b"null")
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"null")


def compra(**cambios):
    cuerpo = {"email": "ana@mail.com", "zona": "CABA",
              "carrito": [{"producto": "buzo", "talle": "M", "cantidad": 1}]}
    cuerpo.update(cambios)
    return cuerpo


def test_una_ruta_inexistente_devuelve_404(url):
    status, cuerpo = pedir(url, "GET", "/api/v1/otra")
    assert status == 404
    assert cuerpo["error"]["code"] == "RUTA_INEXISTENTE"






def test_un_error_de_negocio_devuelve_422_con_el_codigo_del_checkout(url):
    cuerpo = compra(carrito=[{"producto": "buzo", "talle": "XXXL", "cantidad": 1}])

    status, respuesta = pedir(url, "POST", RUTA, cuerpo)

    assert status == 422
    assert respuesta["error"]["code"] == "TALLE_INVALIDO"


def test_un_cuerpo_que_no_es_json_devuelve_400_json_invalido(url):
    status, respuesta = pedir(url, "POST", RUTA, crudo=b"{esto no es json")

    assert status == 400
    assert respuesta["error"]["code"] == "JSON_INVALIDO"




def test_pedir_un_pedido_que_no_existe_devuelve_404_pedido_inexistente(url):
    status, respuesta = pedir(url, "GET", f"{RUTA}/999")

    assert status == 404
    assert respuesta["error"]["code"] == "PEDIDO_INEXISTENTE"
