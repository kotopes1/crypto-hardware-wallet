"""
The forms module in Django provides a collection of form fields and widgets
that can be used to create HTML forms.
The forms module includes a variety of form fields such as CharField,
IntegerField, and ChoiceField, as well as widgets like TextInput and Select.
These can be used to create form classes
that define the fields and validation for a form.

To use the forms module, you will need to import it and create a form class
that inherits from forms.Form. You can then add fields to the form using
the various form fields and widgets provided by the module.
Once you have defined your form, you can use it in a view
to handle form submissions and display the form in a template.

"""
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
The OrderForm class is a ModelForm that provides a form for creating and
updating Order models.
This class inherits from forms.ModelForm and is associated with the Order
model.
It automatically creates form fields for each of the model's
fields and allows for
easy validation and handling of form submissions.
To use the OrderForm, you will need to import it and create
an instance of the class.
You can then use this instance to display the form in a template
and handle form submissions in a view.
The form also includes additional fields, widgets and validations.
    """
    class Meta:
        """
        The Meta class is used to specify additional options for the OrderForm.
        This class is used to specify the model associated with the form,
        """
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
