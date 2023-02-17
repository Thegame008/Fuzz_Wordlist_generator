import string
import sys

if len(sys.argv) != 2:
    print("Uso: python3 generar_diccionario.py <archivo>")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, 'r') as f:
    words = f.read().split()

alphabet = string.ascii_lowercase

output_file = input("Ingrese el nombre de archivo de salida: ")

with open(output_file, 'w') as f:
    generated_words = set()
    for word in words:
        word = word.strip().lower()
        new_word = ""
        for c in word:
            if c.isalnum():
                new_word += c
        if not new_word:
            continue
        generated_words.add(new_word)
        for c in alphabet:
            generated_words.add(new_word + c)
            for d in alphabet:
                generated_words.add(new_word + c + d)
            for d in alphabet:
                generated_words.add(new_word + c + "_" + d)
                generated_words.add(new_word + c + "-" + d)
            for d in alphabet:
                generated_words.add(c + new_word + d)
                generated_words.add(c + new_word + "_" + d)
                generated_words.add(c + new_word + "-" + d)
            for d in alphabet:
                generated_words.add(new_word)
                generated_words.add(c + new_word)
                generated_words.add(c + new_word + d + "_" + c)
                generated_words.add(c + new_word + d + "-" + c)
                generated_words.add(c + new_word + "_" + d + c)
                generated_words.add(c + new_word + "-" + d + c)
                generated_words.add(new_word + "_" + c + d)
                generated_words.add(new_word + "-" + c + d)
                generated_words.add(c + "_" + new_word + d)
                generated_words.add(c + "-" + new_word + d)
                generated_words.add(c + "_" + new_word + d + "_" + c)
                generated_words.add(c + "-" + new_word + d + "-" + c)
                generated_words.add(c + "_" + new_word + d + "-" + c)
                generated_words.add(c + "-" + new_word + d + "_" + c)

    for word in generated_words:
        f.write(word + '\n')

print("Se ha generado el diccionario exitosamente en el archivo", output_file)
