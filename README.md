# GpioPythonDocker

Dockerized gpio library for for Raspberry Pi

## Run 
```
docker run --privileged dschowta/gpiopy <python file>
```

For example run the example file
```
docker run --privileged  -v $(pwd):/home/example  dschowta/gpiopy /home/example/motionsensor.py

```

## Build Locally
```
docker build -t gpiopy .
```
