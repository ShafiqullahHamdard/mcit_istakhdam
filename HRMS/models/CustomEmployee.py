from odoo import api, fields, models


# from datetime import date


class HrEmployee(models.Model):
    _name = "custom.employee"
    _description = "Employee"
    _order = 'name'
    # _inherit = ['mail.thread']
    name = fields.Char(string="نوم")
    fatherName = fields.Char(string="پلار نوم")
    GrandFatherName = fields.Char(string="نیکه نوم")
    phone = fields.Integer(string="ټیلیفون نمبر")
    Email = fields.Char(string="برېښنالیک")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'other')], string="جنسیت")
    Date_of_birth = fields.Date(string='تولد نیټه', default=fields.date.today())
    # , default = fields.date.context_today()
    # department_id = fields.Integer(string ='Department_id')
    department_id = fields.Many2one('custom.department', string='ډیپارټمنټ نوم')
    # priority = fields.Selection([
    #     ('0', 'Low'),
    #     ('1', 'Medium'),
    #     ('2', 'High')], string='Priority')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancel')], string='status')

