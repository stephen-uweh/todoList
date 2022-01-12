from odoo import api, fields, models, tools, http, release, registry
from odoo.http import request

class Todo(models.Model):
    _name = "todo.item",

    due = fields.Char('Due date', required=True)
    state = fields.Char('State of Todo', required=True, default="pending")
    task = fields.Char('Task', required=True)

