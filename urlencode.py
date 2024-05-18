import urllib.parse
import sys

encoded_str = urllib.parse.quote(sys.argv[1])
print(encoded_str) 
