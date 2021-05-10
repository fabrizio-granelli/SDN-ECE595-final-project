
import time
import os
os.system("""curl -X POST -d '{"address":"10.0.1.1/24"}' http://localhost:8080/router/0000000000000001""")
os.system("""curl -X POST -d '{"address":"10.0.2.1/24"}' http://localhost:8080/router/0000000000000001""")
os.system("""curl -X POST -d '{"address":"10.0.3.1/24"}' http://localhost:8080/router/0000000000000001""")
os.system("""curl -X POST -d '{"address":"10.0.7.1/24"}' http://localhost:8080/router/0000000000000001""")


os.system("""curl -X POST -d '{"address":"10.0.4.1/24"}' http://localhost:8080/router/0000000000000002""")
os.system("""curl -X POST -d '{"address":"10.0.5.1/24"}' http://localhost:8080/router/0000000000000002""")
os.system("""curl -X POST -d '{"address":"10.0.6.1/24"}' http://localhost:8080/router/0000000000000002""")
os.system("""curl -X POST -d '{"address":"10.0.7.2/24"}' http://localhost:8080/router/0000000000000002""")

os.system("""curl -X POST -d '{"gateway": "10.0.7.2"}' http://localhost:8080/router/0000000000000001""")
os.system("""curl -X POST -d '{"gateway": "10.0.7.1"}' http://localhost:8080/router/0000000000000002""")
while True:
    os.system("bash case1.sh")
    print("----------------------------")
    print("----------------------------")
    print("----------------------------")
    print("----------------------------")
    print("-----NORMAL OPERATION------")
    print("----------------------------")
    print("----------------------------")
    print("----------------------------")
    print("----------------------------")




    time.sleep(60)
    os.system("bash case2.sh")
    print("----------------------------")
    print("----------------------------")
    print("----------------------------")
    print("----------------------------")
    print("-----EMERGENCY OPERATION----")
    print("----------------------------")
    print("----------------------------")
    print("----------------------------")
    print("----------------------------")
    time.sleep(60)
