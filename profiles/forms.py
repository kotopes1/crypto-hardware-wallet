"""
A class representing a form for user input.

    This class inherits from the Form class provided by Django,
    which provides a set of
    methods and options to create and handle forms for user input
    in a Django application.
"""
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    A form for updating user profile information.

    This class inherits from the ModelForm class provided by Django,
    which provides a
    convenient way to create a form based on a Django model.
    """
    class Meta:
        """
        A class containing metadata for a model.

    Attributes:
        db_table (str): The name of the database
        table associated with the model.
        indexes (List[Tuple[str]]): A list of tuples
        representing the fields that should be indexed.
        """
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'profile-form-input')
            self.fields[field].label = False
