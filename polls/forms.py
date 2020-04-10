from django import forms

# Create your forms here.
class VotesForm(forms.Form):
    voter_first_name = forms.CharField(max_length=12)
    voter_last_name = forms.CharField(max_length=12)
    voter_id = forms.IntegerField(min_value=0)
    voter_choice = forms.CharField(max_length=30)
    vote_submit_time = forms.DateTimeField()