The log_likelihood() function compares the frequencies of tokens or ngrams in a corpus and reference corpus,
rank ordering the output by the log likelihood values of the corpus.

The corpus and reference corpus must be iterables of tokenized texts. For example, a list of lists:



log_likelihood() will return a rank ordered list with the following data in each item:
    - the item
    - its log likelihood value
    - its frequency in the corpus
    - its frequency in the reference corpus

Example:

>>> from keyness import log_likelihood
>>> corpus = [['here', 'is', 'an', 'example', 'of', 'the', 'first', 'text', 'in', 'the', 'corpus'], ['here', 'is', 'an', 'example', 'of', 'the', 'second', 'text', 'in', 'the', 'corpus'], ['here', 'is', 'an', 'example', 'of', 'the', 'third', 'text', 'in', 'the', 'corpus']]
>>> reference_corpus = [['here', 'is', 'an', 'example', 'of', 'the', 'first', 'text', 'in', 'the', 'reference', 'corpus'], ['here', 'is', 'an', 'example', 'of', 'the', 'second', 'text', 'in', 'the', 'reference', 'corpus'], ['here', 'is', 'an', 'example', 'of', 'the', 'third', 'text', 'in', 'the', 'reference', 'corpus']]
>>> log_likelihood(corpus, reference_corpus)
[('reference', 3.88, 0, 3), ('is', 0.014, 3, 3), ('text', 0.014, 3, 3), ('the', 0.014, 3, 3), ('here', 0.014, 3, 3), ('example', 0.014, 3, 3), ('an', 0.014, 3, 3), ('corpus', 0.014, 3, 3), ('of', 0.014, 3, 3), ('in', 0.014, 3, 3), ('third', 0.005, 1, 1), ('first', 0.005, 1, 1), ('second', 0.005, 1, 1)]
