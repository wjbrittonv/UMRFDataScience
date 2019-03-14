# UMRFDataScience
This repository is for UMRF Data Science projects.

## Cloning the Repository
First, make sure you have git installed. On the linux subsystem, run the following commands:
* `sudo apt-get install git`
* Configure your account for contributing using your GitHub login information:
	* `git config --global user.name "YOUR_USERNAME"` sets your username
	* `git config --global user.email "your_email_address@example.com"` sets your email address

Now that everything is installed, you need to clone the repository and get the app running.
1. Change into the folder where you want the app to live (e.g. if you are using the linux subsystem and want the app to be on your desktop, you would
  type `cd /mnt/c/Users/[your username]/Desktop`).
2. Clone the repository using `sudo git clone https://github.com/laurarnichols/UMRFDataScience.git`.
3. Change into the cloned repository using `cd UMRFDataScience`.

## Contributing
1. Before you start a project, use `git pull origin` to get an up-to-date version of the code.
2. Then, create a new branch using `git checkout -b NAME-OF-BRANCH`. You can also switch to an existing branch
   using `git checkout NAME-OF-BRANCH`.
3. You can now make changes to files and git will track the changes. At any point, you can use `git status` to see what files you have changed.
4. Each time you change a file, create a commit:
	* Stage the file or folder using `git add FILE OR FOLDER`. 
	* Complete commit using `git commit -m "COMMENT TO DESCRIBE THE INTENTION OF THE COMMIT"`. 
	* Push the changes from your local clone to the origin (what you see online) using `git push origin NAME-OF-BRANCH`.
	* If you mistakely commit something, you can revert (undo) the last commit using `git revert HEAD`.
5. To merge your code, get online and submit a pull request from your branch to main.
6. Once the pull request is merged, the branch will be deleted, so to make new changes, start at 1.

### Useful commands
Here is a simple list of useful commands when contributing with git:
* `git pull origin` gets updates from the central copy
* `git checkout NAME-OF-BRANCH` changes to an existing branch
* `git checkout -b NAME-OF-BRANCH` creates a new branch and changes to it
* `git status` shows all files that have been changed or added to be committed
* `git add FILE OR FOLDER` stages changes to be committed
* `git commit -m "COMMENT TO DESCRIBE THE INTENTION OF THE COMMIT"` makes the change official on your local copy
* `git push origin NAME-OF-BRANCH` updates the central copy
* `git revert HEAD` undoes the last commit on a branch
* `git branch` lists the branches you have on your local copy; there will be a star by the branch your are currently on
* `git branch -d NAME-OF-BRANCH` will delete a given branch
* `git diff` shows the difference between local, unstaged changes and the official (pulled or committed) version
* `git checkout -- NAME-OF-FILE` deletes changes to a given file that have not been staged to commit
* `git checkout .` deletes all local changes in the repository that have not been added to the staging area
* `git clean -f` deletes untracked changes
* `git reset .` removes files from staging area before they have been committed
