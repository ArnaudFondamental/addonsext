from odoo import fields, models, api
import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = "product.template"
    code = fields.Text('Code', required=True)
