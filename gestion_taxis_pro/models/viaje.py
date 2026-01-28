
from odoo import models, fields, api

class Viaje(models.Model):
    _name = 'taxi.viaje'
    _description = 'Viaje Taxi'

    name = fields.Char(default='Nuevo')
    conductor_id = fields.Many2one('taxi.conductor')
    taxi_id = fields.Many2one('taxi.taxi')
    tarifa_id = fields.Many2one('taxi.tarifa')

    origen = fields.Char(required=True)
    destino = fields.Char(required=True)

    distancia_km = fields.Float()
    minutos_espera = fields.Float()

    precio = fields.Float(compute='_calcular_precio', store=True)

    fecha_inicio = fields.Datetime()
    fecha_fin = fields.Datetime()

    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ], default='pendiente')

    @api.depends('distancia_km', 'minutos_espera', 'tarifa_id')
    def _calcular_precio(self):
        for r in self:
            if r.tarifa_id:
                r.precio = (
                    r.tarifa_id.precio_base +
                    (r.distancia_km * r.tarifa_id.precio_km) +
                    (r.minutos_espera * r.tarifa_id.precio_min_espera)
                )
            else:
                r.precio = 0

    def action_iniciar(self):
        for r in self:
            r.estado = 'en_progreso'
            r.fecha_inicio = fields.Datetime.now()

    def action_completar(self):
        for r in self:
            r.estado = 'completado'
            r.fecha_fin = fields.Datetime.now()

    def action_cancelar(self):
        for r in self:
            r.estado = 'cancelado'
