def sw(seq_i, seq_j, gap):
    """
    Local alignment of 2 sequences using Smith-Waterman algorithm
    with BLOSUM62 substitution matrix and a specified gap penalty.

    >>> sw('THEFASTCAT', 'THERAT', -4)
    Optimal score: 20.0
    ('THEFAS', 'THERAT')
    >>> sw('FAT', 'THEFASTCAT', -4)
    Optimal score: 11.0
    ('FAT', 'FAS')
    >>> sw('THECATISFAT', 'AFASTCAT', -4)
    Optimal score: 18.0
    ('CAT', 'CAT')
    """
