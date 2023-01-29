"""
Django forms widgets for handling file inputs.
This module contains widgets for handling file inputs, including the
ClearableFileInput widget for handling file clearing and
the gettext_lazy for handling translations.
Imports:
    ClearableFileInput :  Django's ClearableFileInput widget
    for handling file clearing
    gettext_lazy : Django's gettext_lazy for handling translations
"""
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
A custom ClearableFileInput widget.

This class is a custom implementation of Django's ClearableFileInput widget
with additional functionality such as custom file input text
and custom clear checkbox text.
Attributes:
    input_text (str): The text to display for the file input button.
    clear_checkbox_label (str): The text to display for the clear checkbox.
Methods:
    render: Renders the widget.
"""
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
