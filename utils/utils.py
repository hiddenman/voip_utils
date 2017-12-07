# Utils

def cleanup_code(code=''):
    """Return stripped code string"""
    code = code.strip().replace(' ', '').replace('\t', '')
    return code

# FIXME: do i need this?
def cleanup_volume(volume=''):
    """Return stripped volume string"""
    volume = cleanup_code(volume)
    return volume

def sort_code(code='', with_array=False):
    """Return sorted code string and sorted code array (if with_array is True). Using comma as seperator"""
    code_array = code.split(',')
    code_array_len = len(code_array)
    if (code_array_len > 1):
        code_array.sort()        
        code = ''
        for i in range(code_array_len):
            if (code_array[i] != ''):
                code += code_array[i]
                if (i < (code_array_len - 1)):
                    code += ','
    if (with_array):
        return code,code_array
    else:
        return code

def cleanup_price(price=''):
    """Return stripped price with replaced comma by point, removed spaces and tabs"""
    # FIXME: get something like :space:
    price = price.strip().replace(' ', '').replace('\t', '').replace(',', '.')
    return price
    
    
