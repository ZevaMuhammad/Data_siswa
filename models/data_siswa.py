from odoo import models, fields, api
from datetime import datetime

class DataSiswa(models.Model):
    _name = "data.siswa"
    _description = "Data Siswa"

    nomor_induk = fields.Char(string="Nomor Induk Siswa", required=True)
    nama = fields.Char(string="Nama", required=True)
    jenis_kelamin = fields.Selection(
        selection=[("laki_laki", "Laki-laki"), ("perempuan", "Perempuan")],
        string="Jenis Kelamin",
        required=True
    )
    tanggal_lahir = fields.Date(string="Tanggal Lahir")
    asal_sekolah = fields.Char(string="Asal Sekolah")
    alamat = fields.Text(string="Alamat")
    
    kota_asal = fields.Selection(
        selection=[("malang", "Malang"), ("luar_kota", "Luar Kota")],
        string="Kota Asal",
        required=True
    )
    
    tahun_kelahiran = fields.Char(
        string="Tahun Kelahiran", compute="_compute_tahun_kelahiran", store=True)

    @api.depends('tanggal_lahir')
    def _compute_tahun_kelahiran(self):
        for record in self:
            if record.tanggal_lahir:
                record.tahun_kelahiran = record.tanggal_lahir.strftime('%Y')
            else:
                record.tahun_kelahiran = ''
