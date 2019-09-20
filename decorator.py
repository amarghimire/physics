def my_doc(any_function):
    def test():
        return f'{any_function.__doc__}'
    return test
@my_doc
def user():
    '''this is me user'''
    return "all user data"

print(user())