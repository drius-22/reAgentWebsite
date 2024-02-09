from django import forms

class contactus_form(forms.Form):
    form_name = forms.CharField(strip=True, 
                                label='Nombre', 
                                max_length=100,
                                error_messages={'required': 'Porfavor ingrese un nombre.','max_length':'El nombre es muy largo.'},
                                widget=forms.TextInput(attrs={'class': 'form-input'})
                                )
    form_email = forms.EmailField( label='Correo Electrónico ', 
                                    error_messages={'required': 'Porfavor ingrese un email.','invalid':'Ingrese un valido email.'},
                                    widget=forms.EmailInput(attrs={'class': 'form-input'})
                                    )
    form_phone = forms.CharField(strip=True,
                                label='Numero de Teléfono',
                                max_length=50,
                                error_messages={'required': 'Porfavor ingrese un numero de telefono.','max_length':'El numero es muy largo.'},
                                widget=forms.TextInput(attrs={'class': 'form-input'})
                                )
    form_message = forms.CharField( 
                            label='Mensaje' ,
                            required=False,
                            max_length=500,
                            error_messages={'max_length':'El mensaje es muy largo.'},
                            widget=forms.Textarea(attrs={'class': 'form-input'})
                            )

