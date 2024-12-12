from odoo import models, fields # type: ignore

class DocumentosCarrera(models.Model):
    _name = 'practica.documentos_carrera'
    _description = 'Documentos Requeridos por Carrera'

    name = fields.Char(string='Nombre del documento', required=True)
    carrera = fields.Selection([
        ('ingenieria_sistemas', 'Ingeniería en Sistemas'),
        ('ingenieria_alimentos', 'Ingeniería en Alimentos'),
        ('ingenieria_agroindustrial', 'Ingeniería Agroindustrial'),
        ('administracion_empresas', 'Administración de Empresas'),
        ('desarrollo_local', 'Desarrollo Local'),
    ], string='Carrera', required=True)
    descripcion = fields.Text(string='Descripción del documento')
    archivo_pdf = fields.Binary(string='Archivo PDF')
    archivo_nombre = fields.Char(string='Nombre del archivo')