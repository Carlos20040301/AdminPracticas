from odoo import models, fields, api

class SolicitudGraduacion(models.Model):
    _name = 'practica.solicitud_graduacion'
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
    comentario = fields.Text(string='Comentario del coordinador', readonly=True)

    # Relación Many2many con los documentos de la carrera
    documentos_necesarios = fields.Many2many(
        'practica.documentos_carrera',
        string='Documentos necesarios',
        compute='_compute_documentos_necesarios',
        store=True
    )

    @api.depends('carrera')
    def _compute_documentos_necesarios(self):
        for record in self:
            if record.carrera:
                record.documentos_necesarios = self.env['practica.documentos_carrera'].search([('carrera', '=', record.carrera)])
            else:
                record.documentos_necesarios = False

    #Campo para el archivo PDF de la solicitud
    archivo_pdf = fields.Binary(string='Documento PDF', attachment=True)
    archivo_nombre = fields.Char(string='Nombre del archivo PDF')