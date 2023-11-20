with open('./movies_character.csv', 'r', encoding='utf-8', newline='') as f:
    first_line = f.readline().strip()

table_name = first_line
