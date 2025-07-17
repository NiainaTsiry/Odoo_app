{
    'name': 'artisanat',
    'version': '1.0',
    'summary': 'Module pour gérer les produits artisanaux',
    'depends': ['product', 'website'],  # ← ICI !!!
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/test_views.xml',
    ],
    'installable': True,
    'application': True,
}
