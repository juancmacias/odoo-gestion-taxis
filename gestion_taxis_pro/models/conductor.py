
from odoo import models, fields

class Conductor(models.Model):
    _name = 'taxi.conductor'
    _description = 'Conductor Taxi'

    name = fields.Char(required=True)
    telefono = fields.Char()
    licencia = fields.Char()
    taxi_id = fields.Many2one('taxi.taxi')
    activo = fields.Boolean(default=True)
