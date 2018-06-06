import html

def make_element(name ,value, **attrs):
    keyvals = ['%s = "%s"' % item for item in attrs.items()]
    attrs_str = ''.join(keyvals)
    elememt = '<{name} {attrs} > {value} </{name}> '.format(
                name = name,
                attrs = attrs_str,
                value = html.escape(value))
    return elememt



print (make_element('item','Albatross',size='large' , quantity = 6))



print(keyvals)
