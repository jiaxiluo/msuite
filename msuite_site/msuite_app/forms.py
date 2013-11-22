from django import forms

# form class for displaying objects on the admin site using a list
class StringListField(forms.CharField):
	def prepare_value(self, value):
		return ', '.join(value)

	def to_python(self, value):
		if not value:
			return []
		return [item.strip() for item in value.split(',')]

