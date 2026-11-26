# Bug reports for exercise4.py

Line: 4
Problem: The administrator password is hard-coded in the source, exposing a secret and ignoring secure configuration.
Example: inspecting the module source reveals `admin123`, even when no password has been configured externally.
Fix: `ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")`

Line: 14
Problem: `find_user` interpolates the username directly into SQL, allowing SQL injection.
Example: `find_user(db, "x' OR '1'='1")` returns the first user instead of None.
Fix: `return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()`
