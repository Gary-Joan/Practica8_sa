import time
import redis
from flask import Flask
import json
import jsonpickle
from json import JSONEncoder, dumps, loads

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
# The name of the Redis set

colorSet = "Colors"

 

# Add elements to the Redis set

cache.sadd(colorSet, "Red")

cache.sadd(colorSet, "Orange")

cache.sadd(colorSet, "Yellow")

cache.sadd(colorSet, "Green")

cache.sadd(colorSet, "Blue")

cache.sadd(colorSet, "Indigo")

cache.sadd(colorSet, "violet")

 

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

#ruta para poder ver los elementos guardados en el redis
@app.route('/')
def hello():
    print("Contents of the Redis set:")

    print(cache.smembers(colorSet))
    count = get_hit_count()
    sampleJson = jsonpickle.encode(cache.smembers(colorSet))
    lista = dumps(sampleJson, default=str)
    return lista
if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)