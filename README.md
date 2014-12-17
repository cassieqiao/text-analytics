Text Analytics
==============

Northwestern MSIA Text Analytics

Assignment 1 - Regular Expressions

In this assignment you will write a program that will take as input one plain text file and will print as
output every sentence of the input file that contains a time point, one sentence per line.
Finding time points is a frequent task in text analytics. Regular expressions are well suited for this task
and that is what we will use for this assignment.
A time point could be an absolute date (e.g. “October 31st, 2013” or “10/31/13”), an absolute time (e.g.
“14:00 PST”) or even a relative time (e.g. “the day my mother was born”). However the sentence
“Many days I eat toast for breakfast.” does not contain a time point.

Assignment 2 - Lucene intro and edit distance

1. Introduction to lucene 
Write a program that
• Creates a lucene index
• Breaks classbios.txt into one chunk per person. (You could use regular expressions for this).
• Indexes each chunk into your index as a separate document. Tell us in your submission which fields
you chose to include and how you configured then.
• Asks the user to type queries and prints their results. For the result print the actual phrase that
matched your query with some context (a few words before and after the actual phrase that
matched the query). In your submission include three “creative queries” exploring the capabilities
of the query parser and prints their output.

2. Edit distance. 
Compute the edit distance between Shakespeare and the following three common misspellings of the
word: Shaxberd, Shexpere, Shackspere showing in a diagram the intermediate costs and the optimal
matching path(s). Assume that the cost of insertion/deletion is 2, and the cost of substitution is 3.

Assignment 3 - Term Document Matrix and introduction to SNLP library

1. Term Document Matrix ?40pts
Write a program that uses the classbios information retrieval index that you produced in your previous
assignment to:
• Produces a term-document matrix (T) based on raw term-frequencies. As your answer tell us what
the 10 terms are that have the largest entries in your matrix T.
• Produce a TF-IDF (1+log(Tf))*log(N/Df) normalized document matrix (M). As your answer tell us
what the 10 terms are that have the largest entries in your matrix T.

2. Naive document summarization 
A naïve, yet often, and surprisingly powerful method, used method to summarize a document is to
take the k terms with highest frequency for that document from the Term document matrix.
• Use T and M from the previous exercise to summarize each class bio. As your answer, you do not
need to give us the summary for each document. Instead, tell us whether you think T or M is a better
matrix to use for document summarization and what value of k you think works best for this
particular type of document. Illustrate your answer with a few actual examples.

3. Introduction to the Stanford Natural Language Processing tools. - 30pts
• Install the Core NLP from: http://nlp.stanford.edu/software/corenlp.shtml
• Use the CoreNLP to extract parts of speech for the classbios.txt documents. Turn in the output
for the first sentence.

Assignment 4 - Web scrapping. Classification

In this homework we are going to analyze a different dataset to learn how to work with html documents.
This dataset consists of wikipedia entries about cities and countries in the world.
You will turn in a single report.pdf document.

1. (40%) Index the wikipedia text for the capital cities in the world and their countries. This link
contains the links to each of those entries:
http://en.wikipedia.org/wiki/List_of_countries_and_capitals_with_currency_and_language
. Create an index using the text indexing tool of your choice (e.g. Lucene).
. Extract the text corresponding to the wikipedia entries of each of the capital cities and each
country and add a document to your index for each city you extract. In your document you
should have five fields: city_name, country_name, continent, city_text and country text.
You may use any web scrapping library of your choice to extract the text. For example,
lxml, BeautifulSoup and Scrapy are some Python options.
As in any real world analytics, especially text analytics there are some special cases. In this case
there are cases where the one-to-one relationship between country and capital breaks down. Make
a reasonable choice about how to handle these cases and document it in the first section of your
report. How many capital cities did you include? How many countries?

2. (30%) Using your index find all the cities whose text contains
• (10%) the words: Greek and Roman but not the word Persian. In Lucene, use BooleanQuery.
• (10%) The word Shakespeare (even if it is misspelled!). In Lucene, use a FuzzyQuery. FYI: It
is implemented using edit distance between words, as seen in class.
(10%) The words “located below sea level” near each other. In Lucene, use a PhraseQuery
with a slop factor of 10. It uses edit distance between phrases (the insertion/deletion
substitution operators are applied to terms in the positional index, not to letters).

