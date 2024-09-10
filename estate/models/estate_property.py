from odoo import fields, models

class estate_property(models.Model):
    _name = 'estate.property'
    _description = 'Descrip estate.property'

    name = fields.Char(required=True, default="Nuevo")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Datetime()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Orientación',
        selection=[('norte', 'Norte'), ('sur', 'Sur'), ('este','Este'), ('oeste','Oeste')], required=True,
        help="Selecciona Orientación")
    state = fields.Selection(string='Estatus',
                            selection=[('nuevo','Nuevo'), ('oferta_recibida','Oferta Recibida'),('oferta_aceptada','Oferta Aceptada'), ('vendida','Vendida'), ('cancelada','Cancelada')],
                            required=True, help='Selecciona Estatus de Vivienda',default='nuevo')
    
