import datetime
from django.test import TestCase
from django.utils import timezone

from .models import *

class QuestionModelTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() retourne false pour une question avec une date de création dans le future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(created_at=time)
        self.assertIs(future_question.was_published_recently(), False)
    
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() retourne False si la question à été posé il y a plus de 1 jour
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(created_at=time)
        self.assertIs(old_question.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_question(self):
        """
        Dois me retourner True si la question date de moins de 1 jour
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(created_at=time)
        self.assertIs(recent_question.was_published_recently(), True)
        
