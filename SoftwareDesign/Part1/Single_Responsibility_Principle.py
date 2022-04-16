# SRP SINGLE RESPONSIBILITY PRINCIPLE

# In the context of the SRP we define a responsibility as a "reason for change".
# If you can think of more than one reason to change a class, it has multiple responsibilities and thus breaks the SRP.


# User service only register a user.
class User_Service:

    # Initialize user service object
    def __init__(self, _email_validator, _email_sender, _db_context):
        self._email_validator = _email_validator
        self._email_sender = _email_sender
        self._db_context = _db_context

    # Register a new user if email is valid
    def Register(self, email, password):
        # Check if mail is valid
        if self._email_validator.Validate_Email(email) == -1:
            print("Not accepted")
        print('new user')

        # Send an email throug a email service class objcet
        self._email_sender.Send_Email("Good news boyz")
        return


# An email service only validates and sends an email.
class Email_Validator:

    # Initialize a email service object
    def __init__(self, smpt_client):
        self.smpt_client = smpt_client

    # Check is email is valid
    def Validate_Email(self, email):
        return email.find('@')


class Email_Sender:
    def __init__(self):
        return
    # Send an email to the client

    def Send_Email(self, message):
        print(message)


if __name__ == '__main__':
    email_val = Email_Validator('smtp_client')
    email_sender = Email_Sender()

    user_serv = User_Service(email_val, email_sender, 'db_context')

    user_serv.Register('p@m', 123)
