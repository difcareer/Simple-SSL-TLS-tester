Simple-SSL-TLS-tester
=====================

A simple and fast tool for testing SSL/TLS support against a list of hosts.

######Dependencies:
* python2.7
* curl 7.22+
* python-thread
* python-multiprocessing

######Usage:
`hosts.txt` contains a list of the domains you plan to test.

```
https://www.akamai.com
https://www.reddit.com
https://www.google.com
https://www.yahoo.com
...
```

`test_hosts.py` will read this list and using `curl` attempt to establish a TLSv1, SSLv2, and SSLv3 connection per host.  When it is done, it will produce a simple report listing which protocols were successful on which domains.

```
$ ./test_hosts.py 

TESTING HOSTS...
https://www.akamai.com
https://www.reddit.com
https://www.google.com
https://www.yahoo.com
https://duckduckgo.com
https://www.gmail.com
https://www.github.com
https://www.facebook.com
https://www.amazon.com
https://www.microsoft.com
https://www.etsy.com


RESULTS:


+ TLSv1 ENABLED HOSTS:
+----------------------------
|- https://www.akamai.com
|- https://www.reddit.com
|- https://www.github.com
|- https://www.facebook.com
|- https://duckduckgo.com
|- https://www.gmail.com
|- https://www.amazon.com
|- https://www.etsy.com
|- https://www.google.com
|- https://www.microsoft.com
|- https://www.yahoo.com
+----------------------------


+ SSLv3 ENABLED HOSTS:
+----------------------------
|- https://www.amazon.com
|- https://www.google.com
|- https://www.microsoft.com
|- https://www.yahoo.com
+----------------------------

```
