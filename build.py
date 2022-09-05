#!/usr/bin/env python3

from string import Template

template_filepath = "templates/main.html.template"
template = None

content_directory = 'content'

all_pages = [
	{
		'filename': 'index',
		'TITLE': 'Home',
		'DESCRIPTION': "Chris Achenbach's Homepage!",
	},
	{
		'filename': 'projects',
		'TITLE': 'Projects',
		'DESCRIPTION': "Chris Achenbach's awesome project page!",
	},
	{
		'filename': 'contact',
		'TITLE': 'Contact',
		'DESCRIPTION': "Contact Me!",
	}
]
	



with open(template_filepath, 'r') as f:
    template = Template(f.read())


for page in all_pages:
    
    filename = page['filename']
    input_filepath = content_directory + '/' + filename
    output_filepath = filename + '.html'
    content = ''

    with open(input_filepath, 'r') as f:
        content = f.read()

    output = template.substitute({
        'TITLE': f"Achenbach - {page['TITLE']}",
    	'DESCRIPTION': page['DESCRIPTION'],
        'MAIN': content,
    })

    with open(output_filepath, 'w+') as f:
        f.write(output)
