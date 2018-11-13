from api.models.models import Parcel

class Validator:
    """
    Validates the various user input before passing it to the parcellist.
    """

    def input_fields(self,owner,parcel_name,source,destination):
        """Returns the input fields or none if input is not valid"""
        if self.pure_text(owner) and self.pure_text(source) and\
        self.pure_text(destination) and self.normal_string(parcel_name):
            return [owner,parcel_name,source,destination]
        return

    def pure_text(self,text):
        """Returns text only if the text is purely letters, no integers"""
        if self.normal_string(text):
            if text.strip().isalpha()==True:
                return text

    def normal_string(self,text):
        """test input to be string"""
        if isinstance(text, str):
            """check if string is empty using strip function"""
            new_text = str(text).strip()
            if not new_text:
                """if string empty return false"""
                return
            return new_text
        else:
            return

    def order_id(self,number):
        """test input to be int"""
        if isinstance(number, int):
            """check if int is greater than 0"""
            if number > 0:
                return number
            else:
                return
        else:
            return

    def status_update(self,status):
        if status.casefold() == 'cancel':
            return status
