


"""login handling functions"""
def loginValidator(email, password):
    return True




"""register handling functions"""
def registerValidator(email, name, surname, password):
    isValidEmail=False
    isValidName=False
    isValidSurname=False
    isValidPassword=False

    if len(name)>=3:
        isValidName=True



    return (isValidName&isValidSurname&isValidEmail&isValidPassword)

def registerInvalidMessage():
    return("invalid")
