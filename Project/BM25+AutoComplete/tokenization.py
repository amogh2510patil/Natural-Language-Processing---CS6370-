#from util import *

# Add your import statements here

from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize import TreebankWordTokenizer






class Tokenization():

  """
  Tokenization using a Naive Approach

  Parameters
  ----------
  arg1 : list
    A list of strings where each string is a single sentence

  Returns
  -------
  list
    A list of lists where each sub-list is a sequence of tokens
  """

  def naive(self, text):
    tokenizedText = []

		#Fill in code here
    tk = WhitespaceTokenizer()
    for sentence in text:
      token = tk.tokenize(sentence)
      tokenizedText.append(token)
    return tokenizedText


  """
  Tokenization using the Penn Tree Bank Tokenizer

  Parameters
  ----------
  arg1 : list
    A list of strings where each string is a single sentence

  Returns
  -------
  list
    A list of lists where each sub-list is a sequence of tokens
  """
	  


  def pennTreeBank(self, text):
    tokenizedText = []

    #Fill in code here
    PTB_tk = TreebankWordTokenizer()
    for sentence in text:
      token = PTB_tk.tokenize(sentence)
      tokenizedText.append(token)
    return tokenizedText
















