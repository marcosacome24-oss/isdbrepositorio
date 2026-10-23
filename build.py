import os
import subprocess
import sys


def main():
    if os.environ.get("DATABASE_URL") or os.environ.get("POSTGRES_URL"):
        subprocess.run([sys.executable, "manage.py", "migrate", "--noinput"], check=True)
    else:
        print("DATABASE_URL not set; skipping migrations (SQLite in /tmp is migrated at runtime).")


if __name__ == "__main__":
    main()
