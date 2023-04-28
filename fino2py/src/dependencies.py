'''
This script is just housing the dependencies for the other scripts in the src folder.
It is not intended to be run as a script.
The dependencies are:
    - pathlib
    - pandas
possible future dependencies:
    - csv
'''

import pathlib as pl
import pandas as pd
from functools import reduce
from typing import Union, Tuple, Optional
from datetime import datetime