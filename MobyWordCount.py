import collections
import string
# Reading the text in mobydick.txt and removing punctuation, returning text to the list new_moby
with open("/home/austin/Documents/Source_Allies/mobydick.txt") as f:
    moby_list = f.read()
    new_moby = moby_list.translate(str.maketrans("","" , string.punctuation)).lower().split()
# Reading and returning text from stop-words.txt, returning text to the list stop_list
with open("/home/austin/Documents/Source_Allies/stop-words.txt") as fp:
    stop_list = fp.read().split()

words =[]
# Removing stop words from new_moby list
for word in new_moby:
    if word.lower() not in stop_list:
        words.append(word)
# Using collections.Counter and .most_common to return the 100 most common words
most_common = collections.Counter(words).most_common(100)


print(most_common)