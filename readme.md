# AI SUT for CANoe/CANoe4SW 16 AI SIL Testing and Analysis Sample
## Prerequisites
- Python3.8/3.9
- Installed CANoe/CANoe4SW

## Installation step for a local Windows machine
1. Start a shell e.g. in Visual Studio Code or IDE of choice
2. Optional: Activate a python development environment (e.g. virtual environment)
3. Install dependencies and TensorFlow and PyTorch via pip install -r requirements.txt
4. Install CANoe-SilAdapter module via executing the enable_SilAdapter.py file with python enable_SilAdapter.py
5. Run tf_sut.py or torch_sut.py either via shell (python torch_sut.py) or IDE of choice 