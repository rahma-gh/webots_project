import sys
import os

sys.path.insert(0, "C:/Program Files/Webots/lib/controller/python")
os.environ["WEBOTS_HOME"] = "C:/Program Files/Webots"
os.add_dll_directory("C:/Program Files/Webots/lib/controller")
os.environ["PATH"] = "C:/Program Files/Webots/lib/controller;" + os.environ["PATH"]