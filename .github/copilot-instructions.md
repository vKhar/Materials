# Copilot Instructions

## Big Picture
- Materials repo = curated Jupyter notebooks for NJC H2 Computing; no monolithic app, just thematic notebooks grouped by purpose.
- Knowledge flow: foundational theory in [Notes](Notes) → guided practice in [Exercises](Exercises) → bite-sized daily drills in [365-Days-of-H2-Computing](365-Days-of-H2-Computing).
- Each notebook mixes markdown pedagogy, math (LaTeX/KaTeX), and editable code cells that students complete; keep instructional text pristine while extending solution scaffolds separately.

## Environment & Tooling
- Target Python 3.7.7 plus teaching stack from [README.md](README.md) (Flask 2.2.5, PyMongo 4.6.1, Jupyter 6.5.6, DB Browser, MongoDB 3.4.9); assume students may only have that baseline.
- Prefer Jupyter Notebook format (`.ipynb`); when scripting is unavoidable, mirror content back into notebooks for learners.
- To distribute PDFs, run the VS Code task `ConvertPDF` (wraps `jupyter nbconvert --to pdf ${file}`) instead of ad-hoc commands.

## Notebook Structure Patterns
- Lessons start with "Learning Objectives" and a Colab badge (e.g. [365-Days-of-H2-Computing/Day_001.ipynb](365-Days-of-H2-Computing/Day_001.ipynb)); preserve the badge URL so hosted lessons stay in sync.
- Exercises consistently reference prerequisite chapters in their first markdown cell (see [Exercises/Exercise_02_Programming_Constructs.ipynb](Exercises/Exercise_02_Programming_Constructs.ipynb)); update both sides if you rename or add content.
- Code prompts are marked with `# YOUR CODE HERE` or `# YOUR ANSWER HERE`; append exemplar solutions below those cells instead of overwriting the placeholder so teachers can diff changes easily.
- Math-heavy prompts already use $$…$$ blocks (Exercise 2.2 arithmetic sequence); keep the same KaTeX-friendly syntax when adding new theory.

## Content Conventions
- Directory naming encodes sequencing: `Day_###`, `Exercise_##`, `Chapter_##`; follow the numbering to avoid breaking cross-links embedded in text.
- Shared media (figures, CSVs) belong in the nearest `img/` or `resources/` subfolder inside each track; reference them with relative paths so notebooks run in GitHub/Colab contexts.
- Examples rely on standard library only; if you need third-party modules, call them out explicitly in the markdown and keep imports confined to the cell that needs them.
- When illustrating algorithms, favor stepwise, input-driven programs similar to the IO walkthroughs in [365-Days-of-H2-Computing/Day_001.ipynb](365-Days-of-H2-Computing/Day_001.ipynb) to stay aligned with pedagogy.

## Workflow Tips
- Keep solutions deterministic and console-friendly so they work equally in IDLE, VS Code, and Colab (mirroring the sample interactions shown throughout the repo).
- Document any new dependencies or datasets directly inside the modified notebook header so learners know what to install before running cells.
- If you add new learning units, update adjacent notebooks to mention them in their "Related Notes"/"References" lists to maintain navigational consistency.
- When creating code solutions, do not attempt to use external modules like pandas, numpy etc, stick to the default Python library. modules like math, pymongo, flask, sqlite3, csv, datetime, socket, sys are allowed.
- do not use import unnecessarily.
- skip Notebook summary to avoid reading large file, just read the contents in the context
- do not attempt to read the entire .ipynb file
- when a task executed by a tool takes more than 3 minutes to complete, prompt user for abort or continue.