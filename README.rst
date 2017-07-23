The log_likelihood() function compares the frequencies of tokens or ngrams in a corpus and reference corpus,
rank ordering the output by the log likelihood values of the corpus.

The corpus and reference corpus must be iterables or tokenized texts. For example, a list of lists:



log_likelihood() will return a rank ordered list with the following data in each item:
    - the item
    - its log likelihood value
    - its frequency in the corpus
    - its rate in the corpus (set using the norm_to keyword argument)
    - its frequency in the reference corpus
    - its rate in the reference corpus

Example:

>>> from keyness import keyness
>>> corpus = [['here', 'is', 'an', 'example', 'of', 'the', 'first', 'text', 'in', 'the', 'corpus'], ['here', 'is', 'an', 'example', 'of', 'the', 'second', 'text', 'in', 'the', 'corpus'], ['here', 'is', 'an', 'example', 'of', 'the', 'third', 'text', 'in', 'the', 'corpus']]
>>> reference_corpus = [['here', 'is', 'an', 'example', 'of', 'the', 'first', 'text', 'in', 'the', 'reference', 'corpus'], ['here', 'is', 'an', 'example', 'of', 'the', 'second', 'text', 'in', 'the', 'reference', 'corpus'], ['here', 'is', 'an', 'example', 'of', 'the', 'third', 'text', 'in', 'the', 'reference', 'corpus']]
>>> keyness.log_likelihood(corpus, reference_corpus)
[('reference', 3.88, 0, 0.0, 3, 90.909), ('example', 0.014, 3, 100.0, 3, 90.909), ('an', 0.014, 3, 100.0, 3, 90.909), ('is', 0.014, 3, 100.0, 3, 90.909), ('corpus', 0.014, 3, 100.0, 3, 90.909), ('the', 0.014, 3, 100.0, 3, 90.909), ('text', 0.014, 3, 100.0, 3, 90.909), ('here', 0.014, 3, 100.0, 3, 90.909), ('of', 0.014, 3, 100.0, 3, 90.909), ('in', 0.014, 3, 100.0, 3, 90.909), ('third', 0.005, 1, 33.333, 1, 30.303), ('first', 0.005, 1, 33.333, 1, 30.303), ('second', 0.005, 1, 33.333, 1, 30.303)]
