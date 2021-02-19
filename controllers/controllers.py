# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request, Response
import json


class SaleOrder(http.Controller):
    @http.route('/sale-order/quality-survey', type='json', auth="none", methods=["POST"], csrf=False)
    def quality_survey(self, **kw):
        '''
        This will collect the portal ID and save the quality-survey value to the corresponding sale order(s).
        '''
        # Get the data from the request:
        data = json.loads(request.httprequest.data)
        order_id = data.get("orderId")
        quality_survey = data.get("quality-survey")

        # Ensure both values are present in the request:
        if order_id and quality_survey:
            # Get sale orders where the portal value is equal to the order_id from the request:
            sale_orders = list(request.env["sale.order"].sudo().search([("portal", "=", order_id)]))

            # Loop in case there are multiple sale orders with the same id:
            if sale_orders:
                for order in sale_orders:
                    order.write({
                        "quality_survey": quality_survey
                    })
                
                # Return True to show that update was successful:
                return "True"
            else:
                # Return error message
                return "No sale order found."
        else:
            # Return error message
            return "'orderId' and 'quality-survey' are required fields."
            