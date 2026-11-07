from django.test import TestCase
from django.urls import reverse

from .models import Note


class NoteModelTest(TestCase):
    """Tests for the Note model."""

    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note."
        )

    def test_note_has_title(self):
        self.assertEqual(self.note.title, "Test Note")

    def test_note_has_content(self):
        self.assertEqual(
            self.note.content,
            "This is a test note."
        )

    def test_note_string_representation(self):
        self.assertEqual(str(self.note), "Test Note")

# Create your tests here.
