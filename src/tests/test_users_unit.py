# src/tests/test_user_unit.py

import json
from datetime import datetime
import pytest
import src.api.users

def test_add_user(test_app, monkeypatch):
 	pass


def test_add_user_invalid_json(test_app, monkeypatch):
    pass


def test_add_user_invalid_json_keys(test_app, monkeypatch):
    pass


def test_add_user_duplicate_email(test_app, monkeypatch):
    pass


def test_single_user(test_app, monkeypatch):
    pass


def test_single_user_incorrect_id(test_app, monkeypatch):
    pass


def test_all_users(test_app, monkeypatch):
    pass


def test_remove_user(test_app, monkeypatch):
    pass


def test_remove_user_incorrect_id(test_app, monkeypatch):
    pass


def test_update_user(test_app, monkeypatch):
    pass


@pytest.mark.parametrize(
    "user_id, payload, status_code, message",
    [
        [1, {}, 400, "Input payload validation failed"],
        [1, {"email": "me@testdriven.io"}, 400, "Input payload validation failed"],
        [
            999,
            {"username": "me", "email": "me@testdriven.io"},
            404,
            "User 999 does not exist",
        ],
    ],
)


def test_update_user_invalid(test_app, monkeypatch):
    pass


def test_update_user_duplicate_email(test_app, monkeypatch):
    pass