import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")

print("Vocab size", encoder.n_vocab)

text = "The cat sat on the mat"
tokens = encoder.encode(text)
print("Tokens:", tokens)
decodedText = encoder.decode(tokens)
print("Decoded text:", decodedText)
