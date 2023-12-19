from pathlib import Path

# Edit these variables to match the project
page_title = "Chemical structure gallery | ecoinvent 3.10"
project = "ecoinvent_chemical-structures"
dir_images = "images"
root_path = Path("/home/stew/code/gh/Stew-McD.github.io/")
assets_path = Path("assets")
template_html = root_path / "templates" / "gallery-template.html"

# Set the paths to the HTML and image directories
project_html = root_path / "projects" / project / f"gallery-{project}.html"
img_path = root_path / "assets" / "projects" / project / dir_images
assets_path = assets_path / "projects" / project / dir_images

# Get a list of all svg files in the base path
svg_filenames = list(img_path.glob("*.svg"))
svg_filenames.sort(reverse=True)
# Generate the JavaScript array of image paths
image_paths = ",\n".join(f'"../../assets/projects/{project}/images/{f.name}"' for f in svg_filenames)


# Read the original HTML file
with open(template_html, "r") as file:
    html = file.read()

# Replace the placeholder with the generated image paths
html = html.replace('IMAGE_PATH_LIST', image_paths).replace('PAGE_TITLE', page_title)

# Write the updated HTML back to the file
with open(project_html, "w") as file:
    file.write(html)

print(f"\n //// \n Updated html: \n{project_html} \n //// \n")