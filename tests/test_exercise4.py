import inspect
import sqlite3

import exercise4


def test_admin_password_is_not_hard_coded():
    assert "admin123" not in inspect.getsource(exercise4)


def test_find_user_uses_parameterized_sql():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT, email TEXT)")
    db.execute("INSERT INTO users VALUES ('ana', 'ana@mail.com')")
    assert exercise4.find_user(db, "x' OR '1'='1") is None
    assert exercise4.find_user(db, "ana") is not None
