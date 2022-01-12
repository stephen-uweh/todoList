# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import base64
import datetime
import json
import os
import logging
import re
import requests
import werkzeug.urls
import werkzeug.utils
import werkzeug.wrappers

from itertools import islice
from lxml import etree
from textwrap import shorten
from xml.etree import ElementTree as ET

import odoo

from odoo import http, models, fields, _
from odoo.http import request, Controller
from odoo.osv import expression
from odoo.tools import OrderedSet, escape_psql, html_escape as escape
from odoo import api, fields, models, tools, http, release, registry


class Todo(Controller):

    @http.route('/todo', type='json')
    def all(self):
        todos = self.env[todo.item].sorted(reverse=False)
        return json.dumps(todos)


    @http.route('/todo/<int:todo>',type='json')
    def single_todo(self, **id):
        todo = self.env['todo.item'].search(['id' = id])
        return json.dumps(todo)


    @http.route('/todo/create', type='http', methods=['POST'])
    def create_todo(self, **post):
        vals = {
            'due' = post['due'],
            'task' = post['task']
        }
        self.env['todo.item'].create(vals)
        output = {
            results:{
                'code': 200,
                'message': 'OK'
            }
        }
        return json.dumps(output)


    @http.route('/todo/<int:todo>', type='http')
    def update_todo(self, **kwargs):
        todo = self.env['todo.item'].search[('id' = kwargs.id)]
        vals = {}
        if kwargs.get('due'):
            vals {'due' = kwargs['due']}
        if kwargs.get('state'):
            vals {'state' = kwargs['state']}
        if kwargs.get('task'):
            vals {'task' = kwargs['task']}
        self.todo.write(vals)
        output = {
            results:{
                'code': 200,
                'message': 'OK'
            }
        }
        return json.dumps(output)


    @http.route('/todo/<int:todo>/delete', type='http')
    def delete_todo(self, **id):
        self.env['todo.item'].unlink(id)
        output = {
            results:{
                'code': 200,
                'message': 'OK'
            }
        }
        return json.dumps(output)
