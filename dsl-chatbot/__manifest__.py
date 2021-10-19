# -*- coding: utf-8 -*-
{
    'name': 'DSL Payroll',
    'version': '14.0.1.0.0',
    'summary': """Odoo Template""",
    'description': """Odoo Template """,
    'category': 'Generic Modules/Odoo Template',
    'author': 'Daffodil Software Limited',
    'company': 'Daffodil Software Limited',
    'website': "https://smart.daffodil.family",
    'depends': ['base',
                'hr_payroll_community',
                'hr_payslip_monthly_report',
                'hr',
                'report_xlsx',
                'hrms_dashboard'
                ],
    'data': [
    ],
    'images': ['static/description/banner.gif'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 180.0,
    'currency': 'USD'
}