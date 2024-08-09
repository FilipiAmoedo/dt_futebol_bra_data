import subprocess
from project_conf import DEPENDENCIAS_INTERNAS, DEPENDENCIAS_EXTERNAS
import sys
from os import path
PROJECT_ROOT = path.dirname(path.dirname(path.abspath(__file__)))

REMOTE_FOLDER_INT = path.join(path.expanduser('~'), 'Documents', 'repo_wheels')


def update():
    # @TODO Preciso fazer listar o workingset.
    subprocess.run(sys.executable + f" -m pip install  --upgrade pip",  shell=True, check=True)
    subprocess.run(
        sys.executable + f" -m pip install  --upgrade --find-links=file:{REMOTE_FOLDER_INT} {' '.join(DEPENDENCIAS_INTERNAS)}"
                         f" {' '.join(DEPENDENCIAS_EXTERNAS + ['wheel'])}",  shell=True, check=True)
    subprocess.run(sys.executable + ' -m pip freeze > requirements.txt', shell=True, check=True, cwd=PROJECT_ROOT)


if __name__ == '__main__':
    update()