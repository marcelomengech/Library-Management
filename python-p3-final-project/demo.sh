#!/bin/bash

echo "=== Library Management System Demo ==="

# Add authors
echo -e "\n1. Adding Authors..."
python -m lib_cli.cli author add "Stephen King" -b "Horror author"
python -m lib_cli.cli author add "J.K. Rowling" -b "Fantasy author"

# List authors
echo -e "\n2. Listing Authors..."
python -m lib_cli.cli author list

# Add books
echo -e "\n3. Adding Books..."
python -m lib_cli.cli book add "The Shining" 1 --isbn "978-0307743657" --year 1977
python -m lib_cli.cli book add "Harry Potter" 2 --isbn "9780747532743" --year 1997