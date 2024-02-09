from django import forms


CITY_COUNTRY_CHOICES = [
    ('Guayaquil', 'Ecuador - Guayaquil'),
    ('Quito', 'Ecuador - Quito')
]
POSSIBLE_CATEGORIES= [
        ('departamento', 'Departamento'),
        ('casa', 'Casa'),
        ('terreno', 'Terreno'),
]
POSSIBLE_TYPES= [
        ('venta', 'Venta'),
        ('renta', 'Renta'),
]

AMENITIES_CHOICES =[
    ('calefaccion', 'Calefacción'),
    ('patio', 'Patio'),
    ('piscina', 'Piscina'),
    ('wi-fi', 'Wi-Fi'),
    ('gimnasio', 'Gimnasio'),
]






class RequestVisit(forms.Form):

    request_name = forms.CharField(strip=True, 
                                label='Nombre', 
                                max_length=100,
                                error_messages={'required': 'Porfavor ingrese un nombre.','max_length':'El nombre es muy largo.'},
                                widget=forms.TextInput(attrs={'class': 'form-input'})
                                )
    request_email = forms.EmailField( error_messages={'required': 'Porfavor ingrese un email.','invalid':'Ingrese un valido email.'},
                                    widget=forms.EmailInput(attrs={'class': 'form-input'})
                                    )
    request_phone = forms.CharField(strip=True,
                                label='Telefono',
                                max_length=50,
                                error_messages={'required': 'Porfavor ingrese un numero de telefono.','max_length':'El numero es muy largo.'},
                                widget=forms.TextInput(attrs={'class': 'form-input'})
                                )
    request_message = forms.CharField( required=False,
                            max_length=500,
                            error_messages={'max_length':'El mensaje es muy largo.'},
                            widget=forms.Textarea(attrs={'class': 'form-input'})
                            )







class FindYourProperty(forms.Form):

    country_city = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=CITY_COUNTRY_CHOICES
    )
    type_property = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=POSSIBLE_CATEGORIES
    )
    state_property = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=POSSIBLE_TYPES
    )
    n_bathrooms = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])
    n_rooms = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])
    lower_range_price = forms.IntegerField(initial= 0)
    higher_range_price = forms.IntegerField(initial= 1000000)
    lower_range_size = forms.IntegerField(initial= 0)
    higher_range_size = forms.IntegerField(initial= 1000000)
    amenities = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=AMENITIES_CHOICES,
    )


