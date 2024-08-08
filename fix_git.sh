git filter-branch --force --index-filter \
'git rm --cached --ignore-unmatch combine_data.ipynb' \
--prune-empty --tag-name-filter cat -- --all
