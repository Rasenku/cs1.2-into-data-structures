text = "one fish two fish red fish blue fish"

def read_file():
	f = open(words.txt, "r")
	words = f.read()
	f.close()
	return words

def histogram():
	histograms = {}
	words = text.split()
	for word in words:
		count = text.count(word)
		histograms.update( {word: count})
	return histograms


# Returns the number of unique tokens
def unique_words(histogram):
	return len(histogram)

# Returns the occurences in histogram
def frequency(word, histogram):
	return histogram[word]

test_histogram = histogram()

print(frequency("red", test_histogram))

print(test_histogram)
