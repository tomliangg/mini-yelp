# wsgi = web server gateway inferface

from app import app  # Import your Flask app instance

if __name__ == "__main__":
    app.run()  # For development/testing (use WSGI server in production)