# i am infinite
# hello guys today we are going to write a email collector
import re
sr = """
hello@gmail.net
hello@gmail.org
hello@gmail.co
/sh10@gmail.omaa89
shiva
hello@gmail.n
i am a good person
"""
# built a perfect email collector to be a perfect builder and have experience in it as a builder
# we need to always create a perfect email collector
# if something doesn't come play a hit and trial method we need to very intrested in this topic and we need to have
# pe = re.findall("[\w/%&<>^@!]*@[\w/%]*",sr)
se = re.findall("\w[\w/%#`{_$?+|&^!*-]{1,64}\w[\w]@[\w/%]*.[\w]{2,6}|net|org|com",sr)
for line in se:
    print(line)
# so guys this is a basic email collector