
import math
from textblob import TextBlob as tb
#import nltk
#from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize

"""
text blob helps in Part-of-speech Tagging,Noun Phrase Extraction,Sentiment Analysis, Tokenization,
 Words Inflection and Lemmatization
 """

def tf(word, blob): # term frequency
    return blob.words.count(word) / len(blob.words)

def sublinear_tf (word,blob):
    return 1 + math.log(blob.words.count(word))

def n_containing(word, bloblist): #number of documents contining that word
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):  #finding inverse document frequncy 
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))# no division by 0 error 

def tfidf(word, blob, bloblist):   #find tf-idf
    
    return sublinear_tf(word, blob) * idf(word, bloblist)

document1 = tb("""Python is a 2000 made-for-TV horror movie directed by Richard
Clabaugh. The film features several cult favorite actors, including William
Zabka of The Karate Kid fame, Wil Wheaton, Casper Van Dien, Jenny McCarthy,
Keith Coogan, Robert Englund (best known for his role as Freddy Krueger in the
A Nightmare on Elm Street series of films), Dana Barron, David Bowe, and Sean
Whalen. The film concerns a genetically engineered snake, a python, that
escapes and unleashes itself on a small town. It includes the classic final
girl scenario evident in films like Friday the 13th. It was filmed in Los Angeles,
 California and Malibu, California. Python was followed by two sequels: Python
 II (2002) and Boa vs. Python (2004), both also made-for-TV films.""")

document2 = tb(""" Python, from the Greek word (πύθων/πύθωνας), is a genus of
nonvenomous pythons found in Africa and Asia. Currently, 7 species are
recognised. A member of this genus, P.reticulatus, is among the longest
snakes known.""")

document3 = tb("""The Colt Python is a .357 Magnum caliber revolver formerly
manufactured by Colt's Manufacturing Company of Hartford, Connecticut.
It is sometimes referred to as a "Combat Magnum". It was first introduced
in 1955, the same year as Smith & Wesson's M29 .44 Magnum. The now discontinued
Colt Python targeted the premium revolver market segment. Some firearm
collectors and writers such as Jeff Cooper, Ian V. Hogg, Chuck Hawks, Leroy
Thompson, Renee Smeets and Martin Dougherty have described the Python as the
finest production revolver ever made.""")



#remove stop words
stop_words = set(stopwords.words('english')) 
my1 = [word for word in document1.words if word not in stopwords.words('english')]
text1 = ' '.join(my1)
document1 = tb(text1)

my2 = [word for word in document2.words if word not in stopwords.words('english')]
text2 = ' '.join(my2)
document2 = tb(text2)

my3 = [word for word in document3.words if word not in stopwords.words('english')]
text3 = ' '.join(my3)
document3 = tb(text3)



bloblist = [document1, document2, document3]
for i, blob in enumerate(bloblist):
    print("Top words in document "+ str(i+1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words:
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))
    print(' ')
    
for x , blob in enumerate(bloblist):
    print("Nouns in document " + str(i+1)+" : " + str(blob.noun_phrases)) 
    print('')
    
    
def clean_document(document):
    """Cleans document by removing unnecessary punctuation. It also removes
    any extra periods and merges acronyms to prevent the tokenizer from
    splitting a false sentence
    """
    # Remove all characters outside of Alpha Numeric
    # and some punctuation
    document = re.sub('[^A-Za-z .-]+', ' ', document)
    document = document.replace('-', '')
    document = document.replace('...', '')
    document = document.replace('Mr.', 'Mr').replace('Mrs.', 'Mrs')

    # Remove Ancronymns M.I.T. -> MIT
    # to help with sentence tokenizing
    document = merge_acronyms(document)

    # Remove extra whitespace
    document = ' '.join(document.split())
    return document


    
