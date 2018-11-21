from model import Parcel
from validate_email import validate_email
from flask import jsonify

class Validator:
    """
    Validates the various user input before passing it to the parcellist.
    """

    def input_fields(self,owner,parcel_name,source,destination):
        """Returns the input fields or none if input is not valid"""
        if not self.pure_text(owner):
            return jsonify({"message":""})
        if not self.pure_text(source):
            return jsonify({"message":""})
        if not self.pure_text(destination):
            return jsonify({"message":""})
        if not self.normal_string(parcel_name):
            return jsonify("message":"")


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

    def status_update(self, status):
        new_status = status.strip()
        if new_status.casefold() == 'cancel':
            return new_status

    def email(self,email):
        if validate_email(email) == True:
            return email
