# %%
import pandas as pd
import json
import requests
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import warnings
import os
from dotenv import load_dotenv, find_dotenv
warnings.simplefilter("ignore")
# %%

# Parse command line arguments
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-u", "--url", type=str, help="hireflix interview url")
parser.add_argument("-t", "--tech", type=str, help="Technology evaluated")
args = vars(parser.parse_args())

# Set up parameters
hf_url = args["url"]
technology = args["tech"]
load_dotenv(find_dotenv())
access_token = os.getenv('AWS_API_KEY')

# %%
# url = 'https://admin.hireflix.com/es/jobs/646fb78ac74fd055303aa0fc/interview/648c5b120d5fd5e960f53279'
# technology = 'PM'

headers = {'Authorization': f'Bearer {access_token}'}

# %%
interview_id = hf_url.split('/')[-1]

response = requests.post(url="https://dev-fs-ai-vetting.fullstack.com/ScoreInterview", headers=headers, data=json.dumps({'interview_id': interview_id,
                                                                                                                         'technology': technology
                                                                                                                         }))

# %%
if response.json():
    
    final_score = response.json()['final_score']
    decision = response.json()['decision']
    flag = response.json()['flag']
    
    if flag == "Hire":
        score_name = 'knn_score'
    else:
        score_name = 'rf_score'
    
    question_scores = json.loads(response.json()['question_scores'])[score_name]
    
    
    print('AI Score: {0}'.format(final_score))
    print('Decision: {0}'.format(decision))
    print('Flag: {0}'.format(flag))
    print(f"Detailed Questions' Scores: {json.dumps(question_scores)}")

else:
    print('Error Running the app. Please try again.')