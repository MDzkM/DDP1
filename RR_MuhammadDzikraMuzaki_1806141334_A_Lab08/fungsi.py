## Templates of the functions module to be imported by main module.

def check_palindrom(word) :
    """ This is a method to check whether a string is a palindrome.
    This method receives a str as its parameter.
    This method checks its first and last character RECURSIVELY.
    This method returns boolean value whether is is a palindrome or not. """

    ## Base case
    if word == "":
        return True

    ## Mengecek huruf pertama dan terakhir apakah sama
    elif word[0] == word[-1]:
        ## Memanggil fungsi check_palindrom kembali dengan sisa string
        # selain yang pertama dan terakhir
        return check_palindrom(word[1:-1])

    ## Mengembalikan nilai false apabila tidak sama
    return False
 
 
def reverse_string(word):
    """ This is a method to reverse a string RECURSIVELY.
    This method receives a str as its parameter.
    This method returns a reversed str of its given parameter. """

    ## Base case
    if len(word) == 1 :
        return word[0]

    ## Membalik string secara rekursif
    # dengan menaruh char pertama di belakang dan
    # char selanjutnya di depannya
    else:
        return reverse_string(word[1:]) + word[0]
 
 
def make_palindrom(word):
    """ This is a method to create a palindrome from a non palindrome str.
    This method receives a str as its parameter.
    This method returns the shortest palindrome that can be created from the parameter. """
    reverse_word = reverse_string(word)
    if(word == reverse_word):
        return word
 
    while(reverse_word[0] == word[-1]):
        reverse_word = reverse_word[1:]
 
    return word + reverse_word
 
