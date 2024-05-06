# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Reference=f(valeur d'attributs)",
    'version': '0.1',
    'author': "Fondamental Group - Arnaud Gay",
    'description': """
Permit to have code on attribute
0.1 : 
- add code on model and attribute view
- auto compute ref when variant is created
TODO
- permit to generate code with just value attribut
- Add Prefix/Suffix on product reference, white char, illimited attributs with boolean is in ref
====================""",
    'website': 'https://www.fondamental-corporate.com/',
    'depends': ['stock'],
    'data': ['views/product_attribute_code_view.xml',
             'views/product_template_code_view.xml'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}