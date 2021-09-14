#Unique Word Counter created and written by Bahram Esmailian
#simply change the string below to some phrase in the form of "word word word"

#Excerpt from Godel, Escher, Bach: an Eternal Golden Braid by Douglas R. Hofstadter Pg. 29
string = """Achilles: What is that strange flag down at the other end of the track?
It reminds me somehow of a print by my favorite artist, M.C. Escher.
Tortoise: That is Zeno's flag.
Achilles: Could it be that the hole in it resembles the holes in a Mobius strip Escher 
once drew? Something is wrong about that flag I can tell.
Tortoise: The ring which has been cut from it has the shape of the numerical for zero, 
which is Zeno's favorite number.
Achilles: But zero hasn't been invented yet! It will only be invented by a Hindu mathematician
some millenia hence. And thus, Mr. T, my argument proves that such a flag is impossible.
Tortoise: Your argument is persuasive, Achilles, and I must agree that such a flag is
impossible. But it is beautiful anyways, is it not?
Achilles: Oh, yes, there is not doubt of its beauty."""

array = string.split()
unique_words = set(array)
word_dict = {}
for word in array:
	if word not in word_dict:
		word_dict[word] = 1
	elif word in unique_words:
		word_dict[word] += 1

print(word_dict)
