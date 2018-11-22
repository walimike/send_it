from validate_email import validate_email
from flask import jsonify

class Validator:
    """
    Validates the various user input before passing it to the parcellist.
    """

    def pure_text(self,text):
        """Returns text only if the text is purely letters, no integers"""
        if self.normal_string(text):
            if text.strip().isalpha()==True:
                return text

    def normal_string(self,text):
        """test input to be string"""
        if isinstance(text, str):
            new_text = str(text).strip()
            if new_text:
                return new_text

    def email(self,email):
        if validate_email(email) == True:
            return email

    def integer(self,number):
        if isinstance(number, int):
            if number > 0:
                return number

    def password(self,password):
        if len(password)>8:
            return password
