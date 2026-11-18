from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_qr_returns_png() -> None:
    response = client.get("/qr", params={"text": "https://example.com"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    assert response.content.startswith(b"\x89PNG\r\n\x1a\n")


def test_qr_rejects_empty_text() -> None:
    response = client.get("/qr", params={"text": ""})
    assert response.status_code == 422


def test_qr_requires_text() -> None:
    assert client.get("/qr").status_code == 422


def test_qr_rejects_oversized_text() -> None:
    response = client.get("/qr", params={"text": "a" * 1001})
    assert response.status_code == 422


def test_qr_rejects_invalid_box_size() -> None:
    response = client.get("/qr", params={"text": "hello", "box_size": 0})
    assert response.status_code == 422
