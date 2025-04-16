# -*- coding: utf-8 -*-
# from odoo import http


# class AlquilerVehiculos(http.Controller):
#     @http.route('/alquiler_vehiculos/alquiler_vehiculos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alquiler_vehiculos/alquiler_vehiculos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('alquiler_vehiculos.listing', {
#             'root': '/alquiler_vehiculos/alquiler_vehiculos',
#             'objects': http.request.env['alquiler_vehiculos.alquiler_vehiculos'].search([]),
#         })

#     @http.route('/alquiler_vehiculos/alquiler_vehiculos/objects/<model("alquiler_vehiculos.alquiler_vehiculos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alquiler_vehiculos.object', {
#             'object': obj
#         })
