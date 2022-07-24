INSTRUCTIONS TO RUN:

(1) BM_25 CODE:

Libraries needed: nltk

Step 1: Go to the folder named BM25+AutoComplete.
Step 2: Run "main.py" file.

For Hypothesis Testing and Comparative Analysis Plots:
Run "HypothesisTesting.py" file.

(2) QUERY AUTO COMPLETE:

Libraries needed: nltk, pyqt

Step 1: Go to the folder named BM25+AutoComplete.
Step 2: Run "AutoCompleter.py" file.
	A Widget window will open up.
	Enter query in the input box with help from autocomplete suggestion.
	After entering query, close the Widget window.
	Your query would have been stored in "userquery.txt"
Step 3: Run "main.py" file with Handle Custom Query Option selected.

(3) LSA CODE:

Libraries needed: nltk

Step 1: Go to the folder named LSA.
Step 2: Run "main.py" file.

For Hypothesis Testing and Comparative Analysis Plots:
Run "HypothesisTesting.py" file.

(4) Spell check CODE:

Libraries needed: textblob, pyspellckecker

Step 1: Go to conda prompt and install textblob, pyspellckecker by using the command "conda install textblob" and "conda install pyspellckecker" .
Step 2: Go to the folder named LSA.
Step 3: Uncomment the code of spell check from "main.py" file in  the method "preprocessQueries" and "preprocessDocs"
Step 4: Run "main.py" file.

