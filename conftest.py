import sys
import os

# Chemins Webots selon le système d'exploitation
if os.name == 'nt':  # Windows
    WEBOTS_HOME = "C:/Program Files/Webots"
    sys.path.insert(0, f"{WEBOTS_HOME}/lib/controller/python")
    os.environ["WEBOTS_HOME"] = WEBOTS_HOME
    os.add_dll_directory(f"{WEBOTS_HOME}/lib/controller")
    os.environ["PATH"] = f"{WEBOTS_HOME}/lib/controller;" + os.environ["PATH"]
else:  # Linux (GitHub Actions)
    WEBOTS_HOME = "/usr/local/webots"
    sys.path.insert(0, f"{WEBOTS_HOME}/lib/controller/python")
    os.environ["WEBOTS_HOME"] = WEBOTS_HOME