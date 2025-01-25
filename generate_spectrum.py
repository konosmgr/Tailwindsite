#!/usr/bin/env python3

"""
This Python script generates an HTML file with multiple columns of colors.
Each column corresponds to a color, and each column includes rows of
shades (from 0 to 950 in steps of 50). The top box in each column is rounded.

Requirements:
- Minimal spacing.
- The top box in each column is rounded.
- Each color is displayed in its own column.
- Each row in a column represents a different shade.
- Uses Tailwind via CDN for styling.

Usage:
    python generate_shade_columns.py
"""

def generate_shade_columns_html(output_filename="shade_columns.html"):
    # Define the colors you want to generate columns for.
    colors = [
        "red", "pink", "rose", "fuchsia", "orange", "amber", "yellow",
        "lime", "green", "emerald", "teal", "cyan", "sky", "blue",
        "indigo", "violet", "purple", "stone", "neutral", "zinc",
        "gray", "slate"
    ]

    # Define the range of shades from 0 to 950 in increments of 50.
    shades = list(range(0, 1000, 50))  # [0, 50, 100, ..., 950]

    # Start building the HTML.
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Color Columns with Shades</title>
    <!-- Tailwind CSS CDN -->
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@3.3.2/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100 min-h-screen flex items-center justify-center p-4">
    <main class="grid grid-flow-col auto-cols-fr gap-1">
"""

    for color in colors:
        # For each color, create a column.
        html += f'        <div class="flex flex-col gap-1">\n'
        # Column title
        html += f'            <div class="text-center text-sm font-bold mb-1 capitalize">{color}</div>\n'

        for idx, shade in enumerate(shades):
            # The first box in each column gets rounded top corners.
            extra_classes = ""
            if idx == 0:
                extra_classes = "rounded-t-lg"

            # Construct the Tailwind shade class.
            # If shade == 0, let's substitute it with 50 to avoid invalid classes
            # unless your Tailwind config has an actual '0' shade.
            tailwind_shade = shade if shade != 0 else 50

            html += (
                f'            <div class="h-10 w-24 flex items-center justify-center '
                f'text-sm text-transparent hover:text-white/70 bg-{color}-{tailwind_shade} {extra_classes}">'
                f'{shade}</div>\n'
            )

        html += "        </div>\n"

    # Close out the HTML
    html += """
    </main>
</body>
</html>
"""

    # Write to file
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Generated {output_filename}")


if __name__ == "__main__":
    generate_shade_columns_html()
