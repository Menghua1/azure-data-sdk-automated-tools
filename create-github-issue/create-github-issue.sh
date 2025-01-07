# Opening new issue
create_new_issue="https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/issues"

# Construct the JSON payload for the new issue
json="{
  \"title\": \"$ISSUE_TITLE\",
  \"body\": \"$file_content\",
  \"labels\": [\"bug\"]
}"

# Send a POST request to create the new issue
response=$(curl -s -X POST \
  -H "Authorization: token $GITHUB_PAT" \
  -H "Content-Type: application/json" \
  -d "$json" "$create_new_issue")

# Print the response from GitHub API
echo "Response from GitHub API:"
echo "$response"
