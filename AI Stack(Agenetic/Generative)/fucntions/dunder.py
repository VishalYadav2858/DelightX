def chai_status(cups):
    '''
    Docstring for chai_status
    
    :param cups: Description
    '''
    
    if cups ==0:
        return  "Sorry no chai"
    # print(cups)
    return "serving ur chai"
    
print(chai_status.__doc__)
print(chai_status.__name__)