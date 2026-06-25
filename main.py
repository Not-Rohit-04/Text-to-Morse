from morse import morse_data
from interface import title,initial_txt



is_on = True

while is_on:
    
    print(title)
    print(initial_txt)
    
    def text_to_morse(text):
        morse_code=[]
        
        for char in text.upper():
            if char in morse_data:
                morse_code.append(morse_data[char])
        return ' '.join(morse_code)

    int_text = input('Text to Morse.')
    if len(int_text) == 0:
        print('Enter a text to convert')
    elif int_text == 'exit':
        is_on = False
    else: 
        output = text_to_morse(int_text)
        print(f'Morse-Code_Text:-{output}')
