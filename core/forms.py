from django import forms

from .models import Vehicle, Provider, Supply, Maintenance, Traffic

# Formulário de cadastro de veículo
class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'


# Formulário de cadastro de fornecedor
class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'


class SuplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = '__all__'


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = '__all__'


class TrafficForm(forms.ModelForm):
    class Meta:
        model = Traffic
        fields = '__all__'