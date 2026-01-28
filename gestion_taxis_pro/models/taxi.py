
from odoo import models, fields

class Taxi(models.Model):
    _name = 'taxi.taxi'
    _description = 'Taxi'

    name = fields.Char(string='Matrícula', required=True)
    marca = fields.Char()
    modelo = fields.Char()
    activo = fields.Boolean(default=True)
