class User:
    '''
    Class that outlines the behaviour and attributes of the user
    '''

    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password