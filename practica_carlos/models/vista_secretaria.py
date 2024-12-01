from odoo import models, fields, api

class VistaSecretaria(models.Model):
    _name = 'graduacion.vista_secretaria'
    _description = 'Vista de Secretaría'

    nombre_secretaria = fields.Char(string='Nombre de la Secretaría', required=True)
