def sentence_maker(sentence):
    capetalized = sentence.capitalize()
    if capetalized.startswith(('How', 'What', 'Why', 'When', 'Where', 'Who')):
        return f"{capetalized}?"
    else:
        return f"{capetalized}."


input_data = []
while True:
    input_str = input("Enter something (type '/end' to quit): ")
    if input_str == '/end':
        break
    else:
        input_data.append(sentence_maker(input_str))

print(" ".join(input_data))