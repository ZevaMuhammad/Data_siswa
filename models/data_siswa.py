from odoo import models, fields, api
from odoo.exceptions import ValidationError
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
    asals = fields.Many2one("sekolah.asal", string="Asal Sekolah", store=True)
    alamat = fields.Text(string="Alamat")
    asal = fields.Many2one("kota.asal", string="Kota Asal", store=True)
    umur = fields.Integer(string="Umur", compute="_compute_umur", store=True)

    @api.depends('tanggal_lahir')
    def _compute_umur(self):
        for record in self:
            if record.tanggal_lahir:
                today = datetime.today()
                birth_date = fields.Date.from_string(record.tanggal_lahir)
                age = today.year - birth_date.year
                if (today.month, today.day) < (birth_date.month, birth_date.day):
                    age -= 1
                record.umur = age
            else:
                record.umur = 0 
    
    @api.constrains('tanggal_lahir')
    def _check_tanggal_lahir(self):
        for record in self:
            if record.tanggal_lahir and record.tanggal_lahir > fields.Date.today():
                raise ValidationError("Tanggal lahir tidak boleh di masa depan!")