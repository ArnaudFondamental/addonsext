from odoo import fields, models, api
import logging
_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
    _inherit = "product.product"
    product_template_variant_value_ids = fields.Many2many('product.template.attribute.value',
                                                          relation='product_variant_combination',
                                                          domain=[('attribute_line_id.value_count', '>', 0)],
                                                          string="Variant Values", ondelete='restrict')
    fg_ref = fields.Char(compute='_compute_myref')
    #default_code = fields.Char('Internal Reference', compute='_compute_myref', store= True)

    @api.depends('product_template_variant_value_ids', 'code')
    def _compute_myref(self):
        for record in self:
            i = 0
            attributs = record.product_template_variant_value_ids
            _logger.info("ATTRIBUTS : " + str(attributs))
            res = ""
            for attribut in attributs:
                _logger.info(" CODE ::: " + str(attribut.product_attribute_value_id.code))
                res = res + str(attribut.product_attribute_value_id.code)
                i = i + 1
                if i == 1:
                    res += self.product_tmpl_id.code
            record.fg_ref = res
            record.default_code = res





    #
    #
    # def write(self, values):
    #     _logger.info("values : " + str(values))
    #     # for myelement in self:
    #     #     _logger.info("WRITE WRITE on product.product : " + str(myelement.id))
    #     #     _logger.info("CODE product.template : " + str(myelement.product_tmpl_id.code))
    #     #     _logger.info("Combinaison : " + str(myelement.combination_indices))
    #     #     myref = myelement.product_tmpl_id.code
    #     #     for attribut in myelement.combination_indices.split(","):
    #     #         _logger.info("ATTRIBUT : " + str(attribut))
    #     #         code = self.env['product.template.attribute.value'].search(
    #     #             [('id', '=', attribut)]).product_attribute_value_id.code
    #     #         _logger.info("CODE ::::: " + str(code))
    #     #         myref = myref + code
    #     #         _logger.info("REF ::::: " + str(myref))
    #     #         #myelement.write({'default_code': myref})
    #
    #     res = super(ProductProduct, self).write(values)
    #     self.env.registry.clear_cache()
    #     return res
    #
