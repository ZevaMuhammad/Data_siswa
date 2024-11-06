from odoo import models, fields

class genre(models.Model):
    _name = "sekolah.asal"
    
    name = fields.Char(string="sekolah Asal", required=True )
    alamat_sekolah = fields.One2many("data.siswa","asals",string="Alamat Sekolah")