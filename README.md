# AI-grading-v2

This is the second version of the AI grading tool. This tool is designed to grade Hireflix interviews for the following technologies/ skills: 

> React, .NET, Node, PHP - Laravel, Java, Python, Ruby, Angular.

Please follow the instructions to install and use the tool.

## Installation Steps

> The tool requires python >= 3.9

1. Clone the repo

2. Move to the project directory: 
<code> cd AI-grading-client-v2 </code>

3. Install dependencies: 
`pip install -r requirements.txt`

## How to use

In this initial phase, we will use the tool to filter out the interviews that fail. If the result from the AI grader is < 7, you should assign the grade to the interview and move along.

### Usage:

1. Move to the project directory : 
<code> cd AI-grading-client-v2 </code>

2. Copy the hireflix URL for the interview you want to grade. it should look like this: `https://admin.hireflix.com/es/jobs/<position-id>/interview/<candidate-interview-id>` 

3. Copy the name of the tech/skill to be evaluated:

>> React, .NET, Node, PHP - Laravel, Java, Python, Ruby, Angular

4. Take into account the Seniority of the candidadate based on the recruiters assessment and position:

>> Principal, Senior, Mid-level, Junior

5. Run the script using the url, tech/skill, and seniority:  `python3 AIGrade_v2.py --url <copied-url> --tech <copied-tech> --seniority <seniority-level>` 

6. Verify the output of the script in the console

### Output:
The tool will provide four values as output:

1. `AI Score`: Grade of the interview
2. `Decision`: Final Decision based on the interview score
3. `Flag`: Recommendation based on grading results
4. `Final Feedback`: Final Feedback for the candidate's interview

After grading each question, the script will store the detailed results in a JSON file named `detailed_scores_<interview-id>.json` in the project's working directory. The JSON file stores both the score and the feedback for each question.

If the score is higher than 7, you should go and grade the interview. Make sure to store the AI results in JIRA after you have finished grading. If the score is bellow 7, and the value of `Flag` is `No-Hire`, you should skip the interview. In this case, you should provide the AI score in the candidate's Lever profile, and make a note clarifying the decision made by the AI tool.

_______________
Last update: 10/08/2023


