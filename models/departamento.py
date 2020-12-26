from odoo import models, fields, api

class departamento(models.Model):
    _name = 'empleados.departamento'
    _description = 'departamento'

    name = fields.Char(string="nombre")

   