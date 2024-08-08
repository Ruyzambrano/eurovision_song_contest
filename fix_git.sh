git filter-branch --force --index-filter \
'git rm --cached --ignore-unmatch combined_visualisations.ipynb' \
--prune-empty --tag-name-filter cat -- --all
