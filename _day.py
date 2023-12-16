import sys
from pathlib import Path
d = sys.argv[1]
Path(f'day{d}.txt').touch()
Path(f'day{d}.py').touch()
Path(f'day{d}_test.txt').touch()