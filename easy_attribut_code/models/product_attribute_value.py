from odoo import fields, models, api
import logging
_logger = logging.getLogger(__name__)

class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'
    code = fields.Text('Code', required=True)