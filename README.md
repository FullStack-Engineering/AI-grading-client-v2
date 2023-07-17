# AI-grading-v2

This is the second version of the AI grading tool. This tool is designed to grade Hireflix interviews for the following technologies/ skills: 

> React, PM (Project Manager), .NET, Node, QA Automation, QA Manual, PHP - Laravel, Java, Python Data Engineer, Python, Business Analyst, Ruby, DevOps, Angular, AI Machine Learning Engineer, Product Manager.

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

>> React, PM, .NET, Node, QA Automation, QA Manual, PHP - Laravel, Java, Python Data engineer, Python, Business Analyst, Ruby, DevOps - AWS, Angular, ML, Product Manager

4. Run the script using the url and tech/skill:  `python3 AIGrade_v2.py --url <copied-url> --tech <copied-tech>` 

5. Verify the output of the script in the console

### Output:
The tool will provide three values as output:

1. `AI Score`: Grade of the interview
2. `Decision`: Final Decision based on the interview score
3. `Flag`: Recommendation based on grading results

If the score is higher than 7, you should go and grade the interview. Make sure to store the AI results in JIRA after you have finished grading. If the score is bellow 7, and the value of `Flag` is `No-Hire`, you should skip the interview. In this case, you shoul provide the AI score in the candidate's Lever profile, and make a note clarifying the decision made by the AI tool.

_______________
Last update: 6/28/2023


