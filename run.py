"""
Module entry point for the app
"""

from api.route import app

if __name__ == '__main__':
    app.run(debug=False)
