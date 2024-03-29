# Copyright 2016 Antiun Ingenieria S.L. - Javier Iniesta
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "MRP Sale Info",
    "summary": "Adds sale information to Manufacturing models",
    "version": "12.0.0.0.1",
    "category": "Manufacturing",
    "website": "https://www.gruporequiez.com",
    "author": "gflores",
    "license": "AGPL-3",
    "application": False,
    'installable': True,
    "depends": [
        "mrp",
        "sale_mrp",
        "sale_order_dates",
        "stock",
        "sale_stock",
    ],
    "data": [
        "views/mrp_production.xml",
        "views/mrp_workorder.xml",
    ]
}
