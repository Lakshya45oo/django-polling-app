from django import forms
from .models import Choice


class VoteForm(forms.Form):
    """Form used to cast a vote on one question."""
    choice = forms.ModelChoiceField(
        queryset=Choice.objects.none(),
        widget=forms.RadioSelect,
        empty_label=None,
        error_messages={
            'required': 'Please select a choice before voting.',
            'invalid_choice': 'That is not a valid choice for this poll.',
        },
    )

    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only allow choices that belong to THIS question (validation)
        self.fields['choice'].queryset = question.choice_set.all()