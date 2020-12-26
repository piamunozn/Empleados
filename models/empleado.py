from odoo import models, fields, api

class empleado(models.Model):
    _name = 'empleados.empleado'
    _description = 'empleados'
    
    name = fields.Char(string="nombre", required=True)
    email = fields.Char(string="email", required=True)
    phone = fields.Char(string="phone", required=True)

    gender = fields.Selection([
        ('masculino', 'masculino'),
        ('femenino', 'femenino'),
        ('otro', 'otro')
    ], default="masculino")

    marital = fields.Selection([
        ('soltero', 'Soltero'),
        ('casado', 'Casado'),
        ('conviviente', 'Conviviente'),
        ('viudo', 'Viudo'),
        ('divorciado', 'Divorciado')
    ], string='Marital Status', default='soltero')