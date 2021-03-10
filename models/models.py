# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_note = fields.Text()
    # _inherit = 'sale.order'

    # quality_survey = fields.Text()
