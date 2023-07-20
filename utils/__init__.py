import os
import glob

_all_=[os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+"/*.py")]