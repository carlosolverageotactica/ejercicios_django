from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from polls.models import Pregunta

class PollsViewsTestCase(TestCase):
    def setUp(self):
        self.question = Pregunta.objects.create(
            pregunta_texto="Test question",
            publica_fecha=timezone.now()
        )
        self.choice = self.question.opcion_set.create(
            opcion_texto="Choice 1",
            votos=0
        )

    def test_index_view(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test question")

    def test_detail_view_success(self):
        response = self.client.get(reverse('polls:detail', args=(self.question.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test question")
        self.assertContains(response, "Choice 1")

    def test_detail_view_404(self):
        response = self.client.get(reverse('polls:detail', args=(999,)))
        self.assertEqual(response.status_code, 404)
