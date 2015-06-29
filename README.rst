PRESTASHOP Apis based on django ORM
=====================================

What's that?
-----------

Is a library to connect with the apis of a prestashop website.


How to use
----------

In a similar way to django orm

Using it 
---------------

.. code-block:: python
   
   # Configure
   from prestaorm import Api
   Api.config(url, key)
                
   # Use the api
   from prestaorm.models import Product
                
   # Get a list of instances of products
   products = Product.objects.filter(name="Product%").sort_by("name")

   # Get one instance
   product, _ = Product.objects.get_or_create(name="Product1", reference="REF1")                
   product.price = 8  
   product.save()             


Work in progress
-------------------
This is a work in progress. I'm implementing only the models that I would need. Extra help is welcome.

