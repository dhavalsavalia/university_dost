import json

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def mathjax_scripts():

    mathjax_js_url = '//cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js'

    mathjax_config_file = "TeX-AMS_CHTML"
    url = "{}?config={}".format(mathjax_js_url, mathjax_config_file)
    load_script_tag = '''<script type="text/javascript" async
      src="{}">
    </script>'''.format(url)

    mathjax_config_data = {
                            "tex2jax": {
                                "inlineMath": [
                                    ['$','$'], 
                                    ['\\(','\\)']
                                ]
                            } 
                        }

    config_script_tag = ''
    if mathjax_config_data:
        config_script_tag = '<script type="text/x-mathjax-config">'
        config_script_tag += 'MathJax.Hub.Config('
        config_script_tag += json.dumps(mathjax_config_data)
        config_script_tag += ');'
        config_script_tag += '</script>'

    return mark_safe(load_script_tag + config_script_tag)
