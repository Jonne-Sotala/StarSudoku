import os
from build.settings import ROOT_DIR
from build.initialize_database import initialize_database


def build():
    os.makedirs(os.path.join(ROOT_DIR, 'data'), exist_ok=True)
    initialize_database()


def build_test():
    os.makedirs(os.path.join(ROOT_DIR, 'data'), exist_ok=True)
    initialize_database(test=True)


if __name__ == "__main__":
    build()
    build_test()
