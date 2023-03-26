from odoo import models,fields

class SchoolTeacher(models.Model):
    _name = "school.teacher"
    name = fields.Char("name")
    profile = fields.Text("profile")
    subject_ids = fields.One2many("shool.subject", "teacher_id",  string = "SchoolSubject")