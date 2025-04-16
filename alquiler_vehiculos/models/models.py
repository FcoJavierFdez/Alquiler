# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class alquiler_vehiculos(models.Model):
#     _name = 'alquiler_vehiculos.alquiler_vehiculos'
#     _description = 'alquiler_vehiculos.alquiler_vehiculos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
