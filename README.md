# ZMQ with docker-compose

docker-compose file with a simple ZMQ queue, based on the example presented on
http://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/devices/queue.html


Start with:
```
docker-compose up --scale server=1
```

Ouput example:

```
[{'label': 'cim', 'confidence': 0.9525, 'box': [336.5, 301.99, 439.43, 486.87]}, {'label': 'cim', 'confidence': 0.9506, 'box': [212.58, 172.13, 321.44, 338.93]}, {'label': 'cim', 'confidence': 0.9501, 'box': [280.32, 131.93, 384.38, 306.51]}, {'label': 'cim', 'confidence': 0.9476, 'box': [275.16, 281.35, 367.56, 483.91]}, {'label': 'cim', 'confidence': 0.9438, 'box': [282.15, 470.97, 385.78, 589.05]}, {'label': 'cim', 'confidence': 0.9393, 'box': [150.64, 120.41, 246.34, 214.31]}, {'label': 'cim', 'confidence': 0.9382, 'box': [197.31, 287.65, 261.89, 486.8]}, {'label': 'cim', 'confidence': 0.9337, 'box': [146.83, 246.75, 196.07, 431.97]}, {'label': 'cim', 'confidence': 0.9312, 'box': [141.82, 439.44, 196.09, 588.83]}, {'label': 'cim', 'confidence': 0.931, 'box': [210.1, 481.55, 259.17, 588.89]}]
```
