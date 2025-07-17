from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class ProductAddController(http.Controller):

    @http.route('/product/add', auth='public', website=True)
    def product_add_page(self, **post):
        return request.render('artisanat.product_views', {})
    
    @http.route('/', auth='public', website=True)
    def product_page(self, **post):
        return request.render('artisanat.test', {})
