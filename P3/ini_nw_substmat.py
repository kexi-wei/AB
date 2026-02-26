def nw(seq_i, seq_j, gap):
    """
    Global alignment of 2 sequences using Needleman-Wunsch.

    >>> nw('FAT', 'FAST', 2, -1, -1)
    Optimal score: 5
    ('FA-T', 'FAST')
    >>> nw('THEFASTCAT', 'THERAT', 8, -8, -4)
    Optimal score: 16
    ('THE-FASTCAT', 'THER-A-T---')
    >>> nw('THERAT', 'THEFASTCAT', 8, -8, -4)
    Optimal score: 16
    ('THE-RA-T---', 'THEF-ASTCAT')
    """
