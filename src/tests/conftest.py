import os
from build.settings import ROOT_DIR
from build.initialize_database import initialize_database


def pytest_configure():
    os.makedirs(os.path.join(ROOT_DIR, 'data'), exist_ok=True)
    initialize_database(test=True)
