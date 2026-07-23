import os
import shutil
import subprocess
import urllib.request
import zipfile
import platform

UI = "https://github.com/RobloxScripts-dev/package/raw/refs/heads/main/package.zip"
ZA = "package.zip"

def cmd(x):
    subprocess.run(x, check=True)

def install_unzip():
    if shutil.which("unzip"):
        return

    system = platform.system()

    if system == "Linux":
        if shutil.which("apt"):
            cmd(["sudo", "apt", "update"])
            cmd(["sudo", "apt", "install", "-y", "unzip"])
        elif shutil.which("pkg"):
            cmd(["pkg", "install", "-y", "unzip"])
        elif shutil.which("apk"):
            cmd(["apk", "add", "unzip"])
        else:
            raise RuntimeError("No supported package manager found")
    else:
        raise RuntimeError("Install unzip manually")

def download():
    if not os.path.exists(ZA):
        urllib.request.urlretrieve(UI, ZA)

def extract():
    with zipfile.ZipFile(ZA) as z:
        z.extractall("package")

def run():
    os.chdir("package")

    if not os.path.exists("main.py"):
        raise FileNotFoundError("main.py not found")

    cmd(["python3", "main.py"])

if __name__ == "__main__":
    install_unzip()
    download()
    extract()
    run()
