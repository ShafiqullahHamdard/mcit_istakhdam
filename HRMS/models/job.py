from odoo import models, fields


class Job(models.Model):
    _name = 'custom_job.job'
    _description = 'Custom Job'
    name = fields.Char(string='Job Title')
    description = fields.Text(string='Description')
    department_id = fields.Many2one('custom.department', string='Department')
    # manager_id = fields.Many2one('custom.employee', string='Manager')
    salary = fields.Float(string='Salary')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    is_active = fields.Boolean(string='Active', default=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancel')], string='status')

    _sql_constraints = [
        ('unique_field_constraint', 'UNIQUE(name)', 'Error message for unique constraint violation.'),
        ('check_field_constraint', 'CHECK(salary>5000)', 'Error message for check constraint violation.'),
        ]
