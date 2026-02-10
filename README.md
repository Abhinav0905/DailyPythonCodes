# 🤖 Daily Python Programs Generator

An automated system that generates 5 unique Python programs every day with comprehensive inline comments and automatically commits them to GitHub.

## 📋 Features

- ✅ Generates 5 different Python programs daily
- ✅ Each program includes detailed inline comments explaining the code
- ✅ Fully automated - runs without manual intervention
- ✅ Scheduled to run every night at 11:00 PM UTC
- ✅ Automatically commits and pushes to GitHub
- ✅ Organized by date in `programs/YYYY-MM-DD/` folders
- ✅ 15+ different program templates including:
  - Fibonacci sequence generator
  - Palindrome checker
  - Prime number finder
  - Word frequency counter
  - Temperature converter
  - Sorting algorithms
  - Binary search
  - And more!

## 🚀 Setup Instructions

### 1. Push to GitHub

First, create a GitHub repository and push this code:

```bash
# If you haven't set up the remote yet
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Add all files
git add .

# Commit the initial setup
git commit -m "Initial setup: Daily Python program generator"

# Push to GitHub
git push -u origin main
```

> **Note**: Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and repository name.

### 2. Enable GitHub Actions

1. Go to your repository on GitHub
2. Click on the **"Actions"** tab
3. If prompted, click **"I understand my workflows, go ahead and enable them"**

### 3. Set Workflow Permissions

To allow the GitHub Action to commit and push changes:

1. Go to **Settings** → **Actions** → **General**
2. Scroll down to **"Workflow permissions"**
3. Select **"Read and write permissions"**
4. Check **"Allow GitHub Actions to create and approve pull requests"**
5. Click **"Save"**

### 4. Adjust Schedule (Optional)

The workflow runs at 11:00 PM UTC by default. To change the time:

1. Open `.github/workflows/daily_programs.yml`
2. Find the `cron` line:
   ```yaml
   - cron: '0 23 * * *'  # minute hour day month day-of-week
   ```
3. Modify it to your preferred time:
   - `'0 0 * * *'` → Midnight UTC
   - `'0 12 * * *'` → Noon UTC
   - `'30 20 * * *'` → 8:30 PM UTC

## 🧪 Manual Testing

You can manually trigger the workflow to test it:

1. Go to the **"Actions"** tab on GitHub
2. Click on **"Daily Python Programs Generator"** workflow
3. Click **"Run workflow"** button
4. Select the branch (usually `main`)
5. Click **"Run workflow"**

Or run locally:

```bash
python generate_programs.py
```

## 📁 Project Structure

```
dailyFivequestionsPython/
├── .github/
│   └── workflows/
│       └── daily_programs.yml    # GitHub Actions workflow
├── programs/                     # Generated programs (auto-created)
│   └── YYYY-MM-DD/              # Date-based folders
│       ├── YYYYMMDD_01_program_name.py
│       ├── YYYYMMDD_02_program_name.py
│       └── ...
├── generate_programs.py         # Main generator script
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🔧 How It Works

1. **Scheduled Trigger**: GitHub Actions runs the workflow every night at 11 PM UTC
2. **Environment Setup**: Sets up Python 3.11 environment
3. **Program Generation**: Runs `generate_programs.py` which:
   - Creates a date-based directory
   - Randomly selects 5 program templates
   - Generates files with inline comments
   - Saves them with timestamped names
4. **Git Commit**: Automatically commits the new programs
5. **Push to GitHub**: Pushes changes to the repository

## 📝 Program Templates

The generator includes templates for:

- **Fibonacci Generator** - Generate Fibonacci sequences
- **Palindrome Checker** - Check if strings are palindromes
- **Prime Numbers** - Find and verify prime numbers
- **Word Frequency Counter** - Analyze word frequencies in text
- **Temperature Converter** - Convert between temperature scales
- **List Operations** - Find max/min in lists
- **String Reverser** - Reverse strings and word order
- **Factorial Calculator** - Calculate factorials iteratively and recursively
- **List Comprehensions** - Examples of Python list comprehensions
- **Dictionary Operations** - Merge, invert, and filter dictionaries
- **File Statistics** - Count lines, words, and characters
- **Sorting Algorithms** - Bubble sort and selection sort
- **Number Guessing Game** - Interactive number guessing
- **Student Management** - OOP example with student class
- **Binary Search** - Iterative and recursive implementations

## 🎯 Customization

### Add More Program Templates

Edit `generate_programs.py` and add new templates to the `PROGRAM_TEMPLATES` list:

```python
{
    "name": "your_program_name",
    "code": '''# Your Python code here
def your_function():
    # Add inline comments
    pass
'''
}
```

### Change Number of Daily Programs

Modify the selection in `generate_daily_programs()` function:

```python
# Change 5 to your desired number
shuffled_templates = random.sample(PROGRAM_TEMPLATES, 5)
```

## 🐛 Troubleshooting

### Programs aren't being committed

- Check workflow permissions in repository settings
- Ensure the workflow has "Read and write permissions"
- Check the Actions tab for error logs

### Workflow isn't running

- Verify the workflow file is in `.github/workflows/` directory
- Check that GitHub Actions is enabled for your repository
- The first scheduled run happens after the workflow is added to the default branch

### Time zone issues

- GitHub Actions uses UTC time
- Convert your local time to UTC for the cron schedule
- Use [crontab.guru](https://crontab.guru/) to help with cron syntax

## 📜 License

This project is open source and available for anyone to use and modify.

## 🤝 Contributing

Feel free to fork this repository and customize it for your needs!

---

**Generated with ❤️ by GitHub Actions**
