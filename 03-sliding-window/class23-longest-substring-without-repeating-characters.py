# class 23: Longest Substring Without Repeating Characters

'''
A partir de una cadena de carácteres debes encontrar la más larga subcadena de carácteres sin que se repita ningún carácter.

Ejemplo 1:

# Input
lengthOfLongestSubstring("abcabcbb")

# Output
3


Ejemplo 2:

# Input
lengthOfLongestSubstring("jdkafnlcdsalkxcmpoiuytfccv")

# Output
15

'''

def length_of_longest_substring(s: str) -> int:
    inicio = 0
    ch_to_pos = {}  # hash map de caracteres a posicion
    longest = 0
    for fin in range(len(s)):
        if s[fin] in ch_to_pos and inicio <= ch_to_pos[s[fin]]:
            inicio = fin + 1
        ch_to_pos[s[fin]] = fin
        longest = max(longest, fin - inicio + 1)
        print(f"inicio={inicio} -longest:{longest} -s[{fin}]= {s[fin]} -", end = " ")
        print(f"ch_to_pos[{s[fin]}]= {ch_to_pos[s[fin]]} -ch_to_pos: {ch_to_pos}")
    return longest


demo1 = "abcabcbb"
response = length_of_longest_substring(demo1)
print(response)

# demo2 = "jdkafnalcdslkxampoiuy"
# response = length_of_longest_substring(demo2)
# print(response)

demo3 = "bbbbb"
response = length_of_longest_substring(demo3)
print(response)