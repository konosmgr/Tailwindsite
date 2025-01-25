def generate_spectrum_html():
    colors = ['red', 'orange', 'amber', 'yellow', 'lime', 'green', 'emerald', 'teal', 'cyan', 'sky', 'blue', 'indigo', 'violet', 'purple', 'fuchsia', 'pink', 'rose', 'stone', 'neutral', 'zinc', 'gray', 'slate']
    shades = ['950', '900', '800', '700', '600', '500', '400', '300', '200', '100', '50']
    
    html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="./dist/output.css" rel="stylesheet">
</head>
<body class="bg-gray-100">
    <main class="container mx-auto p-4">
        <div class="grid grid-flow-col auto-cols-fr gap-1">'''

    for color in colors:
        html += f'\n            <div class="flex flex-col gap-1">'
        for shade in shades:
            html += f'\n                <div class="h-16 text-transparent flex items-center justify-center hover:text-white/50 bg-{color}-{shade}">{shade}</div>'
        html += '\n            </div>'

    html += '''
        </div>
    </main>
</body>
</html>'''
    
    with open('full-spectrum.html', 'w') as f:
        f.write(html)

generate_spectrum_html()
