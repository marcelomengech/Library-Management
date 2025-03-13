import os
import sqlite3
import shutil

# Remove existing database
if os.path.exists('library.db'):
    os.remove('library.db')
    print("Removed existing database")

# Create a fresh database
conn = sqlite3.connect('library.db')
conn.close()
print("Created fresh database")

# Clear existing migration versions
versions_dir = 'migrations/versions'
if os.path.exists(versions_dir):
    for file in os.listdir(versions_dir):
        if file.endswith('.py'):
            os.remove(os.path.join(versions_dir, file))
    print("Cleared existing migration versions")

# Initialize database schema
from lib_cli.db import init_db
init_db()
print("Initialized database schema")

print("Alembic environment reset successfully")