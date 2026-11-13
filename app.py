import sqlite3


def get_user(conn: sqlite3.Connection, username: str):
    """Return one user row by name.

    The query is parameterised: the caller cannot change its structure.
    """
    cur = conn.execute("SELECT id, username FROM users WHERE username = ?", (username,))
    return cur.fetchone()


def render_health() -> str:
    return "ok"
