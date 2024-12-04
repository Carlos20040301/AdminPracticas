from datetime import datetime
import re
from odoo.exceptions import ValidationError  # type: ignore # Esta es la importación correcta

from odoo import models, fields, api # type: ignore

class SolicitudPractica(models.Model):
    _name = 'practica.solicitud_practica'
    _description = 'Solicitud de Práctica'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nombre completo', required=True)
    numero_cuenta = fields.Char(string='Número de cuenta', required=True, size=11)
    correo_institucional = fields.Char(string='Correo institucional', required=True)
    carrera = fields.Selection([
        ('ingenieria_sistemas', 'Ingeniería en Sistemas'),
        ('ingenieria_agroindustrial', 'Ingeniería Agroindustrial'),
        ('administracion_empresas', 'Administración de Empresas'),
        ('desarrollo_local', 'Desarrollo Local'),
        ('comercio_agro', 'Comercio Internacional con Orientación en Agroindustria'),
        ('tecnologia_alimentos', 'Técnico en Tecnología de Alimentos'),
        ('produccion_agricola', 'Técnico en Producción Agrícola'),
        ('admin_cafetaleras', 'Técnico en Administración de Empresas Cafetaleras'),
        ('agro_exportacion', 'Técnico en Agroexportación'),
    ], string='Carrera', required=True)
    correo_personal = fields.Char(string='Correo personal', required=True)
    telefono = fields.Char(string='Número de teléfono', required=True, size=8)
    direccion = fields.Text(string='Dirección', required=True)
    estado = fields.Selection([
        ('pendiente', 'Documentación Pendiente'),
        ('en_revision', 'En revisión'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ], string='Estado de la solicitud', default='pendiente', readonly=True)
    comentario = fields.Text(string='Comentarios', readonly=True)

    estado_fecha = fields.Datetime(string='Estado cambiado el', readonly=True)
    comentario_fecha = fields.Datetime(string='Fecha del comentario', readonly=True)

    # Relación Many2many con los documentos de la carrera
    documentos_necesarios = fields.Many2many(
        'practica.docs_practica',
        string='Documentos necesarios',
        compute='_compute_documentos_necesarios',
        store=True
    )

    @api.depends('carrera')
    def _compute_documentos_necesarios(self):
        for record in self:
            if record.carrera:
                documentos = self.env['practica.docs_practica'].search([('carrera', '=', record.carrera)])
                record.documentos_necesarios = [(6, 0, documentos.ids)]  # Asigna los IDs encontrados
            else:
                record.documentos_necesarios = [(5, 0, 0)]  # Limpia la relación si no hay carrera seleccionada

    def action_pendiente(self):
        for record in self:
            record.estado = 'pendiente'

    def action_approve(self):
        for record in self:
            record.estado = 'aprobada'

    def action_disaprove(self):
        for record in self:
            record.estado = 'rechazada'
    
    def action_revision(self):
        for record in self:
            record.estado = 'en_revision'

    def write(self, vals):
        # Actualiza las fechas al cambiar comentario o estado
        if 'comentario' in vals and vals['comentario']:
            vals['comentario_fecha'] = datetime.now()
        if 'estado' in vals and vals['estado']:
            vals['estado_fecha'] = datetime.now()
        return super(SolicitudPractica, self).write(vals)
    
    @api.constrains('numero_cuenta')
    def _check_numero_cuenta(self):
        for record in self:
            if len(record.numero_cuenta) != 11 or not record.numero_cuenta.isdigit():
                raise ValidationError("El número de cuenta debe tener 11 dígitos numéricos.")

    @api.constrains('telefono')
    def _check_telefono(self):
        for record in self:
            if len(record.telefono) != 8 or not record.telefono.isdigit():
                raise ValidationError("El teléfono debe tener 8 dígitos numéricos.")

    @api.constrains('correo_institucional', 'correo_personal')
    def _check_correo(self):
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        for record in self:
            if record.correo_institucional and not re.match(email_regex, record.correo_institucional):
                raise ValidationError("El correo institucional no tiene un formato válido.")
            if record.correo_personal and not re.match(email_regex, record.correo_personal):
                raise ValidationError("El correo personal no tiene un formato válido.")

    @api.constrains('direccion')
    def _check_direccion(self):
        for record in self:
            if len(record.direccion) >= 200:
                raise ValidationError("La dirección no debe tener más de 100 caracteres.")