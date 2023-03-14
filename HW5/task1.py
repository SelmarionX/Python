# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'ываабв лповап абвцуквАБВ алоабвабв ываываыв'
text = list(filter(lambda el: 'абв' not in el.lower(), text.split()))
print(' '.join(text))
