import nltk
from nltk.corpus import words, names
import ssl
# https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

word_list = words.words()
namelist = names.words()


#Source: Reference TH code for comparison 