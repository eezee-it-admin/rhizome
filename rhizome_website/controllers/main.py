# Copyright 2021      Eezee-IT (<http://www.eezee-it.com>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import http


class WebsiteBlog(http.Controller):

    @http.route([
        '/cf654f212c11e103eeab302863a0bfa5.txt',
        '/aae183afcc141ccf3312f1203af002a5.txt',
        '/e0f0b0de55adce5b203da8c6021510a0.txt',
    ], type='http', auth="public", website=True)
    def mailjet_pages(self, sitemap=False):
        return ""
