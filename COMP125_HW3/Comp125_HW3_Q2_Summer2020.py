"""
Student Name: Deniz Güneş
File: similarity.py
------------------------
This file should implement a console program that prompts users
for a DNA or an RNA strand that they want to search through and a target strand
that they want to search for. The program then outputs the closest match
to the target strand, as defined by the similarity metric presented in the
PDF.If the types of nucleic acids are different which means one of them contains T
and the other contains U, the program must ask for another "sequence to match!".
"""

def search_sequence(sequence_to_match, subsequence):
    """
    This function takes in two sequences, and calculates
    the number of spots at which the two sequences have the same
    base pairs.
    >>> search_sequence("GAUC", "AAUC")
    3
    >>> search_sequence("AGC", "TAG")
    0
    """
    match_count = 0
    for i in range(0, len(subsequence)):
        for j in range(i, len(sequence_to_match)):
            if subsequence[i] == sequence_to_match[j]:
                match_count += 1
    return match_count


def find_best_substrand(sequence_to_match, strand_to_search):
    """
    This function takes in two strands, one to search through and one
    for which you are trying to find a match. The function returns the closest
    match to the target sequence in the search sequence.
    >>> find_best_substrand("TCATA","ATGCCTGATA")
    'TGATA'
    >>> find_best_substrand("", "ATGCCTGATA")
    ''
    """
    sequence_to_match.upper()
    strand_to_search.upper()
    #first lets check if the strands are properly given
    if ("T" in sequence_to_match and "U" in strand_to_search) or \
            ("U" in sequence_to_match and "T" in strand_to_search):
            print("The nucleic acids types must be same!")


    max = 0
    #We need to check the strand_to_search in blocks
    #The best block's starting point must be stored to be able form the best mathcing string
    for i in range(0, len(strand_to_search)):
        current = search_sequence(sequence_to_match, strand_to_search[i: i + len(sequence_to_match)])
        if current > max:
            max = current
            start = i

    best = strand_to_search[start: start + len(sequence_to_match)]
    return best


def main():
    """
    Replace this comment with a more descriptive one.
    Don't forget to delete the pass statement below.
    """
    a = search_sequence("AGC", "TAG")
    print(a)
    best = find_best_substrand("TCATA", "ATGCCTGATA")
    print('The best match is ' + best)


if __name__ == "__main__":
    main()
