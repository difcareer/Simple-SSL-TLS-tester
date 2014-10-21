#!/usr/bin/python2

import sys
import os
import subprocess
import threading

global tls1
global ssl2
global ssl3

opts = sys.argv[1:]
vers = [3,2,1]
tls1 = []
ssl2 = []
ssl3 = []
threads = []
threads_done = False
hosts = False

def show_help():
    print """
=====================================================================
 Quickly scan a list of hosts for various TLS and SSL compatibility.
=====================================================================

-h, --help:	Display this message

Usage:
------------------------------
 $ ./test_hosts.py HOSTS

Example:
------------------------------
 $ ./test_hosts.py example_hosts.txt

"""

if len(opts) <= 0:
    show_help()
else:
    for opt in opts:
        if (opt == '-h') or (opt == '--help'):
            show_help()
            quit()
    hosts = open(opts[0],'r')

def test_host(a_host):
    a_host = a_host.rstrip()
    a_host = a_host.lstrip()
    for ver_num in vers:
        cmd = ["curl","-silent","-"+str(ver_num),a_host]
        if ver_num == 1:
            proto = "TLS"
        else:
            proto = "SSL"

        try:
            resp = subprocess.check_output(cmd)
            if ver_num == 2:
                ssl2.append(a_host)
            elif ver_num == 3:
                ssl3.append(a_host)
            elif ver_num == 1:
                tls1.append(a_host)
        except:
            pass

print '\nTESTING HOSTS...'
for a_host in hosts:
    print a_host,
    t = threading.Thread(target=test_host,args=(a_host,))
    threads.append(t)
    t.start()

while threads_done == False: 
    threads_dead = 0
    for a_thread in threads:
        if a_thread.is_alive() == False:
            threads_dead += 1
    if threads_dead >= len(threads):
        threads_done = True


print '\n\nRESULTS:\n\n'
if len(tls1):
   print "+ TLSv1 ENABLED HOSTS:"
   print "+----------------------------"
   for a_host in tls1:
       print "|- "+a_host
   print "+----------------------------\n\n"

if len(ssl2):
   print "+ SSLv2 ENABLED HOSTS:"
   print "+----------------------------"
   for a_host in ssl2:
       print "|- "+a_host
   print "+----------------------------\n\n"

if len(ssl3):
   print "+ SSLv3 ENABLED HOSTS:"
   print "+----------------------------"
   for a_host in ssl3:
       print "|- "+a_host
   print "+----------------------------\n\n"
