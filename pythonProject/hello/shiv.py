# # i am infinite
# # hello guys today we are going to create a program
# # hello guys we are going to create some program we need to have a clear vision on it
# # hello guys we are going to learn about exceptions in this program
# # inta = input("sir please enter the input :  ")
# # if inta=="hello":
# #     raise Exception("this is not valid")
# # raise is used to raise an exception
# # while except is used to handle an exception
# # the above one is an example of exception handling in python
# # try and except is one of the things you need to be proficient at
# # there are many exceptions in python you can learn about them to use it in your program just have a look on them
# exa = "json"
# try:
#     print(a)
# except Exception as e:
#     print("e")
#
# # or you can generally print any statement instead of e you can also print a statement like hello json
# # the above code gives value name 'a' is not defined we need to have a perfect vision on them
# a = int(input("sir please enter the value"))
# b = int(input("sir please enter the value"))
# print(a/b)
# if b==0:
#     raise ZeroDivisionError("sir b should not equal to 0")
# # now guys let's raise and other exception we need to have idea about
# # i do not have anything to do with it
# # if exception is raised anywhere in the code then the code below it does not function
# a = input("sir please enter the value")
# if a=="shiva":
#     print(a)
# else:
#     try:
#         print(a)
#     except Exception as e:
#         raise ValueError("sir your word is not recognised")
#     else:
#         print("see the code worked properly with no exception")
#     finally:
#         print("this statement prints at any cost")
# # see the basic syntax is we need to have a clear vision on our topic
# # now let's write a code which is just opposite to the above code
# a = input("sir please enter the value")
# if a=="ori":
#     print(a)
# else:
#     try:
#         print(c)
# # during try if the above code doesn't work properly then the program itself raises an exception we need to hava a view
#     except Exception as e:
#         raise ValueError("sir your word is not recognised")
#     else:
#         print("see the code worked properly with no exception")
#     finally:
#         print("this statement prints at any cost")
# the persons who prepared python needs to be highly intellectual about the concepts they have
# now let's prepare a program using the above topics to have a clear vision on them
print("--------------------------hello guys this is a program----------------------------")
print("this is the program which tells about samrats of india we need to have a clear vision on them")
# intar = input("sir please enter the name of the great samrats of india in your acqiuantance ")
# dict1 = {"Ajatashatru":"Ajatashatru ruled Magadha and was from the Haryanka dynasty. His father was Emperor Bimbisara, Ajatashatru captured his father by capturing power. Ajatashatru took place in the time of Buddha and Mahavira and gave him complete patronage. Ajatshatru defeated Vajji and gained control of a large state like Vaishali. Ajatashatru defeated his brother who was the ruler of the Khosla kingdom and also gained suzerainty over Khosla. In Ajatashatru’s time, Magadha was a very powerful kingdom of Madhya Bharat.","Chandragupta Maurya":"Chandragupta, the founder of the Maurya dynasty, known as the first Ahmaraja of India, started his campaign after attaining Chanakya Rupi the great strategist as a guru and started winning the war at the young age of 20. He was fully capable of resisting Alexander’s invasion of India. As a child, Chandragupta was seen by Chanakya at Taxila, he realized the brilliance of the child Chandragupta and he gave good education to Chandragupta. After growing up, Chandragupta started his kingdom by destroying the Nanda dynasty, he also captured Magadha and extended his kingdom in the west to Iran. Alexander’s commander at that time, Selukas, ruled there. Chandragupta defeated him in battle and took back a lot of kingdom."}
# if intar in dict1:
#     print(dict1[intar])
# else:
#     try:
#         print(bx)
#     except Exception as e:
#         raise  ValueError("sir we do not have any information regarding your input")
#     else:
#         print("sir we have information regarding your input")
#     finally:
#         print("sir if you wish you can search more")
# see we have made a program using the tools now let's go with another one using regular expressions and other things
# import re
# ints = input("sir please enter the input ")
# dict2 = {"Emperor Ashoka":"Ashok the Great was a ruler whose kingdom extended from Afghanistan to Burma and from Kashmir to Tamil Nadu. His capital was Pataliputra. Ashoka is considered the most powerful king in the history of India. Ashoka was the third ruler of the Maurya dynasty, Ashoka was a very harsh ruler in his early days, hence he was called Chand Ashoka. But seeing the death of millions of people in the Kalinga war, his heart changed and he gave up his campaign of expansion. Emperor Ashoka contributed a lot in spreading Buddhism abroad. The national emblem of India and the wheel of the flag are taken from the Ashoka Pillar.","Samudragupta":"Samudragupta was the king of the Gupta dynasty who never lost any war in his entire life. Together with his son Vikramaditya, he started the Golden Age of India. He started the practice of currency and made gold currencies. Cultural rise of India took place in his kingdom."}
# if re.findall("[E-Fe-f]*\s[A-Ba-b]*oka",ints):
#     print(dict2["Emperor Ashoka"])
#     if ints!="Emperor Ashoka":
#         print("sir please check your spelling,and punctuation marks")
# elif re.findall("[S-Ts-t]*ta",ints):
#     print(dict2["Samudragupta"])
#     if ints!="Samudragupta":
#         print("sir please check your spelling,and punctuation marks")
# else:
#     try:
#         print(nothing)
#     except Exception as e:
#         raise ValueError("sir the problem might be of due to two reasons either your input is wrong or we do not have the output for your input")
#     else:
#         print("sorry,we have not output")
#     finally:
#         print("sir if you wish you can run the program again")
# see when exception araises then else and finally stops working
# see we are handling error in this program now
# finally our program is ready
# hello guys now we are going to learn the difference between is & == symbol so let's have a quick review on that
# here == defines whether the two values value is equla or not
# and is defines whether the two values are same or indicate to same object
list1 = [6,5,"0"]
list2 = [6,5,"0"]
# you can see that the below statement gives false because list1 and list2 are independent statements
# even though value is same
print(list2 is list1)
print(list2==list1)
# you can see that == is true
list1 = list2
print(list2 is list1)
# you can see that now the value is true as both indicate to same function or object
print(list2==list1)
# now let's try a new thing and just go with it
list3 = [5,6,9]
list4 = [67,9,5]
list3=list4
print("hello" + str(list3 is list4))
print("mission" + str(list3==list4))
# see you can understand now the solution more easily now have a quick recap
# now let's learn about another function
string = "i am a good boy vishwanath"
print(string[:])
print(string[1:5])
print(string[1::2])
print(string[::-1])
print("hello guy "+string[-4:-1:2])
# the above code removes every second character from forward
print("hello dhruva "+string[-12:-1:-2])
# now i have understood that using integers starting from 1 in skip slice dissapers the entire string
# i think you should put an eye on this afterwards so that it would be good
print("hallo dhruva ")
# we are now going to create some variable now let's a quick review on this to develop ourselves now let's boost our knowledge
print(string.isalnum())
hello = "shiva shiva is great"
print(hello.isalnum())
print(hello.isalpha())
print(hello.isnumeric())
print(hello.count("s"))
print(hello.capitalize())
print(hello.upper())
print(hello.isupper())
print(hello.lower())
print(hello.islower())
print(hello.title())
# title is awesome
print(hello.endswith("great"))
# see now you have got enough functions you can use them to clarify your things
