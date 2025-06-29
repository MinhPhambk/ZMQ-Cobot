FROM python:3.9
WORKDIR /app
COPY requirements.txt ./
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./queue_server.py" ]
