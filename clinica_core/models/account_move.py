from odoo import api, fields, models
from .amount_to_text import to_word

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def format_amount(self, monto, currency=False, lang=False):
        if not monto:
            monto = 0
        if not lang:
            lang_str = self._context.get('lang')
        else:
            lang_str = lang
        if not currency:
            currency_id = self.env.company.currency_id
        else:
            currency_id = currency
        lang_id = self.env['res.lang'].search([('code', '=', lang_str)])

        if lang_id and currency_id:
            fmt = "%.{0}f".format(currency_id.decimal_places)
            return lang_id.format(fmt, monto, grouping=True)
        else:
            return '{:.6f}'.format(monto)

    @api.model
    def numero_a_letra(self, numero):
        return to_word(numero)

    def amount_to_text(self, amount,a=False):
        convert_amount_in_words = self.numero_a_letra(amount)
        return convert_amount_in_words

    def format_monto(self,monto):
        return self.format_amount(monto,currency=self.currency_id)

    def action_print_pdf(self):
        self.ensure_one()
        return self.env.ref('clinica_core.factura_report_action').report_action(self.id)