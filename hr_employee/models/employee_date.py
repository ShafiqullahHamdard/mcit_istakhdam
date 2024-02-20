from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    state = fields.Selection([('new', 'New'), ('old', 'Old')], string='Employee State', compute='_compute_employee_state', store=True)
        # fields.Selection([
        # ('new', 'New'),
        # ('old', 'Old'),
    # ], string='Employee State', compute='_compute_employee_state', store=True)

    hiring_date = fields.Date(string='Hiring Date', required=True)

    def _compute_employee_state(self):
        for employee in self:
            # Calculate the difference in months between hiring date and current date
            difference_in_months = (
                (fields.Date.today() - employee.hiring_date).days) // 30

            # Set the state based on the difference
            employee.state = 'old' if difference_in_months >= 6 else 'new'
