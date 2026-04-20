import sys
import os
import importlib.util

# Set up path for nested Flask app
base_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(base_dir, 'updated_inte_pro', 'updated_inte_pro', 'inte', 'inte')
nested_app_file = os.path.join(app_dir, 'app.py')

# Change to app directory so relative imports work
os.chdir(app_dir)
sys.path.insert(0, app_dir)

# Load Flask app module directly to avoid circular import
spec = importlib.util.spec_from_file_location("flask_app_module", nested_app_file)
flask_app_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(flask_app_module)

# Get the Flask app
app = flask_app_module.app

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

import sys
import os

# Add the nested app directory to Python path
app_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'updated_inte_pro', 'updated_inte_pro', 'inte', 'inte')
sys.path.insert(0, app_dir)
os.chdir(app_dir)

# Import the Flask app from nested directory
from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
