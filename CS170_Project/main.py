import os
import sys
import numpy as np

from src.state import State
from src.menu import main_menu
from src.search_functions import Algorithms

sys.path.append(os.getcwd()) #you can access files in the same directory this way

main_menu()