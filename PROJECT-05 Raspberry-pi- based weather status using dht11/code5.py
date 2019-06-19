import Adafruit_DHT 
sensor = Adafruit_DHT.DHT11 
pin = 4
while:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin) 
    print(temperature) 
    print(humidity) 
