import psutil
import speedtest
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/cpu')
def get_cpu():
    cpu = psutil.cpu_percent()
    cpu = str(int(cpu))+"%"
    return {'cpu': cpu}

@app.route('/velocidad')
def get_vel():
    v = speedtest.Speedtest()
    vel = str(int(v.download()/1000000))+"Mbps"
    return{'velocidad': vel}

@app.route('/memoria')
def get_memo():
    memo = str(int(psutil.virtual_memory().active/(1024**2)))+"MB"
    return {'memoria': memo}

if __name__ == '__main__':
    app.run()
