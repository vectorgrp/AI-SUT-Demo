# AI SUT for CANoe/CANoe4SW AI SIL Testing and Analysis Sample
## Prerequisites
- Python 3.8/3.9 64bit
- Installed CANoe/CANoe4SW>=16

## Introduction
The sample AI SUTs are designed to communicate with the AI SIL Testing and Analysis CANoe/CANoe4SW sample configuration. Please also visit the help site there if there are any problems.

## Available AI SUTs
This repository contains two AI SUTs. They demonstrated how an AI written in PyTorch or TensorFlow can communicate with CANoe/CANoe4SW. If everything is set up correctly, interactions between CANoe/CANoe4SW and SUT are printed out. Depending on the setup, some queries (in particular explainable AI queries) can take a few seconds. 
1. torch_sut.py: *recommended SUT* <br />
  In this SUT, an object detector from torchvision is loaded. The detector is pretrained on the [COCO dataset](https://cocodataset.org/#home). The top 3 annotations are displayed in the CANoe/CANoe4SW sample configuration. For the top 1 annotation, an explanation can be generated.
2. tf_sut.py: <br />
  This SUT demonstrates how an image classifier from TensorFlow can work with CANoe/CANoe4SW. Because an image classifier only classifies the whole image, no bounding boxes are generated and only the input image is shown in the CANoe/CANoe4SW sample configuration. Also, the automatic test may not pass, because image classifiers are mostly trained on the [ImageNet dataset](https://www.image-net.org/) instead of COCO. The ImageNet label IDs are tried to convert to COCO labels IDs.

## Installation steps for a local Windows machine
1. Start a shell e.g. in Visual Studio Code or IDE of choice
   - Recommended: Load the whole repository in an IDE such as Visual Studio Code and then start a shell/terminal there
2. Optional: Activate a python development environment (e.g. virtual environment)
3. Install dependencies like TensorFlow and PyTorch in the shell via `pip install -r requirements.txt`
4. Install CANoe-SilAdapter module in the shell via executing the enable_SilAdapter.py file with `python enable_SilAdapter.py`
5. Run a SUT either in the shell (e.g. `python torch_sut.py`) or IDE of choice 
6. Switch to the CANoe/CANoe4SW sample configuration. If everything is correctly set up, the SUT will display messages whenever it receives new data from CANoe/CANoe4SW.
7. If there is a `[ Warning ] Could not connect to rtinode at '{IP address}', retrying...` displayed, please check if the CANoe/CANoe4SW sample configuration is running.

## Installation steps on a remote machine
1. Checkout this repository on the remote machine
2. Copy the folder "Python Runtime" from the CANoe/CANoe4SW installation folder ({CANoe Installation Folder}\Installer Additional Components\SilAdapter\Python Runtime) into this repository on the remote machine
3. Start a shell on the remote machine
   - Recommended: Load the whole repository in an IDE such as Visual Studio Code and then start a shell/terminal there
4. Optional: Activate a python development environment (e.g. virtual environment)
5. Install dependencies like TensorFlow and PyTorch in the shell via `pip install -r requirements.txt`
6. Install CANoe-SilAdapter module in the shell via executing the enable_SilAdapter.py file with `python enable_SilAdapter.py`
7. Get the IP address of your local machine with the CANoe/CANoe4SW installation (run `ipconfig` in a shell on the local machine) 
8. Setting an environment variable with IP address on the remote machine shell for the SUT to access the local CANoe/CANoe4SW installation. For a Linux system, type in the shell `export VSIL_CONNECTION_ADDRESS={LocalCANoeIPAddress}`. For a Windows system, type `set SIL_CONNECTION_ADDRESS={LocalCANoeIPAddress}` in a cmd-shell or `$env:VSIL_CONNECTION_ADDRESS ={LocalCANoeIPAddress}` in a powershell
9. Run a SUT either in the shell (e.g. `python torch_sut.py`) or IDE of choice 
10. If there is a `[ Warning ] Could not connect to rtinode at '{IP addresse}', retrying... ` displayed, please check if the VSIL_CONNECTION_ADDRESS was correctly set or if the CANoe/CANoe4SW sample configuration is running.
11. Switch to the CANoe/CANoe4SW sample configuration. If everything is correctly set up, the SUT will displays messages whenever it receives new data from CANoe/CANoe4SW.

## Installation steps on Linux remote system with Docker
1. Checkout this repository on the remote machine
2. Copy the folder "Python Runtime" from the CANoe/CANoe4SW installation folder ({CANoe Installation Folder}\Installer Additional Components\SilAdapter\Python Runtime) into this repository on the remote machine
3. Get the IP address of your local machine with the CANoe/CANoe4SW installation (run `ipconfig` in a shell on the local machine) 
4. Start a shell on the remote machine
   - Recommended: Load the whole repository in an IDE such as Visual Studio Code and then start a shell/terminal there
5. Setting an environment variable with IP address on the remote machine shell for the SUT to access the local CANoe/CANoe4SW installation. For a Linux system, type in the shell export `VSIL_CONNECTION_ADDRESS={LocalCANoeIPAddress}`.
6. Build a docker image via `docker-compose build` in the remote shell
7. Start an AI SUT via `docker-compose up torch_sut`
8. If there is a `[ Warning ] Could not connect to rtinode at '{IP address}', retrying...` displayed, please check if the VSIL_CONNECTION_ADDRESS was correctly set.
9. Switch to the CANoe/CANoe4SW sample configuration. If everything is correctly set up, the SUT will displays messages whenever it receives new data from CANoe/CANoe4SW.

## FAQ:
1. ERROR: Could not find a version that satisfies the requirement tensorflow (from versions: none),ERROR: No matching distribution found for tensorflow: <br />
   Check if the python version is a 64-bit python 3.8/3.9 version by typing `python` in the shell. Check python version and whether it runs on win64.


