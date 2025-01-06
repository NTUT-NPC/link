
# 名子還沒想好
[![Generate HTML](https://github.com/NTUT-NPC/link/actions/workflows/gen.yml/badge.svg?branch=main)](https://github.com/NTUT-NPC/link/actions/workflows/gen.yml)
[![pages-build-deployment](https://github.com/NTUT-NPC/link/actions/workflows/pages/pages-build-deployment/badge.svg?branch=main)](https://github.com/NTUT-NPC/link/actions/workflows/pages/pages-build-deployment)

This project allows you to create a customizable landing page for your links, similar to Linktree. By generating an HTML template from a CSV file, you can easily manage and display your links in a visually appealing way. The project utilizes GitHub Actions to automate the generation of HTML files whenever changes are made to the CSV files.

## Screenshots
![image](https://github.com/user-attachments/assets/6d7536da-cc92-48aa-a068-53b0362914ed)


## Project Structure

Here's an overview of the project structure:

```
link
├── docs
│   ├── CNAME
│   ├── index.html
│   ├── link1
│   │   └── index.html
│   ├── link1.csv
│   ├── link2
│   │   └── index.html
│   └── link2.csv
│       ...
├── gen.py
└── template.html
```

### Directory and File Descriptions

- **docs/**: Contains all the generated documentation and HTML files.
  - **CNAME**: Custom domain name for the GitHub Pages site (if applicable).
  - **index.html**: The main landing page generated from the CSV file.
  - **link1/**: A subdirectory for a specific project or group, containing its own index.html.
    - **index.html**: The landing page for "link1".
  - **link1.csv**: CSV file containing links for "link1".

- **gen.py**: A Python script that processes the CSV files and generates the corresponding HTML files.

- **template.html**: The base HTML template used for generating the landing pages.

## Getting Started

### Simple Setup

1. **Fork the Repository:**

   Click the "Fork" button on the top right of the repository page to create your own copy of the project.

2. **Enable GitHub Actions:**

   Go to the "Actions" tab in your forked repository and enable GitHub Actions. This will allow the automated workflow to run.

3. **Enable GitHub Pages:**

   Go to the "Settings" tab, scroll down to the "Pages" section, and select the branch you want to use for GitHub Pages (usually `main`). Save the settings.

4. **Add Your Own CSV File:**

   In the `docs/` directory, create your own CSV file (e.g., `my_links.csv`) with the following format:

   ```
   Title,URL
   ```

   Example:

   ```
   Title,URL
   Google,https://www.google.com
   GitHub,https://github.com
   ```

5. **Push Your Changes:**

   After adding your CSV file, commit your changes and push them to your GitHub repository. The GitHub Actions workflow will automatically run and generate the corresponding HTML files.

### Access Your Generated Links

Once the workflow has completed, you can access your generated landing page at:

```
https://<your-username>.github.io/<repository-name>/<link>
```

Replace `<your-username>` with your GitHub username, `<repository-name>` with the name of your forked repository, and `<link>` with the filename of your CSV (without the `.csv` extension).

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## Acknowledgments

- Inspired by Linktree and similar services.
