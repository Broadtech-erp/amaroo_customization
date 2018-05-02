# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Amaroo Customization',
    'version' : '1.0',
    'summary': 'Get default account and tax from vendor',
    'sequence': 30,
    'description': """
Get default expense account and tax from vendor in invoice line
    """,
    'category': 'Custom',
    'author' : 'Amaroo Solutions',
    'website': 'http://amaroosolutions.co.uk/',
    'images' : [],
    'depends' : ['account', 'purchase'],
    'data': [
        'views/account_invoice_view.xml',
        'views/partner_view.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
