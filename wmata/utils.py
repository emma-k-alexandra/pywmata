def to_snake_case(string: str) -> str:
    result = [string[0].lower()] 

    for character in string[1:]: 
        if character in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'): 
            result.append('_') 
            result.append(character.lower()) 

        else: 
            result.append(character) 
      
    return ''.join(result) 