from django import forms
from .models import Animal, Enclosure, Keeper, VetCard, FeedingSchedule


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            'name', 'species', 'age', 'weight', 'description',
            'photo', 'is_on_display', 'animal_class', 'enclosure',
            'diets', 'keepers'
        ]


class EnclosureForm(forms.ModelForm):
    class Meta:
        model = Enclosure
        fields = ['name', 'area', 'capacity', 'description', 'photo', 'is_open', 'habitat']


class KeeperForm(forms.ModelForm):
    class Meta:
        model = Keeper
        fields = ['full_name', 'position', 'experience_years', 'phone', 'photo', 'bio']


class VetCardForm(forms.ModelForm):
    class Meta:
        model = VetCard
        fields = ['animal', 'health_status', 'vaccinations', 'allergies']


class FeedingScheduleForm(forms.ModelForm):
    class Meta:
        model = FeedingSchedule
        fields = ['animal', 'keeper', 'feeding_time', 'food_details', 'notes']
        widgets = {
            'feeding_time': forms.TimeInput(attrs={'type': 'time'}),
        }