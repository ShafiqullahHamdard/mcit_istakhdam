from odoo import models, fields, api


class Department(models.Model):
    # _name = 'custom.department'
    # _description = 'Department'
    # name = fields.Char(string='Name', required=True)
    # employees = fields.One2many('department.hr_employee','department_id', string='Employees')
    _name = 'custom.department'
    # _inherit = ['mail.thread']
    _description = 'Department'
    name = fields.Char(string='Department Name')
    Manager = fields.Char(string="Manager Name")
    parent_department = fields.Char(string='parent Department')
    employee_ids = fields.One2many('custom.employee', 'department_id', string='Manager')
    job_ids = fields.One2many('custom_job.job', 'department_id', string='Jobs')



