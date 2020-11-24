import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

DATABASE_FILENAME = 'database.db'
DATABASE_PATH = os.path.join(ROOT_DIR, 'data', DATABASE_FILENAME)
