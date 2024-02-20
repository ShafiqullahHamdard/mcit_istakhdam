# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Employee',
    'version': '1.0.0',
    'category': 'Human Resource',
    'sequence': -100,
    'summary': 'Employee Management System',
    'description': """Employee Management System""",
    'depends':['hr'],
    'data': [

        'view/employee.xml',
        # 'view/date.xml',
        'report/report.xml',
        'report/employee_report.xml',
        # 'reprot/emp_report_template.xml',

    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
