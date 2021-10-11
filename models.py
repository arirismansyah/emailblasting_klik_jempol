from app import db
from datetime import datetime


class Pendidikan(db.Model):
    id_pendidikan = db.Column(db.Integer, primary_key=True)
    tingkat_pendidikan = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Pendidikan {}>'.format(self.tingkat_pendidikan)


class Pekerjaan(db.Model):
    id_pekerjaan = db.Column(db.Integer, primary_key=True)
    jenis_pekerjaan = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Pekerjaan {}>'.format(self.jenis_pekerjaan)


class Prov(db.Model):
    kode_prov = db.Column(db.Integer, primary_key=True)
    nama_prov = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return 'Provinsi {}'.format(self.nama_prov)


class Kabkot(db.Model):
    id_kabkot = db.Column(db.Integer, primary_key=True)
    kode_prov = db.Column(db.Integer, db.ForeignKey(
        'prov.kode_prov'), nullable=False)
    nama_kabkot = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Kabupaten/Kota {}>'.format(self.nama_kabkot)


class Status(db.Model):
    id_status = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Status {}>'.format(self.nama_kabkot)


class Customer(db.Model):
    id_customer = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(200), nullable=False)
    jenis_kelamin = db.Column(db.String(1), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(200), nullable=True, unique=True)
    tempat_lahir = db.Column(db.String(200), nullable=True)
    tanggal_lahir = db.Column(db.Date, nullable=True)
    pendidikan = db.Column(db.Integer, db.ForeignKey(
        'pendidikan.id_pendidikan'), nullable=True)
    pekerjaan = db.Column(db.String(200), nullable=True)
    jenis_pekerjaan = db.Column(db.Integer, db.ForeignKey(
        'pekerjaan.id_pekerjaan'), nullable=True)
    instansi = db.Column(db.String(200), nullable=True)
    alamat_domisili = db.Column(db.Text, nullable=True)
    prov_domisili = db.Column(db.Integer, db.ForeignKey(
        'prov.kode_prov'), nullable=True)
    kab_domisili = db.Column(db.Integer, db.ForeignKey(
        'kabkot.id_kabkot'), nullable=True)

    # create string
    def __repr__(self):
        return '<Customer {}>'.format(self.nama)


class Template(db.Model):
    id_template = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    nama_produk = db.Column(db.String(200), nullable=False)
    lampiran = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Integer, db.ForeignKey(
        'status.id_status'), nullable=False, default=0)

    def __repr__(self):
        return '<Template {}>'.format(self.subject)


class Log(db.Model):
    id_log = db.Column(db.Integer, primary_key=True)
    template_email = db.Column(
        db.Integer, db.ForeignKey('template.id_template'))
    customer = db.Column(db.Integer, db.ForeignKey('customer.id_customer'))
    send_at = db.Column(db.DateTime, default=datetime.now)
