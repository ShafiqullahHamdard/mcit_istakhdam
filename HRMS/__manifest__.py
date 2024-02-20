# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'ERP1',
    'version': '1.2',
    'summary': 'HR_Employee ',
    'sequence': -100,
    'description': """ ERP module implementation """,
    'category': 'Human Resource',
    'website': '',
    'images': ['images/accounts.jpeg'],
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/EmployeeMenu.xml',
        'views/DepartmentMenu.xml','security/groups.xml',
        'views/form.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'post_init_hook': '',
    'assets': {
        'web._assets_primary_variables': [],
        'web.assets_backend': [],
        'web.assets_frontend': [],
        'web.assets_tests': [],
        'web.gunit_suite_tests': [

        ],
    },
    'license': 'LGPL-3',
}
