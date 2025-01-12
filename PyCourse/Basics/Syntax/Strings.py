#Indexing
#Left to Right will be 0 - n
#Rigth to Left will be -1 - n
text = "We're programming on Python"
print(text[1])

text2 = "Hello"
print(text2[-1])

#Slicing

text_slice = text[:10] # ':10' will slice from the start to the specified number
print(text_slice)

text_slice_pairs = text[0:10:2] # '0:10:2' will slice from the start to the specified number, selecting elements evenly
print(text_slice_pairs)


