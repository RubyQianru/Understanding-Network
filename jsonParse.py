import json
import os

def transform_repo_data(repos):
    transformed_repos = []
    for repo in repos:
        transformed_repo = {
            "name": repo["name"],
            "full_name": repo["full_name"],
            "description": repo["description"],
            "html_url": repo["html_url"],
            "fork": repo["fork"],
            "created_at": repo["created_at"],
            "updated_at": repo["updated_at"]
        }
        transformed_repos.append(transformed_repo)
    return transformed_repos

# Parse the JSON response
with open('output.txt', 'r') as file:
    response = file.read()

repos = json.loads(response)

# Transform the data
transformed_data = transform_repo_data(repos)

# Write the transformed data to a new file
output_file = 'transformed_repos.json'
with open(output_file, 'w') as file:
    json.dump(transformed_data, file, indent=2)

print(f"Transformed data has been saved to {output_file}")