from django import forms

class CommentForm(forms.Form):
	author=forms.CharField(max_length=70,
		widget=forms.TextInput(attrs={
				"class":"form-control",
				"placeholder": "Vase ime"

			}))

	body=forms.CharField(widget=forms.Textarea(attrs={
			"class":"form-control",
			"placeholder":"Vas komentar"
		}))