# -*- coding: utf-8 -*-
# from odoo import http


# class Pad(http.Controller):
#     @http.route('/pad/pad', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pad/pad/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pad.listing', {
#             'root': '/pad/pad',
#             'objects': http.request.env['pad.pad'].search([]),
#         })

#     @http.route('/pad/pad/objects/<model("pad.pad"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pad.object', {
#             'object': obj
#         })

