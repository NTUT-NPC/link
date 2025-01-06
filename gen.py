import csv, os, shutil

links_dir = 'docs'

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

        with open(os.path.join(links_dir, filename), mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                links += f'<a href="{row["URL"]}">{row["Title"]}</a>\n'

        with open('template.html', 'r') as template_file:
            template = template_file.read()

        output_html = template.replace('{{links}}', links).replace('{{title}}', title)

        output_html_path = os.path.join(output_dir, 'index.html')
        with open(output_html_path, 'w') as output_file:
            output_file.write(output_html)

        print(f"HTML file generated successfully at {output_html_path}.")
