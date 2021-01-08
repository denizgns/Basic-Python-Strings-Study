"""
Student Name: Deniz Güneş
File: complement.py
-----------------------
This file should define a console program that prompts a user for
a strand of a nucleic acid and displays the complement of that strand.
Further details and output format can be found in the PDF.
"""
import string

def build_complement(strand):
    """
    This function takes in a DNA or aN RNA strand, decides which type of
    nucleic acid it is (asks the user if not identifiable)
    returns the complementary strand, as defined by the base pair
    matchings outlined in the PDF.
    >>> build_complement("ATGCAAG")
    'TACGTTC'
    >>> build_complement("AtAg")
    'TATC'
    >>> build_complement("AGCUCAG")
    'UCGAGUC'
    """
    strand.upper()
    if ('T' in strand) or ('t' in strand):
        Strandtype = 'DNA'
    elif ('U' in strand) or ('u' in strand):
        Strandtype = 'RNA'
    elif ('T' not in strand) and ('U' not in strand):
        Strandtype = input('Please enter strand type(DNA , RNA): ').upper()



    complementary = ''
    if Strandtype == 'RNA':
        for i in range(0, len(strand)):
            if strand[i] == 'A' or strand[i] == 'a':
                complementary += 'U'
            elif strand[i] == 'U' or strand[i] == 'u':
                complementary += 'A'
            elif strand[i] == 'G' or strand[i] == 'g':
                complementary += 'C'
            elif strand[i] == 'C' or strand[i] == 'c':
                complementary += 'G'

    if Strandtype == 'DNA':
        for i in range(0, len(strand)):
            if strand[i] == 'A' or strand[i] == 'a':
                complementary += 'T'
            elif strand[i] == 'T' or strand[i] == 't':
                complementary += 'A'
            elif strand[i] == 'G' or strand[i] == 'g':
                complementary += 'C'
            elif strand[i] == 'C' or strand[i] == 'c':
                complementary += 'G'
  
    return complementary

def main():
    """
    Here we take the input strand and pass it through the function.
    And print properly
    """
    strand = input('Please enter the strand: ')
    complement = build_complement(strand)
    print('The complement of ' + strand.upper() + ' is ' + complement)

if __name__ == "__main__":
    main()