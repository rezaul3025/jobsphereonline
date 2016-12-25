from django import forms
from jobsphereonline.models import Employer

class EmployerForm(forms.ModelForm):
	class Meta:
		model = Employer
		fields = ('title','description','address','website','logo','email',)