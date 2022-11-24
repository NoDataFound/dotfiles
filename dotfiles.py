import os
import fade

ssctxt= r""" 







                             _       _   
                           _| | ___ | |_ 
                          | . || . ||  _|
                          |___||___||_|   
 """
sectx2 = r"""


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
fadedssc = fade.water(ssctxt)
fadedssc2 = fade.purplepink(sectx2)

for pair in zip(*map(str.splitlines, (fadedssc, fadedssc2))): 
  print(*pair)
print(' '*71+"\033[36mv0.1")