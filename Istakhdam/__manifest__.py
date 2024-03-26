# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Istakhdam_Amiriat',
    'version': '1.2',
    'summary': 'HR_Employee ',
    'sequence': -100,
    'description': """ ERP module implementation """,
    'category': 'Human Resource',
    'website': '',
    'images': ['images/accounts.jpeg'],
    'depends': ['hr'],
    'data': ['security/ir.model.access.csv',
             'views/customField.xml',
              'reports/employeeReportTemplate.xml','reports/employeeAction.xml',
             'reports/ReportAction.xml',
             'reports/reportTemplate.xml'],
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
