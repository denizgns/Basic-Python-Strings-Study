"""
#Student Name: Deniz Güneş
This program is a translates a text given by a user into
text in Ubbi Dubbi format.
"""
#Constant variables
VOWELS = "aeiou"
ENDWORD = 'ay'

def translate_to_ubbidubbi(user_sentence):
    """
    This function tranlates a user entered sentence imto
    Ubbi Dubbi by adding ub before the first vowel.
    #Write additional doctest for sentences:
    1- "I am able to code" ,
    2- "pig latin is fun"

    #Your doctests starts here
    >>> translate_to_ubbidubbi('I am able to code')
    'ubi ubam ubable tubo cubode'
    >>> translate_to_ubbidubbi('pig latin is fun')
    'pubig lubatin ubis fubun'
    #Your doctest ends here

    >>> translate_to_ubbidubbi('I love python')
    'ubi lubove pythubon'
    >>> translate_to_ubbidubbi('I am able to speak ubbi dubbi')
    'ubi ubam ubable tubo spubeak ububbi dububbi'
    """
    user_sentence.lower()
    #first split the sentence into words using split
    words = user_sentence.split()
    output = []
    #for each word we are looking for the first vowel to add 'ub'
    #if the world starts with a vowel we must handle it differently to prevent errors
    #other than the first vowel, we must not add ubs in front of vowels so we check it too
    for word in words:
        if word[0] in VOWELS:
            output.append('ub' + word)
        else:
            vowel_count = 0
            for i in range(1, len(word)-1):
                if vowel_count == 0:
                    if word[i] in VOWELS:
                        output.append(word[:i] + 'ub' + word[i:])
                        vowel_count = 1


    out_str = ''

    for out in output:
        out_str += out + ' '
    #formed an output string to return so that we can use print easily in the main
    return out_str

def main():
    print('This program translates a text to Ubbi Dubbi')
    user_sentence = input('Enter a text to translate: ')
    print(translate_to_ubbidubbi(user_sentence))

if __name__ == '__main__':
    main()