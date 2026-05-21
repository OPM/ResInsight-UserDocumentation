{{ objname | escape | underline }}

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}
   :show-inheritance:

   {% set inherited = inherited_members if inherited_members is defined else [] %}
   {# Drop every private/dunder member (name starts with '_'): constructors,
      Python internals like __doc__/__module__, etc.
      Value/ValueArray on PdmObjectBase are mutually-recursive typing
      aliases with no leading underscore; autodoc recurses through them
      without terminating, so exclude them by name. #}
   {% set excluded = ['Value', 'ValueArray'] %}
   {% set ns = namespace(methods=[], attributes=[]) %}
   {% for item in methods if item not in inherited and not item.startswith('_') and item not in excluded %}
   {% set ns.methods = ns.methods + [item] %}
   {% endfor %}
   {% for item in attributes if item not in inherited and not item.startswith('_') and item not in excluded %}
   {% set ns.attributes = ns.attributes + [item] %}
   {% endfor %}

   {% if ns.methods %}
   .. rubric:: Methods Summary

   .. autosummary::
   {% for item in ns.methods %}
      ~{{ name }}.{{ item }}
   {%- endfor %}
   {% endif %}

   {% if ns.attributes %}
   .. rubric:: Attributes Summary

   .. autosummary::
   {% for item in ns.attributes %}
      ~{{ name }}.{{ item }}
   {%- endfor %}
   {% endif %}

   {% if ns.methods %}
   .. rubric:: Methods Documentation

   {% for item in ns.methods %}
   .. automethod:: {{ item }}
   {% endfor %}
   {% endif %}

   {% if ns.attributes %}
   .. rubric:: Attributes Documentation

   {% for item in ns.attributes %}
   .. autoattribute:: {{ item }}
   {% endfor %}
   {% endif %}
