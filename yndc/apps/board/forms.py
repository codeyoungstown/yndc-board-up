from django import forms

from board.models import Board, Event, House, Neighborhood


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        exclude = ['slug', 'created_by', 'created_at']

    def _list_checklist(self, prefix):

        cleaned_data = {}
        if hasattr(self, 'cleaned_data'):
            cleaned_data = self.cleaned_data

        initial = {}
        if hasattr(self, 'initial'):
            initial = self.initial

        fields = []
        for field in self.fields.items():
            if field[0].startswith('%s_check' % prefix):

                obj = {
                    'name': field[0],
                    'field': field[1],
                }
                
                if cleaned_data:
                    try:
                        obj['value'] = cleaned_data[field[0]]
                    except KeyError:
                        pass
                else:
                    try:
                        obj['value'] = initial[field[0]]
                    except KeyError:
                        pass

                fields.append(obj)

        return fields

    def outside_checklist_fields(self):
        return self._list_checklist('outside')

    def removal_checklist_fields(self):
        return self._list_checklist('removal')

    def general_checklist_fields(self):
        return self._list_checklist('general')


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        exclude = ['house']


class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['slug']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['house', 'created_by']
