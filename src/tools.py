import socket
import sys

def getMem(sock):
    sock.sendto(b'GETMEM_t', ('127.0.0.1', 5005))
    data, addr = sock.recvfrom(1024)
    for i in data.decode('utf-8').split(','):
            print((int(i.split(' ')[0]),i.split(' ')[1],i.split(' ')[2]))

def getPred(sock):
    sock.sendto(b'GETPRED', ('127.0.0.1', 5005))
    data, addr = sock.recvfrom(1024)
    print(data.decode('utf-8'))

def getSelf(sock):
    sock.sendto(b'GETSELF', ('127.0.0.1', 5005))
    data, addr = sock.recvfrom(1024)
    print(data.decode('utf-8'))

def getSucc1(sock):
    sock.sendto(b'GETSUCC1', ('127.0.0.1', 5005))
    data, addr = sock.recvfrom(1024)
    print(data.decode('utf-8'))

def getSucc2(sock):
    sock.sendto(b'GETSUCC2', ('127.0.0.1', 5005))
    data, addr = sock.recvfrom(1024)
    print(data.decode('utf-8'))

def getLoss(sock):
    sock.sendto(b'GETLOSS', ('127.0.0.1', 5005))
    data, addr = sock.recvfrom(1024)
    print(data.decode('utf-8'))




if __name__ == "__main__":
    sockObj = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sockObj.bind(('127.0.0.1', 5006))
    if sys.argv[1] == 'list_mem':
        getMem(sockObj)
    if sys.argv[1] == 'list_self':
        getSelf(sockObj)
    if sys.argv[1] == 'list_pred':
        getPred(sockObj)
    if sys.argv[1] == 'list_succ1':
        getSucc1(sockObj)
    if sys.argv[1] == 'list_succ2':
        getSucc2(sockObj)
    if sys.argv[1] == 'set_loss_3':
        sockObj.sendto(b'SETLOSS_3', ('127.0.0.1', 5005))
    if sys.argv[1] == 'set_loss_30':
        sockObj.sendto(b'SETLOSS_30', ('127.0.0.1', 5005))
    if sys.argv[1] == 'set_loss_0':
        sockObj.sendto(b'SETLOSS_0', ('127.0.0.1', 5005))
    if sys.argv[1] == 'get_loss':
        getLoss(sockObj)

