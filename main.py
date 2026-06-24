from morse import morse_data

def text_to_morse(text):
    morse_code=[]
    
    for char in text.upper():
        if char in morse_data:
            morse_code.append(morse_data[char])
    return ''.join(morse_code)

int_text = input('Text to Morse.')

output = text_to_morse(int_text)
        
print(output)