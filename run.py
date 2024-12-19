"""
This script runs the Flask application defined in the src.main module.
"""

from src.main import app

if __name__ == "__main__":
    app.run(debug=True, port=5002)
