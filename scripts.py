import shlex
import subprocess
import sys


def python(file):
    run(f"{shlex.quote(sys.executable)} {file}")


def python_module(module):
    run(f"{shlex.quote(sys.executable)} -m {module}")


def run(command):
    subprocess.run(shlex.split(command))


def format():
    run("isort ./scripts.py ./build.py")
    run("black ./scripts.py ./build.py")


def build():
    python("./build.py")


def start():
    python_module("http.server")
