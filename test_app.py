from app import app, APP_VERSION


def test_home_responde_200():
    client = app.test_client()
    resposta = client.get("/")
    assert resposta.status_code == 200
    assert b"TechSecure" in resposta.data


def test_health_retorna_ok_e_versao():
    client = app.test_client()
    resposta = client.get("/health")
    assert resposta.status_code == 200
    assert resposta.get_json() == {"status": "ok", "version": APP_VERSION}
