

with open('input.txt', 'r') as file:
    content = file.read()
    str_list = list(content)
    hash_map = {}
    
    for i, str in enumerate(str_list):
        hash_map[str] = hash_map.get(str, 0) + 1
        if i > 13:
            hash_map[str_list[i-14]] -= 1
            if hash_map[str_list[i-14]] == 0:
                del hash_map[str_list[i-14]]
        if len(hash_map.keys()) == 14:
            print(i + 1)
            break
        