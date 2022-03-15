from distutils.log import error
import os
import argparse

parser = argparse.ArgumentParser(description="SIL Adapter Install")

parser.add_argument("--install_dir", default="", type=str, help="Installation folder of CANoe/CAnoe4SW")

inp = parser.parse_args()
canoe_wheel_path=[]


if os.path.isdir(os.path.join(inp.install_dir, "Installer Additional Components\\SilAdapter\\Python Runtime")):
    print("CANoe installation folder found ")
    canoe_path = inp.install_dir
else:
    print("Trying to find CANoe installation folder via environment variables or local folder")
    if "CANoe_InstallDir64s" in os.environ:
        print("CANoe installation folder found")
        canoe_path = os.environ["CANoe_InstallDir64"]
    elif "CANoe4SW_InstallDir64" in os.environ:
        print("CANoe4SW installation folder found")
        canoe_path = os.environ["CANoe4SW_InstallDir64"]
    elif os.path.isdir(os.path.join(os.getcwd(), "Python Runtime")):
        print("Local Python Runtime folder found")
        canoe_path = os.path.join(os.getcwd(), "Python Runtime")
        canoe_wheel_path = os.path.join(canoe_path,"install_runtime.py")
    else:
        error("No CANoe installation folder found, please check if --install_dir was correctly defined")
        exit()


if canoe_path:
    canoe_path = os.path.abspath(os.path.join(canoe_path, os.pardir))
    if not(canoe_wheel_path):
        canoe_wheel_path = os.path.join(canoe_path, "Installer Additional Components\\SilAdapter\\Python Runtime\\install_runtime.py")
        print(os.path.abspath(canoe_wheel_path))

__file__ = canoe_wheel_path

exec(open(canoe_wheel_path).read())