# Copyright (c) 2024, Deep Prakash Srivastava and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Quiz(Document):
	pass
import frappe

import frappe
from frappe import _
from frappe.utils import now

@frappe.whitelist()
def get_next_question():
    last_question = frappe.session.get('last_question')

    if not last_question:
        frappe.session['last_question'] = None
        last_question = None

    next_question = frappe.get_all('Quiz', filters={'name': ['>', last_question]}, fields=['name', 'question', 'options'], limit=1)

    if next_question:
        next_question = next_question[0]
        frappe.session['last_question'] = next_question['name']
        return next_question
    else:
        return None

@frappe.whitelist()
def submit_answer(question_id, selected_option):
    correct_answer = frappe.get_value('Quiz', question_id, 'correct_answer')
    if selected_option == correct_answer:
        score = 2
    else:
        score = 0

    return score

def update_scores():
    # This function will be called by the scheduler every 10 seconds
    frappe.logger("Quiz Timer", "Updating scores...")
    # Add your score update logic here
    pass
@frappe.whitelist()
def submit_answer(question_id, selected_option):
    correct_answer = frappe.get_value('Quiz', question_id, 'correct_answer')
    if selected_option == correct_answer:
        score = 2
    else:
        score = 0

    return score
