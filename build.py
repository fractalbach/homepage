#!/usr/bin/env python3

from string import Template

template_filepath = "templates/main.html.template"
template = None

content_directory = 'content'
content_filenames = ['index', 'projects', 'contact']


with open(template_filepath, 'r') as f:
    template = Template(f.read())


for filename in content_filenames:
    
    input_filepath = content_directory + '/' + filename
    output_filepath = filename + '.html'
    content = ''

    with open(input_filepath, 'r') as f:
        content = f.read()

    output = template.substitute({
        'SUBTITLE': filename.capitalize(),
        'MAIN': content,
    })

    with open(output_filepath, 'w+') as f:
        f.write(output)
