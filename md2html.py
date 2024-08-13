import markdown
import git

# Function to get the current git branch, latest commit hash, repo name, and remote URL using GitPython
def get_git_info(repo_path='.'):
    repo = git.Repo(repo_path)
    branch_name = repo.active_branch.name
    commit_hash = repo.head.commit.hexsha
    remote_url = repo.remotes.origin.url
    repo_name = remote_url.split('/')[-1].replace('.git', '')  # Extract repo name from URL
    return branch_name, commit_hash, repo_name, remote_url

# Get the branch, commit hash, repo name, and remote URL
branch_name, commit_hash, repo_name, remote_url = get_git_info()

# Read the README.md file
with open('README.md', 'r') as file:
    readme_content = file.read()

# Convert the markdown content to HTML
html_content = markdown.markdown(readme_content)

# Read the HTML template and insert content
with open("template.html", 'r') as f:
    html_with_css = f.read().replace("HTML_CONTENT", html_content)

# Insert branch, commit, repo name, and remote URL information into the HTML
html_with_css = (html_with_css
                 .replace("BRANCH_NAME", branch_name)
                 .replace("COMMIT_HASH", commit_hash)
                 .replace("REPO_NAME", repo_name)
                 .replace("REMOTE_URL", remote_url))

# Save the HTML content to a file
with open('output.html', 'w') as file:
    file.write(html_with_css)

print(f"Conversion complete! The HTML content is saved in 'output.html'.\nRepo: {repo_name}, Branch: {branch_name}, Commit: {commit_hash}, Remote: {remote_url}")
