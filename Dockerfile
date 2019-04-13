# Version: 0.0.1
FROM python:latest
ADD KMT_method.py /
RUN pip install pystrich
CMD [ "python", "./KMT_method.py" ]