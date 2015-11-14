import RPi.GPIO as GPIO
import time
import pika

#from flask import Flask
#from flask import render_template

GPIO.setmode(GPIO.BCM)
pinList = [17, 27]

for i in pinList: 
   GPIO.setup(i, GPIO.OUT) 
   GPIO.output(i, GPIO.HIGH)

#app = Flask(__name__)

SleepTimeL = 1 

#@app.route("/")
#def index():
#  return render_template("index.html") 

#@app.route("/main_door")
#def main_door():
#  """TODO: add relay code here"""
#  GPIO.output(17, GPIO.LOW)
#  time.sleep(SleepTimeL);
#  GPIO.output(17, GPIO.HIGH)
#  return render_template("index.html") 

#@app.route("/side_door")
#def side_door():
#  """TODO: add relay code here"""
#  GPIO.output(27, GPIO.LOW)
#  time.sleep(SleepTimeL);
#  GPIO.output(27, GPIO.HIGH)
#  return render_template("index.html") 

def callback(ch, method, properties, body):
  if body == 'main':
    GPIO.output(17, GPIO.LOW)
    time.sleep(SleepTimeL);
    GPIO.output(17, GPIO.HIGH)
  elif body == 'side':
    GPIO.output(27, GPIO.LOW)
    time.sleep(SleepTimeL);
    GPIO.output(27, GPIO.HIGH)
  print body

credentials = pika.PlainCredentials('garage', 'viviana1!')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='45.55.154.178',credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='door')
channel.basic_consume(callback, queue='door', no_ack=True)
channel.start_consuming()

#if __name__ == "__main__":
#  app.run(host='0.0.0.0', port=80)
