import markdown

# Read the README.md file
with open('README.md', 'r') as file:
    readme_content = file.read()

# Convert the markdown content to HTML
html_content = markdown.markdown(readme_content)

# Wrap the HTML content with a container div and link the CSS
with open("template.html", 'r') as f:
    html_with_css =  f.read().replace("HTML_CONTENT", html_content)


# Save the HTML content to a file
with open('output.html', 'w') as file:
    file.write(html_with_css)

print("Conversion complete! The HTML content is saved in 'output.html'.")
