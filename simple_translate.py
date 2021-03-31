from translate import Translator

translator = Translator(from_lang = 'English', to_lang = 'Hindi')
print("Currently the program will convert from {from_lang}----->{to_lang}\n\n")
c = input("Enter the text to translate\n\n")

result = translator.translate(c)

print("The translated text is: \n" + result)