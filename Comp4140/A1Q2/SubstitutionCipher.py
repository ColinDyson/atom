NUM_LETTERS = 26
ENGLISH_FREQS = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.015, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.024, 0.002, 0.020, 0.001]
a = ord('a')
cipherText = "jgrmqoyghmvbjwrwqfpwhgffdqgfpfzrkbeebjizqqocibzklfafgqvfzfwweogwopfgfhwolphlrlolfdmfgqwblwbwqolkfwbylblylfsfljgrmqbolwjvfpfwqvhqwffpqoqvfpqocfpogfwfjigfqvhlhlroqvfgwjvfpfolfhgqvqvfileogqilhqfqgiqvvosfafgbwqvhqwijvwjvfpfwhgfiwihzzrqgbabhzqocgfhx"
newText = cipherText
letterCounts = [0] * NUM_LETTERS
keyMap = ["a"] * NUM_LETTERS


#count letters in cipherText
for i in range (NUM_LETTERS):
    letterCounts[i] = cipherText.count(chr(i + a))

#
for i in range(NUM_LETTERS):
        mostCommonCipherChar = chr(letterCounts.index(max(letterCounts)) + a)
        mostCommonEnglishChar = chr(ENGLISH_FREQS.index(max(ENGLISH_FREQS)) + a)
        # print("cipher char:", mostCommonCipherChar)
        # print("english char:", mostCommonEnglishChar)

        if mostCommonCipherChar != 0 and mostCommonEnglishChar != 0:
            keyMap[ord(mostCommonEnglishChar) - a] = mostCommonCipherChar
            letterCounts[ord(mostCommonCipherChar) - a] = 0
            ENGLISH_FREQS[ord(mostCommonEnglishChar) - a] = 0

#Apply keyMap
print(keyMap)
for i in range(len(keyMap)):
    print("Replacing", chr(i+a), "with", keyMap[i])
    newText.replace(chr(i + a), keyMap[i])

print(newText)