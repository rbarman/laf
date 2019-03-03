import pandas as pd
from config import *
from random import randint,choice
import os

def setup_warehouse():
	'''creates required folders and a sample file'''
	if not os.path.exists(SOURCE_PATH): os.makedirs(SOURCE_PATH)
	if not os.path.exists(RAW_PATH): os.makedirs(RAW_PATH)
	if not os.path.exists(FINAL_PATH): os.makedirs(FINAL_PATH)
	if not os.path.exists(REPORTS_PATH): os.makedirs(REPORTS_PATH)

	# random incremental file
	n = 100
	status = [choice(['PAID','DENIED','PENDING']) for r in range(0,n)]
	claimnum = [randint(0, 100) for r in range(0, n)]; 
	linenum = [randint(0, 9) for r in range(0, n)];
	paid = [randint(0, 10000) for r in range(0, n)];
	df = pd.DataFrame(data={"claimnum": claimnum,"linenum":linenum,"paid":paid,"status": status})
	df.to_csv(f'{SOURCE_PATH}claim_incr.csv', sep=',',index=False)

def extract():
	''' extract files from source and save to raw '''
	print(f'extracting {SOURCE_PATH}claim_incr.csv')
	df = pd.read_csv(f'{SOURCE_PATH}claim_incr.csv')
	df.to_pickle(f'{RAW_PATH}claim_incr.pkl')

def transform():
	'''transform datasets in /raw to and save to /final'''
	df = pd.read_pickle(f'{RAW_PATH}claim_incr.pkl')
	# seperate claims into paid and pend
	paid = df.loc[df['status'] == 'PAID']
	pend = df.loc[df['status'] == 'PENDING']
	# add a random risk score to paid claims
	risk = [randint(0, 100)/100 for r in range(0, len(paid))]; 
	paid['fraud_risk'] = risk
	# save
	paid.to_pickle(f'{FINAL_PATH}finclmsw.pkl')
	pend.to_pickle(f'{FINAL_PATH}pendw.pkl')

def create_report():
	''' create a summary report of final paid claims to /reports'''
	paid_claims = pd.read_pickle(f'{FINAL_PATH}finclmsw.pkl')
	report_df = pd.DataFrame({
    	'Total Paid': [paid_claims['paid'].sum()],
    	'Average Claim Fraud Risk': [paid_claims['fraud_risk'].mean()]
	})
	report_df.to_csv(f'{REPORTS_PATH}report.csv',index=False)

if __name__ == '__main__':
	setup_warehouse()