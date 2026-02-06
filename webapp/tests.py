from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskTests(TestCase):

    def test_create_task(self):
        response = self.client.post(reverse('task_list'), {'title': 'Test Task'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, 'Test Task')

    def test_complete_task(self):
        task = Task.objects.create(title='Incomplete Task')
        response = self.client.get(reverse('complete_task', args=[task.id]))
        task.refresh_from_db()
        self.assertTrue(task.completed)

    def test_delete_task(self):
        task = Task.objects.create(title='Task to Delete')
        response = self.client.get(reverse('delete_task', args=[task.id]))
        self.assertEqual(Task.objects.count(), 0)
