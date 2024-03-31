from django.test import TestCase
import logistic.forms
from logistic.forms.eventForm import EventForm
from logistic.forms.taskForm import TaskForm
from logistic.forms.taskForm import TaskChecklist
from logistic.forms.taskForm import TaskForm, TaskChecklist 


class forms_test(TestCase):
    def test_event_form_valid(self):
        form = EventForm(data={
            'name': 'Evento de prueba',
            'executionDate': '2022-12-31T23:59',
            'place': 'Lugar de prueba',
            'progress': 'Avance de prueba',
            'finishDate': '2023-01-01T00:01',
            'important': True,
            'user': 1,
        })
        self.assertFalse(form.is_valid())
        
    def test_event_form_invalid(self):
        form = EventForm(data={})
        self.assertFalse(form.is_valid())
        
    def test_task_checklist_form_valid(self):
        form = TaskChecklist(data={
            'done': True,
        })
        self.assertTrue(form.is_valid())
        
    def test_field_labels(self):
        event_form = EventForm()
        task_form = TaskForm()
        task_checklist_form = TaskChecklist()  # Utiliza TaskChecklist importado correctamente

        self.assertEqual(event_form.fields['name'].label, 'Nombre')
        self.assertEqual(task_form.fields['event'].label, 'Evento')
        self.assertEqual(task_checklist_form.fields['done'].label, 'Hecho')