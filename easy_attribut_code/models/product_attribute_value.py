from odoo import fields, models, api
import logging
_logger = logging.getLogger(__name__)


class ProductAttributeValue(models.Model):
    _name = 'product.attribute.value'
    code = fields.Text('Code', required=True,)

class ProductAttributeValue(models.Model):
    _inherit = ['product.attribute', 'mail.thread', 'mail.activity.mixin']
    _name = 'product.attribute'
    value_ids = fields.One2many(
        comodel_name='product.attribute.value',
        inverse_name='attribute_id',
        string="Values", copy=True, tracking=True,)