ARG IMAGE
FROM $IMAGE

RUN pip install PILLOW 

COPY Python* /sut/SilAdapter

RUN python /sut/SilAdapter/install_runtime.py
