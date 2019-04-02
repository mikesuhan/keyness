"""
This module compares two lists of tokenized texts (i.e. a corpus and a reference corpus, 
calculating the log likelihood value of every token.
"""

from math import log as ln


def type_dist(corpus):
    """Counts number of types in a corpus"""
    output = {}

    for text in corpus:
        for word_type in set(text):
            output[word_type] = output.get(word_type, 0) + 1

    return output


def freq_dist(corpus):
    """Counts number of tokens in a corpus"""
    output = {}

    for text in corpus:
        for word in text:
            output[word] = output.get(word, 0) + 1

    return output


def log_likelihood(corpus, reference_corpus, save_as=False, dist_func=freq_dist, norm_to=1000,
                   dummy_zero=.00000000000000000001, encoding='utf8', delimiter='\t'):
    """Rank orders the log likelihood values of every token in a corpus

    Arguments:
    corpus: the corpus on which log likelihood is calculated - must be an iterable of iterables (e.g. a list of tokenized texts)
    reference_corpus: what the corpus is compared against - must be an iterable of iterables (e.g. a list of tokenized texts)

    Keyword Arguments:
    save_as: saves the results as a tsv if this value is a string, returns the output as a list if it is 0, None, or False
    dist_func: the function used to count corpus and reference_corpus
    norm_to: the rate the counts are normalized to in the output
    dummy_zero: the value 0 is substituted with in order to calculate LL of words that occur in one corpus but not the other.
    setting dummy_zero to 0, None, or False will exclude words that do not occur in either corpus
    encoding: encoding used if saved as a tsv
    delimiter: delimiter used if saved as a tsv
    """
    output = []

    corpus_dist = dist_func(corpus)
    ref_corpus_dist = dist_func(reference_corpus)

    if dummy_zero:
        all_words = set(list(corpus_dist.keys()) + list(ref_corpus_dist.keys()))
    else:
        # Excludes words that do not occur in the reference corpus
        all_words = [key for key in corpus_dist.keys() if key in ref_corpus_dist.keys()]

    """
    Calculates log likelihood value (G2) of every word in the corpus.

                                    Corpus      Ref Corpus	    Total
        Frequency of word	        a	        b	            a+b
        Frequency of other words	c-a	        d-b	            c+d-a-b
        Total	                    c	        d	            c+d

    From: http://ucrel.lancs.ac.uk/llwizard.html
    """

    c = sum(corpus_dist[key] for key in corpus_dist)
    d = sum(ref_corpus_dist[key] for key in ref_corpus_dist)

    for word in all_words:
        a = corpus_dist.get(word, dummy_zero)
        b = ref_corpus_dist.get(word, dummy_zero)
        E1 = c * (a + b) / (c + d)
        E2 = d * (a + b) / (c + d)
        G2 = 2 * ((a * ln(a / E1)) + (b * ln(b / E2)))

        # Makes a row in the output list as follows:
        # word,  log likelihood value, corpus frequency, ref corpus frequency
        # round() is used on frequencies so that dummy_zero values are rounded to 0
        output_row = word, round(G2, 3), round(a), round(b)
        output.append(output_row)

    if save_as:
        tsv(sorted(output, key=lambda x: x[1], reverse=True), save_as, encoding=encoding, delimiter=delimiter)
    else:
        return sorted(output, key=lambda x: x[1], reverse=True)


def tsv(output, save_as, encoding='utf8', delimiter='\t'):
    """Saves the result of log_likelihood as a tsv."""
    tsv = '\n'.join(delimiter.join(str(item) for item in line) for line in output)
    header = 'Word', 'LL', 'CC', 'RCC',
    tsv = delimiter.join(header) + '\n' + tsv

    with open(save_as, 'w', encoding=encoding) as f:
        f.write(tsv)

    print('saved as:', save_as)
