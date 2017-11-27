import os
import sys

print(os.path.dirname(sys.argv[0]))
basePath = os.path.dirname(sys.argv[0])
print("".join(basePath) + "/resource/un.csv")
print(os.path.abspath(os.path.dirname(sys.argv[0])))
print(os.path.abspath(".."))