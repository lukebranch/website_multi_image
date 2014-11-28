{
    'name': 'Product Multi-Image',
    'description': 'This module adds multiple product images (22 currently) into a tab in product.template in a tab called Product Images',
    'category': 'Website',
    'version': '1.0',
    'author': 'A Collaboration between Luke Branch and Cristian Sebastian Rocha',
    'depends': ['product','sale'],
    'data': [
        'views/product_images.xml', 
        'security/ir.model.access.csv', 
    ],
    'application': True,
}
