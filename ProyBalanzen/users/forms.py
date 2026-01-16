from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Fieldset

from .models import Usuario

# creación del formulario para el modelo de usuario personalizado
class UserForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # configuración básica de crispy forms
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_enctype = 'multipart/form-data'

        # Layout del formulario
        self.helper.layout = Layout(
            Fieldset(
                'Datos principales',
                Row(
                    Column('nombre', css_class = 'col-md-6'),
                    Column('apellidos', css_class = 'col-md-6'),
                    Column('email', css_class='col-md-6'), # email es el username del modelo
                    Column('telefono', css_class='col-md-6'),
                    Column('fecha_nacimiento', css_class='col-md-6'),
                ),
                Row(
                    Column('password', css_class='col-md-6')
                ),
                Row(
                    Submit('submit', 'Enviar', css_class='btn btn-primary')
                )
            ),
        )