from odoo import models, fields, api

class vistacoordinador(models.Model):
    _name = 'vista.coordinador'
    _description = 'Vista Solicitud de Práctica'

    name = fields.Char(string='Nombre del Coordinador', required=True)