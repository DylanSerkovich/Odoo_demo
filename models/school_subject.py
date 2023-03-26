from odoo import models,fields

class SchoolSubject(models.Model):
    _name = "school.subject"
    name = fields.Char("name")
    credits = fields.Integer("credits")
    max_students = fields.Integer("max_students")
    active = fields.Boolean("active")
    student_ids = fields.Many2many("school.student", string = "SchoolStudents")
    teacher_id = fields.Many2one("school.teacher", string = "SchoolTeacher")