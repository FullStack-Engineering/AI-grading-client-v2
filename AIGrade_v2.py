#%%
import pandas as pd
import json
import requests
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import warnings
warnings.simplefilter("ignore")
#%%

# Parse command line arguments
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-u", "--url", type=str, help="hireflix interview url")
parser.add_argument("-t", "--tech", type=str, help="Technology evaluated")
args = vars(parser.parse_args())
 
# Set up parameters
hf_url = args["url"]
technology = args["tech"]

#%%
#url = 'https://admin.hireflix.com/es/jobs/646fb78ac74fd055303aa0fc/interview/648c5b120d5fd5e960f53279'
#technology = 'PM'

#%%
interview_id = hf_url.split('/')[-1]

response = requests.post(url = 'http://127.0.0.1:5500/ScoreInterview', data = json.dumps({'interview_id': interview_id,
                                                                                          'technology': technology
                                                                                          }))

# %%
if response.json():
    print('AI Score: {0}'.format(response.json()['final_score']))
    print('Decision: {0}'.format(response.json()['decision']))
    print('Flag: {0}'.format(response.json()['flag']))

