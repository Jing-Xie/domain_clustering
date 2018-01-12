import sys

from fingerprint_v import FingerPrint


f = FingerPrint()

for line in sys.stdin:
    try:
        print "%s\t%s" % (f.bigram_fingerprint(line), line.strip())
    except:
        pass
