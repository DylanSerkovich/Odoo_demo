from odoo import models,fields

class SchoolStudents(models.Model):
    _name = "school.student"
    name = fields.Char("name")
    birth_date = fields.Date("birth_date")
    age = fields.Integer("age")
    final_exam_grade = fields.Float("final_exam_grade")
    subject_ids = fields.Many2Many("school.subject", string = "SchoolSubject")