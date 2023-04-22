"""
print('Hello, Contosoville!')

town="Contosoville"

print(f'The town I am looking for is {town}')

def chant(frase):
    print(frase + frase + frase)

chant(town)
"""


def lasso_letter(letter, shift_amount):
    letter_code = ord(letter.lower())
    decode_letter_code = letter_code + shift_amount
    
    a_ascii = ord('a')
    alphabet_size =26
    

    true_letter_code=a_ascii+(((letter_code-a_ascii)+shift_amount)%alphabet_size)
    decode_letter = chr(true_letter_code)
    return decode_letter




def lasso_word(word, shift_amount):
    real_code=""
    for letter in word:
        word_code = lasso_letter(letter, shift_amount)
        real_code = real_code + word_code 
        

    return real_code

# Try to decode the word "terra"
print( "Shifting terra by 13 gives: \n" + lasso_word( "terra", 13 ) )
print(lasso_word("gdkkn",1))

print(lasso_word("Ncevy",13))
print(lasso_word("gpvsui",25))
print(lasso_word("ugflgkg",-18))
print(lasso_word("wjmmf",-1))
print(lasso_word("Ncevy",13) +' '+ lasso_word("gpvsui",25) +"\n"+lasso_word("ugflgkg",-18)+lasso_word("wjmmf",-1))
print(lasso_word("p",-2))