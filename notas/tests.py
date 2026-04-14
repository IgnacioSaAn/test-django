from django.test import TestCase, Client
from .models import Nota
from .forms import NotaForm
from django.contrib.auth.models import User
from django.urls import reverse

class NotaTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.nota = Nota.objects.create(titulo='Test Note', contenido='test note ejemplo', usuario=self.user)

    def test_nota_creation(self):
        self.assertEqual(self.nota.titulo, 'Test Note')
        self.assertEqual(self.nota.contenido, 'test note ejemplo')
        self.assertEqual(self.nota.usuario, self.user)

class NotaFormTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.nota = Nota.objects.create(titulo='Test Note', contenido='test note ejemplo', usuario=self.user)
        self.form_data = {
            'titulo': 'Test Note',
            'contenido': 'test note ejemplo',
        }
        self.form = NotaForm(data=self.form_data)

    def test_nota_form_valid(self):
        self.assertTrue(self.form.is_valid())



#