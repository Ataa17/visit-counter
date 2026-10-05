from unittest.mock import Mock

import app as app_module


def test_home_returns_status_200(monkeypatch):
    fake_db = Mock()
    fake_db.incr.return_value = 1
    monkeypatch.setattr(app_module, "db", fake_db)

    response = app_module.app.test_client().get("/")

    assert response.status_code == 200


def test_home_contains_bonjour(monkeypatch):
    fake_db = Mock()
    fake_db.incr.return_value = 1
    monkeypatch.setattr(app_module, "db", fake_db)

    response = app_module.app.test_client().get("/")

    assert b"Bonjour" in response.data


def test_home_displays_counter(monkeypatch):
    fake_db = Mock()
    fake_db.incr.return_value = 7
    monkeypatch.setattr(app_module, "db", fake_db)

    response = app_module.app.test_client().get("/")

    assert b"vue 7 fois" in response.data
