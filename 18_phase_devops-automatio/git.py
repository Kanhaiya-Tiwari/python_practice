# Clone Repository
from git import Repo

Repo.clone_from(
    "https://github.com/user/project.git",
    "./project"
)

print("Repository cloned")

# Open Existing Repository
from git import Repo

repo = Repo("./project")

# Add Files
repo.git.add(all=True)

# Commit Changes
repo.index.commit(
    "Updated deployment script"
)
# Push Changes
origin = repo.remote(name="origin")

origin.push()

# List Branches
for branch in repo.branches:

    print(branch)

# Create Branch
repo.git.checkout(
    "-b",
    "feature-login"
)