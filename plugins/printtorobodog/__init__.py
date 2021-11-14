#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing.connection import Client

address = ('localhost', 6000)
conn = Client(address, authkey='secret password')
j=0
while j<3:
    conn.send('elooo')
    j=j+1;
# can also send arbitrary objects:
# conn.send(['a', 2.5, None, int, sum])
# conn.send('close')
# conn.close()



def run(readable_results, data, rawbuf):
    conn.send('readable_results')
    print "results sent to listener"

