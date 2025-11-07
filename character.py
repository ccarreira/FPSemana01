#test
# #leia o nome (string) e os vaores de ataque e defesa (interiros) de 3 personagens
"""
Guarde os dados num array bidimensional, onde cada linha contenha um nome e um tuplo
(ataque, defesa)

Mostre a estrutura final e indique o valor mais elevado de ataque e defesa, com o respectivo NotImplemented

Raul
5
15
Maria
15
5
Carlos
10
10


Ataque Maria 15
Defesa Raul 15

"""

character_list = [['Raul', (5,15)], ['Maria', (15,5)], ['Carlos', (10,10)]]

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

def show_characters_desc():
    for character in character_list:
        print(get_nome(character))
        print(get_ataque(character))
        print(get_defesa(character))

def show_character_list():
    print(character_list)

def show_record_characters():
    nome, valor = get_max_ataque()
    print("Ataque", nome, valor)
    nome, valor = get_max_defesa()
    print("Defesa", nome, valor)


show_characters_desc() 
show_character_list()
show_record_characters()

