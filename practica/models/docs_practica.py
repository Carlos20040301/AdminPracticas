from odoo import models, fields, api # type: ignore

class DocumentosPractica(models.Model):
    _name = 'practica.docs_practica'
    _description = 'Documentos Requeridos para Práctica'

    user_id = fields.Many2one('res.users', string='Usuario', default=lambda self: self.env.user)

    name = fields.Char(string='Nombre', required=True)
    #carrera_id = fields.Many2one('practica.carrera', string='Carrera', required=True)
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
    descripcion = fields.Text(string='Descripción')
    archivo_pdf = fields.Binary(string='Archivo PDF')
    archivo_nombre = fields.Char(string='Nombre del archivo')