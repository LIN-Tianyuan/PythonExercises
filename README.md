# Python Exercises submitting methods

## 1. Github account + Fork repository
Log in to GitHub and visit the repository `https://github.com/LIN-Tianyuan/PythonExercises.git`.

Click the **Fork** button in the upper-right corner, and GitHub will automatically copy the repository to your account, forming a **separate copy**, for example:

`https://github.com/student_username/python-exercises`.

Clone your own Fork locally

## 2. Open a terminal (or Git Bash) on your own computer
```bash
git clone https://github.com/student_username/python-exercises.git
cd python-exercises
```
## 3. Create your own homework directory
```bash
mkdir -p submissions/student_zhangsan/exercise1.py
cp exercises/week_1/exercise_1.py submissions/student_zhangsan/exercise1/
# Then finish the exercises.
```
## 4. Submit and push
```bash
git add .
git commit -m "Alex exercise 1"
git push origin main  # Push to your own GitHub repository
```
## 5. Submit Pull Request
Go back to the GitHub page, go to the Fork repository, click **Pull Request** (PR for short), and then:

- Select `LINTianyuan/python-exercises` as the target repository.
- Select `student_username/python-exercises` as the source repository.
- Fill in the PR title (e.g., `Student Alex submits exercise 1 assignment`).
- Click **Create Pull Request**.

## 6. Synchronization of latest homeworks
### 6.1 Add an upstream repository (only need to do this once)
Go to your local repository directory
```bash
cd python-exercises
```
Add the teacher's repository address as “upstream”
```bash
git remote add upstream https://github.com/LIN-Tianyuan/PythonExercises.git
```
Check if it was added successfully
```bash
git remote -v
```
The output should be similar:
```bash
origin    https://github.com/Your GitHub username/python-exercises.git
upstream  https://github.com/LIN-Tianyuan/python-exercises.git
```
### 6.2 Update your repository each time your teacher posts a new assignment
```bash
git fetch upstream
git merge upstream/master
git push origin main
```
fetch upstream: get the latest update from your teacher

merge upstream/main: merge into your local code

push origin main: sync to your own GitHub repository