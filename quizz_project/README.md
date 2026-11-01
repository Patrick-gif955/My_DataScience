# Python Trivia Quiz

A command-line quiz program I built using Python and the Open Trivia Database API.

I created this project to take my Python learning further by working with an external API instead of relying on data I created myself.

## About the Project

The program fetches five general knowledge questions from the Open Trivia Database API.

Each question comes with four options, which are shuffled randomly. Users select their answers using A, B, C, or D.

The program checks each answer, provides feedback, and displays the final score after all five questions.

## What I Learned

While building this project, I practised:

- **Working with APIs:** Using Python's `requests` library to fetch data and understanding HTTP status codes such as 200, 404, and 429.
- **JSON processing:** Converting API responses into Python objects and accessing data stored in nested dictionaries and lists.
- **Data cleaning:** Using `unquote()` to decode URL-encoded characters in the questions and answers.
- **Python logic:** Using loops, conditional statements, `random.shuffle()`, and exception handling to manage the quiz.

## Challenges I Faced

One challenge was understanding how to extract and process the correct and incorrect answers from the API response.

I also encountered issues with list indexing, decoding text, and validating user input.

Working through these challenges helped me understand Python lists, dictionaries, and error handling better.

## Try the Quiz

You can test the project here:

**[Live Quiz Link](https://onlinegdb.com/EBWChZcuC)**

## Tools Used

Python, Requests, Open Trivia Database API

## Author

Patrick Newton