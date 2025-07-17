from odoo import models, fields

class Produit(models.Model):
    _name = 'mon.objet' 
    _description = 'Mon Objet Personnalisé'
    
    name = fields.Char(string='Nom')
    description = fields.Text(string='Description')