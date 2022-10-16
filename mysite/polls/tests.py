from django.test import TestCase
from polls.models import Question, Choice

# Create your tests here.
class QuestionTest(TestCase):
    new_q
    def setUp(self):
        new_q = Question.objects.create(question_text="Is this a successful test?")
        #Choice.objects.create(question=q.pk, choice_text="Yes")
        #Choice.objects.create(question=q.pk, choice_text="Also Yes")

    def test_question(self):
        question = Question.objects.get(id=new_q.pk)
        self.assertEqual(question.question_text=="Is this a successful test?")
