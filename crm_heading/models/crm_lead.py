# -*- encoding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    heading = fields.Many2one(comodel_name='crm.heading')

    def _lead_create_contact(self, cr, uid, lead, name, is_company,
                             parent_id=False, context=None):
        """Propagate heading to created partner.
        """
        partner_id = super(CrmLead, self)._lead_create_contact(
            cr, uid, lead, name, is_company, parent_id=parent_id,
            context=context)
        self.pool['res.partner'].write(
            cr, uid, partner_id, {'heading': lead.heading.id},
            context=context)
        return partner_id