3. (30%) Build a Naive Bayes Classifier that will identify the continent where a city is using the
description of the city. Choose either multinomial or Bernoulli.
1. Extract all terms for all cities from your index (c.f.
http://stackoverflow.com/questions/8910008/how-can-i-get-the-list-of-unique-terms-from-aspecific-
field-in-lucene). For each term compute their mutual information with respect to the
continent where a city lays. Use Laplacian smoothing for your counts.
2. (5%) Write in a table the 30 most informative terms for each continent.
3. (5%) Pick the unique terms from the table above. What are they? How many terms are there in
total?
4. Use them to build a naïve Bayes classifier using any data mining tool of your choice. If you
want to integrate it with your code in Java, you can use: http://www.cs.waikato.ac.nz/ml/weka/ .
5. (10%) Classify the capital cities (training set) and build a confusion matrix.
6. (10%) Find the English wikipedia entry of your favorite city that is not a country capital and
classify it. What is its feature vector? What is the probability that your classifier assigns to each
continent?

Assignment 5 - Stanford NLP exploration

1. Read about the various tools that are available and play with their demos to get familiar with them. You
do not need to turn anything for this part.
2. Choose the three tools that you think could be more useful to you in a future text analytics project and
run then on the file wsj_0063.txt. This text originally appeared in the Wall Street Journal in 1989 and is
now part of the “Penn Treebank Project” which contains a corpus of documents often used to train and
evaluate Natural Language Processing algorithms. Include the full output of running your choice tools in
your submission.
3. For each of your three choice tools include your thoughts on how you might use them in your
professional career.

Final project - Dialog analysis

In this assignment we are going to analyze dialog text. Modern dialog text often occurs online in forums or
chats, or on transcripts of phone conversations; but for this exercise we are going to analyze a theater play,
because the sentences are typically longer and richer, and the text is clearly annotated with the speakers and
settings. Movie scripts with rich dialgo or multiple episode tv series would also work.
Assignment: Pick your favorite theater play for which you can get the text and analyze it using
methodologies of your choice as seen during the course. Turn in a report. Your report should discuss
your methods and your findings and should contain visually appealing representations of your results.
You can work in groups of up to three people. Please, submit a single report for the whole group.
Grading. You will be graded solely on your report. I will consider your choice of methods: What do you do and
how do you do it. Do you do it correctly? How rich is your data and how interesting are the conclusions and
thoughts you derive from it, as well the appeal of the visualizations you choose to present. I will take into
account your effort as well as the overall quality of the write up. A laundry list of facts without any
explanations or conclusions does not constitute a very good report. A lot of speculation with no data to back it
up is not very good either.

These are some ideas for things that you might want to analyze to get you started in your thinking. Feel free to
extend, or deviate as you please. What makes most sense will depend on your choice of play.
- What are the temporal references? If your play contains actual dates (like in a diary) then relative times (like
“last Thursday”) can be converted to absolute references (the Stanford NLP can do this). Can you build some
form of timeline?
- Topics. What are the topics of the play? You could make a break down by character. Do these topics evolve
over time? (E.g. by act). LDA would be quite suitable for this.
- Clustering. You could for example cluster the characters based on the language they use and topics they
discuss. Using LSA and your favorite clustering algorithm might be appropriate.
- What are the Named Entities (People, Places, Companies) that appear in your play?
- Who talks (spends time) with whom? Does it change over time? Which fraction of the talk does each speaker
contribute?
- Who talks about what or whom? What is the sentiment of the speaker about this entity?. You could use
sentiwordnet, or even better, the SNLP library. Notice that you will probably want to do coreference resolution
(to identify what pronouns matches what noun) when identifying who talks about what or whom. In dialogs,
participants agree about the antecedents of pronouns, so you may want to process consecutive utterances from
the various dialog participants as a single unit of text for the purpose of coreference resolution.
- Sentiment. What is the mood of each speaker? (E.g. the average sentiment of the words they utter?) Does it
change over time? Does it depend on who they are talking to or whom or what they are talking about?
- Can you build a classifier that will predict the speaker of an utterance? Would it help to also know the act of
the play? The other speakers? What features do you use?



