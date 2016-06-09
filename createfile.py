# -*- coding: utf-8 -*-
# Copyright 2016 Thomas Saliou - Abstrium SAS <team (at) pydio.com>
import random
import string
import os

lefile = "lefile10MB"
with open(lefile, "w") as f:
    i = 0
    while i < 10*10**4:
        i += 1
        f.write(random.choice(string.letters)*100)
print(os.path.getsize(lefile))

lefile = "lefile100MB"
with open(lefile, "w") as f:
    i = 0
    while i < 10*10**5:
        i += 1
        f.write(random.choice(string.letters)*100)
print(os.path.getsize(lefile))

lefile = "lefile1GB"
with open(lefile, "w") as f:
    i = 0
    while i < 10*10**6:
        i += 1
        f.write(random.choice(string.letters)*100)
print(os.path.getsize(lefile))

lefile = "lefile10GB"
with open(lefile, "w") as f:
    i = 0
    while i < 10*10**7:
        i += 1
        f.write(random.choice(string.letters)*100)
print(os.path.getsize(lefile))

