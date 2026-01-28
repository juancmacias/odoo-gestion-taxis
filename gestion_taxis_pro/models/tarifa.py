
from odoo import models, fields

class TarifaTaxi(models.Model):
    _name = 'taxi.tarifa'
    _description = 'Tarifa Taxi'

    name = fields.Char(required=True)
    precio_base = fields.Float(default=3.0)
    precio_km = fields.Float(default=1.5)
    precio_min_espera = fields.Float(default=0.5)
