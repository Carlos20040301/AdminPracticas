from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

career = fields.Selection(related='user_id.career', store=True)
