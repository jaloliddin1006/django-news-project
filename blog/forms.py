from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'required': True}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body', 'required': True}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control', 'required': False, 'accept': 'image/*'}))
    # category = forms.ModelChoiceField(queryset=UserDefinedCode.objects.filter(owner=user))
    
    class Meta:
        model = Article
        fields = ('title', 'subtitle', 'body', 'image', 'category')
        
        
    # def clean_field(self):
    #     data = self.cleaned_data["field"]
        
    #     return data

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 10:
            raise forms.ValidationError('Juda qisqa')
        return title
    
    def save(self, commit=True):
        instance = super(ArticleForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance