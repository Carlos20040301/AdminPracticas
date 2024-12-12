from odoo import models, fields, api

class PracticaRequest(models.Model):
    _name = 'practica.request'
    _description = 'Solicitud de Práctica'
    
    user_id = fields.Many2one('res.users', string='Usuario', default=lambda self: self.env.user)
    
    account = fields.Char(string='Numero de Cuenta', required=True)
    student_name = fields.Char(string='Nombre del Estudiante', required=True)
    career = fields.Selection([
        ('system', 'Ingenieria en Sistemas'),
        ('agro', 'Ingenieria Agroindustrial'),
        ('trade', 'Licenciatura en Comercio'),
        ('local', 'Licenciatura en Desarrollo Local'),
    ], string='Carrera', default='system')
    request_date = fields.Date(string='Fecha de Solicitud', default=fields.Date.context_today)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('submitted', 'Enviado'),
        ('approved', 'Aprobado'),
        ('rejected', 'Rechazado'),
    ], string='Estado', default='draft')

    espace = fields.Char()

    def action_approve(self):
        for record in self:
            record.state = 'approved'

    def action_reject(self):
        for record in self:
            record.state = 'rejected'