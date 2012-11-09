from sendgrid.message import Message
from mako.template import Template
from mako.lookup import TemplateLookup


class MakoMessage(Message):

    def __init__(self, addr_from, subject, vars={}, text="",
                 temp_path=None, temp_filename=None):
        html = self.render_template_output(vars, temp_path, temp_filename)
        subject = self._render(subject, vars)
        text = self._render(text, vars)
        super(MakoMessage, self).__init__(addr_from, subject, text, html)
        
    def render_template_output(self, vars, temp_path, temp_filename):
        if temp_path and temp_filename:
            lookup = TemplateLookup([temp_path])
            template = lookup.get_template(temp_filename)
            return template.render(**vars)            
        return ""

    def _render(self, temp_data, vars):
        template = Template(temp_data)
        return template.render(**vars)
