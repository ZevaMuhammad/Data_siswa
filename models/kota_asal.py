from odoo import models, fields

class genre(models.Model):
    _name = "kota.asal"
    
    name = fields.Char(string="Kota Asal", required=True )
    deskripsi_kota = fields.One2many("data.siswa","asal",string="Deskripsi Kota")