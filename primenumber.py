from flask import Flask, request, render_template
import time
import os
import socket

app = Flask(__name__)

# Reload itself if code changes
app.debug=True

@app.route('/primenumber/from/<int:fromNum>/to/<int:toNum>')
def primenumber(fromNum,toNum):

    if fromNum is None:
        fromNum = 2
    if fromNum<2:
        tromNum = 2

    if toNum is None:
        toNum = 1000

    fromNumStr = str(fromNum)
    toNumStr   = str(toNum)
    # print("Generating prime numbers from " + fromNumStr + "-" + toNumStr)

    hostname  = socket.gethostname()

    # print([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith(""127."")][:1])
    # print(socket.gethostbyname_ex(socket.gethostname())[2][0])

    ipAddress = request.host.split(':')[0]
    # print("Hostname=" + hostname + "and IP-address=" + ipAddress)

    # Start timer
    startTime = time.time()

    numberOfPrimeNumbers = 0
    primeNumbers = ""

    # Calculate primenumbers
    for num in range(fromNum,toNum + 1):
        # prime numbers are greater than 1
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                primeNumbers += str(num) + " "
                numberOfPrimeNumbers +=1
    
    # Stop timer
    stopTime = time.time()

    # print("Prime numbers=" + primeNumbers)

    # Calculate the elapsed time
    elapsedTime = str(stopTime - startTime)
    print("Elapsed time=" + elapsedTime)
 
    html = "<html>" \
        "<head><title>Prime number genetator</title></head>" \
        "<body>" \
        "<h2>Prime Number Generator!</h2>" \
        "<p>Generating prime numbers between {fromNum} - {toNum}</p>" \
        "<p>Number of prime numbers= {numberOfPrimeNumbers}</p>" \
        "<p>Elapsed time={elapsedTime} seconds</p>" \
        "<p>Hostname={hostname}, IP address={ipAddress}</p>" \
        "</body>" \
        "</html>"
    
    # "<p>Prime numbers= {primeNumbers}</p>" \
    return html.format(hostname=socket.gethostname(), ipAddress=request.host.split(':')[0],fromNum=fromNumStr, toNum=toNumStr, primeNumbers=primeNumbers, numberOfPrimeNumbers=numberOfPrimeNumbers, elapsedTime=elapsedTime)

@app.route('/')
def root():
    return "<html><head><title>Prime number genetator</title></head><body><h2>Prime number generator</h2></body></html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8899,threaded = True)
