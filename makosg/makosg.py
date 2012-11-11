from sendgrid.message import Message
from mako.template import Template
from mako.lookup import TemplateLookup


class MakoMessage(Message):

    def __init__(self, addr_from, subject, context=None, text="",
                 temp_path=None, temp_filename=None):
        context = context or {}
        html = self.render_template_output(context, temp_path, temp_filename)
        subject = self._render(subject, context)
        text = self._render(text, context)
        super(MakoMessage, self).__init__(addr_from, subject, text, html)
        
    def render_template_output(self, context, temp_path, temp_filename):
        if temp_path and temp_filename:
            lookup = TemplateLookup([temp_path])
            template = lookup.get_template(temp_filename)
            return template.render(**context)            
        elif not temp_path and temp_filename:
            raise TemplatePathError('Missing template path')
        elif not temp_filename and temp_path:
            raise TemplateFilenameError('Missing template filename')
        else:
            return ""  # no template specified so just return an empty string

    def _render(self, temp_data, context):
        template = Template(temp_data)
        return template.render(**context)


class TemplatePathError(ValueError):
    pass


class TemplateFilenameError(ValueError):
    pass
