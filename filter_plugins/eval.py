# Evaluate a variable as a jinja2 expression.

from jinja2 import contextfilter, Template

class FilterModule(object):
    '''
    Custom filter for evaluating a variable
    as a jinja2 expression.
    '''

    def filters(self):
      return {
        'eval': self.do_eval
      }

    @contextfilter
    def do_eval(self, context, value):
      tpl = '{{ ' + value = ' }}'
      return Template(tpl).render(context)
