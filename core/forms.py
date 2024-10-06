from django import forms
from django.core.mail.message import EmailMessage

from .models import Produto

class ContatoForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=180)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['name']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\n E-mail: {email}\n assunto: {assunto}\n mensagem: {mensagem}'

        mail = EmailMessage( 
            subject='E-mail enviado pelo sistema django2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br',],
            headers={'Reply-to': email} 
        )
        mail.send()

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']