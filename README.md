# Versioning Exam

## Git WorkTrees - Manage Multiple Work Trees

It allows you to checkout on multiple work trees at once.

Let say that you're working on a new feature that is not fully working yet and that there's a **hotfix** that need to be done on production.
You have a couple of options that are available, **commit** and **stash** are some of the most used. But then you will have to remember where you were once you come back on that feature.

Where is **worktrees** allows you to checkout (**git worktree add**) of multiple branches and show them as directories where you can go and make the changes that are needed, in our case to deal with the hotfix, commit, push go back to the root directory, delete (**git worktree remove**) the folder that have been created with the worktree and continue on your feature.
