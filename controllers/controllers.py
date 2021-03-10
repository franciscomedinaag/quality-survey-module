# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request, Response
import json


class SaleOrder(http.Controller):
    @http.route('/sale-order/quality-survey', type='json', auth="none", methods=["POST"], csrf=False)
    def quality_survey(self, **kw):
        '''
        This will collect the customer data from Shopify registration and create a customer
        '''

        # # Get the data from the request:
        customer = json.loads(request.httprequest.data)
        #  order_id = data.get("orderId")
        #  quality_survey = data.get("quality-survey")

        partner = request.env['res.partner'].sudo().create(
            {'name':customer.get('first_name') + " " + customer.get('last_name') ,
                'shopify_client_id': customer.get('id'),
                'customer': True,
                'email': customer.get('email'),
                'phone': phone_customer,
                'customer_note' : customer.get('note')
            })
        
        return "created"
       
       
        #ultimo_consumidor_tag = request.env['marvelfields.clasificaciones'].sudo().search([('name','=', 'Ultimo Consumidor')])
        #shopify_tag = request.env['marvelfields.subclases'].sudo().search([('name','=','Shopify')]) 
                
        # partner.clasificaciones_ids = [(4, ultimo_consumidor_tag.id)]
        # partner.subclases_ids = [(4, shopify_tag.id)]
        # partner.ncliente = customer.get('id')}





        # # Ensure both values are present in the request:
        # if order_id and quality_survey:
        #     # Get sale orders where the portal value is equal to the order_id from the request:
        #     sale_orders = list(request.env["sale.order"].sudo().search([("portal", "=", order_id)]))

        #     # Loop in case there are multiple sale orders with the same id:
        #     if sale_orders:
        #         for order in sale_orders:
        #             order.write({
        #                 "quality_survey": quality_survey
        #             })
                
        #         # Return True to show that update was successful:
        #         return "True"
        #     else:
        #         # Return error message
        #         return "No sale order found."
        # else:
        #     # Return error message
        #     return "'orderId' and 'quality-survey' are required fields."
            