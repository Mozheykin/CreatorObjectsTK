def parse_srt(input_dict: dict, user_dict: dict|str, item:str, custom:str) -> str: 
    if type(user_dict) is str:
            match item:
                case 'text': return user_dict
                case _: return input_dict.get(item, custom)
    elif type(user_dict) is dict:
            value = user_dict.get(item) 
            match value:
                case None: return input_dict.get(item, custom)
                case _: return user_dict.get(item, custom)
    else:
            return custom

            
def parse_int(input_dict: dict, user_dict: dict, item:str, custom:int) -> int: 
    value = user_dict.get(item) 
    match value:
        case None: return input_dict.get(item, custom)
        case _: return user_dict.get(item, custom)

        
def parse_float(input_dict: dict, user_dict: dict, item:str, custom:float) -> float: 
    value = user_dict.get(item) 
    match value:
        case None: return input_dict.get(item, custom)
        case _: return user_dict.get(item, custom)
