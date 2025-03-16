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
## 3. Modify `exercise.py` and submit the job
```bash
git add exercises/week_1/exercise_1.py
git commit -m "Completion of exercise 1"
git push origin main  # Push to your own GitHub repository
```
## 4. Submit Pull Request
Go back to the GitHub page, go to the Fork repository, click **Pull Request** (PR for short), and then:

- Select `LINTianyuan/python-exercises` as the target repository.
- Select `student_username/python-exercises` as the source repository.
- Fill in the PR title (e.g., `Student Zhang San submits exercise 1 assignment`).
- Click **Create Pull Request**.

