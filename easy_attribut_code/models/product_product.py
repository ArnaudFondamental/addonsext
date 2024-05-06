from odoo import fields, models, api
import logging
_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
    _inherit = "product.product"
    product_template_variant_value_ids = fields.Many2many('product.template.attribute.value',
                                                          relation='product_variant_combination',
                                                          domain=[('attribute_line_id.value_count', '>', 0)],
                                                          string="Variant Values", ondelete='restrict')

    @api.model_create_multi
    def create(self, vals_list):
        _logger.info("------ CREATE Product_product CA PASSE ICI  -----")
        _logger.info(type(vals_list))
        _logger.info(vals_list)
        for val_list in vals_list:
            variants = val_list["product_template_attribute_value_ids"][0]
            _logger.info(len(variants))
            _logger.info(variants)
            vars = variants[2]
            _logger.info(vars)
            code_pdt = "S" + self.env['product.template'].search([('id', '=', val_list["product_tmpl_id"])]).code
            i = 1
            _logger.info(code_pdt)
            res = code_pdt
            for var in vars:
                code = self.env['product.template.attribute.value'].search([('id', '=', var)]).product_attribute_value_id.code
                if i==3 and code != "XX":
                    res = res + "_" + code
                else:
                    if i == 2:
                        res = res + code + "M"
                    else:
                        res = res + code
                i += 1
                _logger.info(code)
            val_list["default_code"] = res
        _logger.info(vals_list)
        products = super(ProductProduct, self.with_context(create_product_product=True)).create(vals_list)
        # `_get_variant_id_for_combination` depends on existing variants
        self.env.registry.clear_cache()
        return products



    def write(self, values):
        _logger.info("------ WRITE Product_product CA PASSE ICI  -----")
        _logger.info(values)
        res = super(ProductProduct, self).write(values)
        return res