from odoo import models, fields, api

class SolicitudGraduacion(models.Model):
    _name = 'graduacion.solicitud_graduacion'
    _description = 'Solicitud de Graduación'

    name = fields.Char(string='Nombre completo', required=True)
    numero_cuenta = fields.Char(string='Número de cuenta', required=True)
    correo_institucional = fields.Char(string='Correo institucional', required=True)
    carrera = fields.Selection([
        ('ingenieria_sistemas', 'Ingeniería en Sistemas'),
        ('ingenieria_alimentos', 'Ingeniería en Alimentos'),
        ('ingenieria_agroindustrial', 'Ingeniería Agroindustrial'),
        ('administracion_empresas', 'Administración de Empresas'),
        ('desarrollo_local', 'Desarrollo Local'),
    ], string='Carrera', required=True)
    telefono = fields.Char(string='Número de teléfono', required=True)
    direccion = fields.Text(string='Dirección', required=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente de entrega de documentos'),
        ('en_revision', 'En revisión'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ], string='Estado de la solicitud', default='pendiente', readonly=True)
    comentario = fields.Text(string='Comentario de Secretaría', readonly=True)

    documentos_necesarios = fields.Many2many(
        'graduacion.documentos_carrera',
        'graduacion_documentos_carrera_solicitud_rel',  # Nombre corto para la tabla intermedia
        'solicitud_id',  # Columna de la tabla intermedia
        'documento_id',  # Columna de la tabla intermedia
        string='Documentos necesarios',
        compute='_compute_documentos_necesarios',
        store=True
    )

    @api.depends('carrera')
    def _compute_documentos_necesarios(self):
        for record in self:
            if record.carrera:
                record.documentos_necesarios = self.env['graduacion.documentos_carrera'].search([('carrera', '=', record.carrera)])
            else:
                record.documentos_necesarios = False

    archivo_pdf = fields.Binary(string='Documento PDF', attachment=True)
    archivo_nombre = fields.Char(string='Nombre del archivo PDF')
