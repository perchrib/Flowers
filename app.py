from flask import Flask, render_template
#import RPi.GPIO as GPIO
import time


def gpio_setup(channel):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.OUT)

def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/turnOn', methods=['POST'])
def turnOn():
    channel = 10
    http_status_code = 204
    time.sleep(3)
    # try:
    #     gpio_setup(channel)
    #     motor_on(channel)
    #     time.sleep(2)
    #     motor_off(channel)
        
    # except:
    #     http_status_code = 501
    # finally:
    #     GPIO.cleanup()
    return "", http_status_code

if __name__ == '__main__':
    raspberry_local_ip = '192.168.0.69'
    app.run(host='0.0.0.0', port='5302')