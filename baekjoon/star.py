n = int(input())

for i in range(1, n+1):
  print("*" * i)
  
# *
# **
# ***
# ****
# *****

##################################

n = int(input())

for i in range(1, n+1):
  print(" " * (n - i), end="")
  print("*" * i)
  
#     *
#    **
#   ***
#  ****
# *****

##################################

n = int(input())

for i in range(n, 0, -1):
  print("*" * i)
  
# *****
# ****
# ***
# **
# *

##################################

n = int(input())

for i in range(n, 0, -1):
  print(" " * (n - i), end="")
  print("*" * i)

# *****
#  ****
#   ***
#    **
#     *

##################################

n = int(input())

for i in range(1, n + 1):
  print(" " * (n - i), end="")
  print("*" * (int(i * 2) - 1))
  
#     *
#    ***
#   *****
#  *******
# *********

##################################

n = int(input())

for i in range(n, 0, -1):
  print(" " * (n - i), end="")
  print("*" * (int(i * 2) - 1))
  
# *********
#  *******
#   *****
#    ***
#     *

##################################

n = int(input())

for i in range(1, n + 1):
  if(i == n): break
  print(" " * (n - i), end="")
  print("*" * (int(i * 2) - 1))

for i in range(n, 0, -1):
  print(" " * (n - i), end="")
  print("*" * (int(i * 2) - 1))

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
  
##################################

n = int(input())

for i in range(1, n + 1):
  if(i == n): break
  print("*" * i, end="")
  print(" " * (n - i), end="")
  print(" " * (n - i), end="")
  print("*" * i)

for i in range(n, 0, -1):
  print("*" * i, end="")
  print(" " * (n - i), end="")
  print(" " * (n - i), end="")
  print("*" * i)
  
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

##################################

n = int(input())

for i in range(n, 0, -1):
  if 1 == i: break
  print(" " * (n - i), end="")
  print("*" * (int(i * 2) - 1))

for i in range(1, n + 1):
  print(" " * (n - i), end="")
  print("*" * (int(i * 2) - 1))
  
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

