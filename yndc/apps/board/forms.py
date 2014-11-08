from django import forms

from board.models import Board, House


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        exclude = ['slug']

    def _list_checklist(self, prefix):

        cleaned_data = {}
        if hasattr(self, 'cleaned_data'):
            cleaned_data = self.cleaned_data

        fields = []
        for field in self.fields.items():
            if field[0].startswith('%s_check' % prefix):

                obj = {
                    'name': field[0],
                    'field': field[1],
                }

                try:
                    obj['value'] = cleaned_data[field[0]]
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
