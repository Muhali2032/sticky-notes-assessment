
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


class NoteCRUDTest(TestCase):
    """Tests for Sticky Notes CRUD functionality."""

    def setUp(self):
        self.note = Note.objects.create(
            title="Original Note",
            content="Original content."
        )

    def test_view_notes(self):
        response = self.client.get(reverse('note_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Original Note")

    def test_create_note(self):
        response = self.client.post(
            reverse('note_create'),
            {
                'title': 'New Note',
                'content': 'New note content.'
            }
        )

        self.assertRedirects(response, reverse('note_list'))
        self.assertTrue(
            Note.objects.filter(title='New Note').exists()
        )

    def test_update_note(self):
        response = self.client.post(
            reverse('note_update', args=[self.note.pk]),
            {
                'title': 'Updated Note',
                'content': 'Updated content.'
            }
        )

        self.assertRedirects(response, reverse('note_list'))

        self.note.refresh_from_db()

        self.assertEqual(self.note.title, 'Updated Note')
        self.assertEqual(self.note.content, 'Updated content.')

    def test_delete_note(self):
        response = self.client.post(
            reverse('note_delete', args=[self.note.pk])
        )

        self.assertRedirects(response, reverse('note_list'))
        self.assertFalse(
            Note.objects.filter(pk=self.note.pk).exists()
        )
