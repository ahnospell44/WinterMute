import sys
import greynoise
gn = greynoise.GreyNoise(offering="community")
out = gn.ip(str(sys.argv[1]))
print (out)
