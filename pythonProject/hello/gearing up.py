# i am infinite
# hello guys today we are going to create a program on regular expressions so let's have a look at it
import re
# the above one is a module imported for regular expressions
mystr = "In the above two excerpts, one can observe that the number ’20’ appears alpha23 in both numeric and 5681-999alphabetical forms. apap Simply following the pre-processing steps, that involve tokenization, lemmatization and so on would not be able to map ’20’ and ‘twenty’ to the same stem, which is of contextual importance. Luckily, we have the in-built library, num2words which solves this problem in a single line."
# shiva = re.compile(r"above two")
# you can even compare two words
# shiva = re.compile(r".")
# the above code runs all values except new line character
# shiva = re.compile(r"^two")
# shiva = re.compile(r"^In")
# the above code is only implemented when it starts with In
# shiva = re.compile(r".$")
# the above code is only executed when the . is in end of the string
# shiva = re.compile(r"ap*")
# the above code is only executed when a is present and p presence is neglected to zero or more than 0
# shiva = re.compile(r"ap+")
# the above code is only executed when a is present and p presence should be one and can be more
# shiva = re.compile(r"a*p*")
# the above code is only executed when a is not present or is more than 0 and similar with p or ap
# shiva = re.compile(r"(ap){2}")
# here ap is grouped and the meaning of the code is that ap should be present at least 2 times
# shiva = re.compile(r"\AIn")
# the above code only runs when In is in starting of the code
# shiva = re.compile(r"\bIn")
# the above code only runs it means it gives it's presence in the output if In is present in beginning of the code or at ending
# shiva = re.compile(r"\Bo")
# shiva = re.compile(r"\d{4}-\d{3}")
# the above code gives you the value of the digits which have number of values as mentioned in the brackets so let's be with our code we need to have a clear understanding on the code
# shiva = re.compile(r"\AIN|two")
# the above code gives two mentioned values if both are satisfied and gives only of if anything is not satisfied
# this regular expressions have good functionality in programming we need to use them so that we can grow good
shiva = re.compile(r"alpha")
print(mystr[71:79])
xr = shiva.finditer(mystr)
for r in xr:
    print(r)
print(mystr[60:62])
# the above one says about the word to split
# hello guys today we are going to create a python file