#!/bin/sh

# Run the database preparation script
python db_prep.py

# Check if db_prep.py completed
echo "Finished db_prep.py. Now starting local_app.py..."

# After db_prep.py finishes, start the Flask application
python local_app.py

# Log that local_app.py has started
echo "Started local_app.py."