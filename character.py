character_list = []
num_characters = 3

def get_nome(character):
    return character[0]

def get_ataque(character):
    return character[1][0]

def get_defesa(character):
    return character[1][1]

def get_max_ataque():
    max_ataque = 0
    max_char = ""
    for character in character_list:
        value = get_ataque(character)
        if value > max_ataque:
            max_ataque = value
            max_char = get_nome(character)
    return max_char, max_ataque

def get_max_defesa():
    max_defesa = 0
    max_char = ""
    for character in character_list:
        value = get_defesa(character)
        if value > max_defesa:
            max_defesa = value
            max_char = get_nome(character)
    return max_char, max_defesa

def show_character_list():
    print(character_list)

def show_record_characters():
    print("Ataque", *get_max_ataque())
    print("Defesa", *get_max_defesa())
    

def input_characters(num):
    for i in range(num):
        nome = input()
        ataque = int(input())
        defesa = int(input())
        character_list.append([nome, (ataque, defesa)])

input_characters(num_characters)
show_character_list()
show_record_characters()

