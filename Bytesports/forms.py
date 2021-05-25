#importamos ModelForm de django y nuestro modelo Match
from django.forms import ModelForm
from Bytesports.models import Match

class MatchForm(ModelForm):
	"""Declaramos una clase MatchForm que hereda de ModelForm y dentro de ella
	una clase Meta que tiene como argumentos un model (sera el modelo de nuestro 
		formulario) y fields que son los campos que queramos de ese modelo"""
	class Meta:
		model = Match
		fields = ['team_name', 'field_name', 'max_players','match_hour', 'location_field', 'team_vs']