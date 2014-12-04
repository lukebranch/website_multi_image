{
    'name': 'Product Multi-Image',
    'description': 'This module adds multiple product images into a tab in product.template in a tab called Product Images, and allows an over-ride of product.image to allow for a multi-image carousel for the product view page.',
    'category': 'Website',
    'version': '1.0',
    'author': 'Luke Branch and Cristian Sebastian Rocha',
    'depends': ['product','sale'],
    'data': [
        'views/product_images.xml',
        'views/website_product_image_carousel.xml',
        'security/ir.model.access.csv', 
    ],
    'application': True,
}
