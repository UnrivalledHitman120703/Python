# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# Name = Indrajeet Mondal; Date = 7th October 2023
# SourceCode

user_info = {
    'username': 'UnrivalledHitman',
    # Changing this will either run or not run the message_friends function.
    'is_authenticated': True
}


def authentication_required(func):
    def wrapper(*args, **kwargs):
        if args[0].get('is_authenticated'):
            result = func(*args, **kwargs)
            return result
        else:
            return print('Message would not be sent. Need to be authenticated')

    return wrapper


@authentication_required
def message_friends(user):
    print('Message has been sent')


message_friends(user_info)
