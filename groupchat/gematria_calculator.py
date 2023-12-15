# filename: gematria_calculator.py

def calculate_gematria(hebrew_word):
    # Hebrew letters gematria values
    gematria_values = {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
        'י': 10, 'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40, 'נ': 50, 'ן': 50,
        'ס': 60, 'ע': 70, 'פ': 80, 'ף': 80, 'צ': 90, 'ץ': 90, 'ק': 100, 'ר': 200,
        'ש': 300, 'ת': 400
    }

    # Calculate the sum of gematria values for each letter in the word
    gematria_sum = sum(gematria_values.get(letter, 0) for letter in hebrew_word)
    return gematria_sum

# Test function
def test_calculate_gematria():
    word = 'יהוה'
    expected_gematria = 26
    calculated_gematria = calculate_gematria(word)
    
    assert calculated_gematria == expected_gematria, f"Test failed: Expected {expected_gematria}, got {calculated_gematria}"
    print("Test passed! The gematria of יהוה is 26.")

# Test the function
word = 'יהוה'  # The Hebrew word to calculate gematria for
result = calculate_gematria(word)
print(f"The gematria of the word {word} is: {result}")
  
# Run the test
test_calculate_gematria()