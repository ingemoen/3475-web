import uuid
import redis
from flask import Flask, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = "d7fc8394709711eb94390242ac130002"

redisCache = redis.Redis(host='qnap.homezone', port=6379)

def setSetup(hostName, currentUuid):
    return


def getSetup(hostName):
    if 'uuid' not in session:
        session['uuid'] = uuid.uuid1().hex
    
    currentUuid = session.get('uuid')

    if not redisCache.exists(currentUuid):
        print(f"Key does not exists : {currentUuid}")
        setSetup(hostName, currentUuid)

    print(f"Session set to : {currentUuid}" )

    return currentUuid


    ##host = host_url
    ## 
    ## parsed_url = urllib.parse.urlparse('https://www.example.com/page.html')
    ## print(parsed_url)

@app.route('/')
def hello():
    setup = getSetup(request.host)
    print(f"Setup : {setup}")

    req = request.host
    return f"Hello Worlds!, {req} "

if __name__ == '__main__':
    app.run(host='0.0.0.0')