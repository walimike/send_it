from validate_email import validate_email
from flask import jsonify

class Validator:
    """
    Validates the various user input before passing it to the parcellist.
    """

    def input_fields(self,parcel_name,source,destination,present_location,price):
        """Returns the input fields or none if input is not valid"""
        if not self.pure_text(parcel_name):
            return jsonify({"message":"an error occured in Parcel Name input"})
        if not self.pure_text(source):
            return jsonify({"message":"an error occured in Source input"})
        if not self.pure_text(destination):
            return jsonify({"message":"an error occured in Destination input"})
        if not self.normal_string(present_location):
            return jsonify({"message":"an error occured in Precent Location input"})
        if not self.integer(price):
            return jsonify({"message":"an error occured in Price input"})


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

    def integer(self,number):
        if isinstance(number, int):
            if number > 0:
                return number
