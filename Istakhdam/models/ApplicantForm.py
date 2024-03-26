from odoo import models, fields


class applicantForm(models.Model):
    _inherit = 'hr.employee'
    father_name = fields.Char(string="Father Name")
    grand_father_name = fields.Char(string ="Grand Father Name")