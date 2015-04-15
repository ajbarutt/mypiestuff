#!/usr/bin/python

import pickle
from datetime import datetime

N = datetime.now()

print N

F = open("Output", 'wb')

pickle.dump(N, F)

F.close()

FA = open("Output", 'rb')

NEW = pickle.load(FA)

print NEW