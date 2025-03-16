from googletrans import Translator

def back_translate(text, target_lang='fr', intermediate_lang='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_lang).text
    back_translated_text = translator.translate(translated_text, dest=intermediate_lang).text
    return back_translated_text

print (back_translate(text))
