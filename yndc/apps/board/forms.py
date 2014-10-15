from django import forms

from board.models import Board, House


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        exclude = ['slug']

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        exclude = ['house']
        
