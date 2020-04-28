
from django import forms
from Swiggy_admin.models import StateModel
from Swiggy_admin.models import CityModel
from Swiggy_admin.models import AreaModel
from Swiggy_admin.models import RestaurantTypeModel

class StateForm(forms.ModelForm):
    class Meta:
        model = StateModel
        fields = ('state_name',)

class CityForm(forms.ModelForm):
    class Meta:
        model = CityModel
        fields = "__all__"
        exclude = ('city_no',)

class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaModel
        fields = "__all__"
        exclude = ('area_no',)

class RestaurantTypeForm(forms.ModelForm):
    class Meta:
        model = RestaurantTypeModel
        fields = ('type_name',)
