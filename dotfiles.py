import os
import fade

dot= r""" 







                             _       _   
                           _| | ___ | |_ 
                          | . || . ||  _|
                          |___||___||_|   
 """
files = r"""


                                           ______  __ __                   
                                          /      \|  \  \                  
                                         |  ▓▓▓▓▓▓\\▓▓ ▓▓ ______   _______ 
                                         | ▓▓_  \▓▓  \ ▓▓/      \ /       \
                                         | ▓▓ \   | ▓▓ ▓▓  ▓▓▓▓▓▓\  ▓▓▓▓▓▓▓
| ▓▓▓▓   | ▓▓ ▓▓ ▓▓    ▓▓\▓▓    \ 
| ▓▓     | ▓▓ ▓▓ ▓▓▓▓▓▓▓▓_\▓▓▓▓▓▓\
| ▓▓     | ▓▓ ▓▓\▓▓     \       ▓▓
\▓▓      \▓▓\▓▓ \▓▓▓▓▓▓▓\▓▓▓▓▓▓▓ 
"""
fadeddot = fade.water(dot)
fadedfiles = fade.purplepink(files)

for pair in zip(*map(str.splitlines, (dot, files))): 
  print(*pair)
print(' '*71+"\033[36mv0.1")
