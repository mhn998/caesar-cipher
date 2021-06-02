import re
import Corpus
import nltk

def encrypt(string:str ,key: int) -> str:
    cipher = ''
    for char in string:
        new_char = char 
        if new_char.isalpha():
            shift = 97 if char.islower() else 65
            new_char = chr((ord(char) + key - shift) % 26 + shift)
        cipher+=new_char
    return cipher

def decrypt(string:str , key:int) -> str:
    return encrypt(string , key*-1)

def crack(string:str)-> str:
    success_cracked= ""
    max_percentage = 50
    
    for key in range (0,26):
        # nltk.download('words')
        word_list = nltk.corpus.words.words()
        decrypted = decrypt(string,key)
        words = decrypted.split()
        english_count = 0
        for word in words:
            cleaned_word = re.sub(r"[^a-zA-Z]+", "", word).lower()
            if cleaned_word in word_list:
                english_count+=1
                
        english_percentage = int(english_count / len(words) * 100)
        if english_percentage > max_percentage:
            max_percentage = english_percentage
            success_cracked = decrypted
            
    return success_cracked
   

if __name__ == "__main__":
    print(encrypt('Wow a dark and stormy night.', 3))
    print(decrypt('Zrz d gdun dqg vwrupb qljkw.',3))
    print(crack('Zrz d gdun dqg vwrupb qljkw.'))