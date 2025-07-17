from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    custom_field = fields.Char(string="Champ personnalisé")