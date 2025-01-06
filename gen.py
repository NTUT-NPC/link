import csv, os, shutil, random

links_dir = 'docs'
colors = ['red', 'green', 'blue', 'orange', 'purple', 'pink', 'brown', 'ng_black', 'ng_blue', 'ng_green', 'ng_red']

gradient_colors = {
    'red': ['#5C2E2E', '#7A3B3B', '#9B4A4A', '#B05C5C', '#C76B6B'],
    'green': ['#2E4D2E', '#3B6A3B', '#4A8B4A', '#5CA05C', '#6FB76F'],
    'blue': ['#2E4B7A', '#3B6A9B', '#4A8BC4', '#5C9BC4', '#6FB3D1'],
    'orange': ['#7A4D2E', '#A65B3B', '#C46A4A', '#D78B5C', '#E7A76B'],
    'purple': ['#4B2E5C', '#6A3B7A', '#8B4A9B', '#A65CB0', '#B76BC4'],
    'pink': ['#5C2E4B', '#7A3B6A', '#9B4A8B', '#B05CA6', '#C76BB7'],
    'brown': ['#4E3B2E', '#6D4A3B', '#8B5C4A', '#A76B5C', '#C76B4A'],
    'ng_black': ['#000000'],
    'ng_blue': ['#2196f3'],
    'ng_green': ['#004d40'],
    'ng_red': ['#ff7f7f'],
}


for item in os.listdir(links_dir):
    item_path = os.path.join(links_dir, item)
    if os.path.isdir(item_path):
        shutil.rmtree(item_path)

for filename in os.listdir(links_dir):
    if filename.endswith('.csv'):
        title = os.path.splitext(filename)[0]
        output_dir = os.path.join(links_dir, title)

        os.makedirs(output_dir, exist_ok=True)

        links = ""
        selected_color = random.choice(colors)
        with open(os.path.join(links_dir, filename), mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                background_colors = gradient_colors[selected_color]
                bg_color = random.choice(background_colors)
                links += f'<a href="{row["URL"]}" style="background-color: {bg_color};">{row["Title"]}</a>\n'


        with open('template.html', 'r') as template_file:
            template = template_file.read()

        output_html = template.replace('{{links}}', links).replace('{{title}}', title)

        output_html_path = os.path.join(output_dir, 'index.html')
        with open(output_html_path, 'w') as output_file:
            output_file.write(output_html)

        print(f"HTML file generated successfully at {output_html_path}.")
