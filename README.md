# How to use

- `python trials.py init` creates the experiments folder.

- `python trials.py assign` creates the `trial_order.txt` file which indicates who will do which trials, and which assigns a random order for each trial.

- You may call `python trials.py analyze` when you have pasted all the chatbot responses from each `inputs/trial{n}.txt` into the corresponding `outputs/trial{n}.txt` folder. This will produce two CSV files; one for word count per response, and another for average word length.
