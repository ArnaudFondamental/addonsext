# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    product_position_code = fields.Integer(string='Code position',default=1, config_parameter='easy_attribut_code.codepos',)

        #config_parameter='easy_attribut_code.pos_code',

