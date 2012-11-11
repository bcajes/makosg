import unittest


class MakoMessageTests(unittest.TestCase):

    def _callUT(self, addr_from, subject, context=None, text="", temp_path=None,
                temp_filename=None):
        from makosg import MakoMessage
        return MakoMessage(addr_from, subject, context, text, temp_path,
                           temp_filename)

    def test_should_render_basic_txt_template(self):
        message = self._callUT('test@example.com', 'Hello ${name}',
                               context={'name': 'bob'},
                               text="How's it going ${name}?",
                               )
        self.assertTrue('bob' in message.subject, message.subject)
        self.assertTrue('bob' in message.text, message.text)
        self.assertTrue(not message.html, message.html)

    def test_should_render_html_file(self):
        message = self._callUT('test@example.com', 'Hello ${name}',
                               context={'name': 'jim'},
                               text="",
                               temp_path='./makosg/test_templates/',
                               temp_filename='example.mako')
        self.assertTrue('<p>jim</p>' in message.html, message.html)
        self.assertTrue(not message.text, message.text)

    def test_should_render_rich_html_message(self):
        message = self._callUT('test@example.com', 'Hello ${name}',
                               context={'name': 'Brian', 'fruits':
                                     ['apple', 'pear', 'berry']},
                               text="My favorite fruit is an ${fruits[0]}",
                               temp_path='./makosg/test_templates/',
                               temp_filename='example2.mako')
        self.assertTrue('<li>apple</li>' in message.html and \
                        '<li>pear</li>' in message.html and \
                        '<li>berry</li>' in message.html and \
                        '<p>Hello Brian</p>' in message.html, message.html)
        self.assertTrue('apple' in message.text, message.text)
        self.assertTrue('Brian' in message.subject, message.subject)
    
    def test_should_raise_template_path_no_path_error(self):
        from makosg import TemplatePathError
        self.assertRaises(TemplatePathError,
                          self._callUT, *['test@example.com', 'Hello ${name}'],
                                         **{'context': {'name': 'bob'},
                                         'text': "How's it going ${name}?",
                                         'temp_path': None,
                                         'temp_filename': "example.mako"
                                         }
                          )
    def test_should_raise_template_path_no_file_error(self):
        from makosg import TemplateFilenameError
        self.assertRaises(TemplateFilenameError,
                          self._callUT, *['test@example.com', 'Hello ${name}'],
                                         **{'context': {'name': 'bob'},
                                         'text': "How's it going ${name}?",
                                         'temp_path': './test_templates/',
                                         }
                          )
        
