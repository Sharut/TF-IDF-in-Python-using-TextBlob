# TF-IDF-in-Python-using-TextBlob
Implemented TERM FREQUENCY - INVERSE TERM FREQUENCY in python using TextBlob and tested it over Small documents. 

It is a very important technique to find important key words from a text file. It is commonly used in data mining for "information summarization or Retrieval

# Term Weighing Systems
Weights can be:

1. binary: 1 if term is present and 0 if not
2. term frequency (TF): frequency of each word in a document
3. document frequency (DF): words that are used more in the collections have more weight
4. TF-IDF: combination of sublinear TF and inverse document frequency

# Term Frequency (TF)
local frequency of a word in the document i.e. the word is weighed by how many times it occurs in the document

# Sublinear Term Frequency: 
sometimes a word is used too often so we want to reduce its influence compared to other less frequently used words for that we can use some sublinear function, e.g. logtf(w,d) 

# Document Frequency (DF)
Global frequency of a word in the document collection . It is the number of documents that contain the word.

# Inverse Document Frequency (IDF)
More often we're interested in words that are rare across the document collections. They tend to be domain specific and are usually more relevant for retrieving this document . So we should give them more weight than to high-frequency words .

# TF-IDF Scheme
When weighting we want to get:
1. domain specific words
2. words that are frequent in the document
3. this can be done by combining TF and IDF:
4. use sub-linear TF to avoid the dominating effect of words that occur very frequently
5. use IDF to reduce weights of terms that occur more frequently to ensure that document matching is done with more discriminative words. As the result, terms appearing too rarely or too frequently are ranked low


so, mathematically
                              tf-idf (w,d∣D) = (1 + log (tf(w,d))) ⋅ log ( |D| / df(w,D))





