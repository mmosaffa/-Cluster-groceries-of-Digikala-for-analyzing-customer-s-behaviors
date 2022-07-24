import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori,association_rules
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv('E:/service5.csv')
df.describe(include="all").iloc[:,:3]
df = df.iloc[:,:7]
np.sum(df.isna())
D=df.dropna()
#s=np.random.choice(D.shape[0],int(0.3*D.shape[0]),replace=False)
#D=D.iloc[s,:]


#'''
A=pd.get_dummies(D)
frequent_itemsets = apriori(A, min_support=0.05, use_colnames=True,max_len=3)
rules = association_rules(frequent_itemsets, metric="confidence",min_threshold=0.2)
#low_memory=False
#Get some info about time-related rules
Month=A.columns[0:6]
monthrules=[]
for x in Month:
    if sum(rules['antecedents']=={x})>0:
     monthrules.append(rules[rules['antecedents']=={x}])   


#April
monthrules[0].iloc[:,:2]
monthrules[0].iloc[:,2:5]
monthrules[0].iloc[:,5:]

#February
monthrules[1].iloc[:,:2]
monthrules[1].iloc[:,2:5]
monthrules[1].iloc[:,5:]

#January
monthrules[2].iloc[:,:2]
monthrules[2].iloc[:,2:5]
monthrules[2].iloc[:,5:]


#Get some info about agency-related rules
Agency=A.columns[6:22]

agencyrules=[]
for x in Agency:
    if sum(rules['antecedents']=={x})>0:
     agencyrules.append(rules[rules['antecedents']=={x}])   

#DOT
agencyrules[0].iloc[:,:2]
agencyrules[0].iloc[:,2:5]
agencyrules[0].iloc[:,5:]

#DSNY
agencyrules[1].iloc[:,:2]
agencyrules[1].iloc[:,2:5]
agencyrules[1].iloc[:,5:]

#HPD
agencyrules[2].iloc[:,:2]
agencyrules[2].iloc[:,2:5]
agencyrules[2].iloc[:,5:]

#concat=pd.concat((agencyrules[2].iloc[:,:2],agencyrules[2].iloc[:,2:5],agencyrules[2].iloc[:,5:]),axis=1)


#Get some info about borough-related rules
Borough=A.columns[1070:]
Boroughrules=[]
for x in Borough:
    if sum(rules['antecedents']=={x})>0:
     Boroughrules.append(rules[rules['antecedents']=={x}])   

Boroughrules[0].iloc[:,:2]
Boroughrules[0].iloc[:,2:5]
Boroughrules[0].iloc[:,5:]

#Get some info about complaint-type-related rules
Complaint=A.columns[23:162]


#Removing NYPD and HPD
D2=D[D['Agency']!='NYPD']
D2=D2[D2['Agency']!='HPD']
A2=pd.get_dummies(D2)
frequent_itemsets2 = apriori(A2, min_support=0.05, use_colnames=True,max_len=2)
rules2 = association_rules(frequent_itemsets2, metric="confidence",min_threshold=0.2)

#Get some info about time-related rules
Month2=A2.columns[0:6]
monthrules2=[]
for x in Month2:
    if sum(rules2['antecedents']=={x})>0:
     monthrules2.append(rules2[rules2['antecedents']=={x}])   


#April
monthrules2[0].iloc[:,:2]
monthrules2[0].iloc[:,2:5]
monthrules2[0].iloc[:,5:]

#June
monthrules2[3].iloc[:,:2]
monthrules2[3].iloc[:,2:5]
monthrules2[3].iloc[:,5:]

#Get some info about agency-related rules
Agency2=A2.columns[6:21]

agencyrules2=[]
for x in Agency2:
    if sum(rules2['antecedents']=={x})>0:
     agencyrules2.append(rules2[rules2['antecedents']=={x}])   

#DOHMH
agencyrules2[0].iloc[:,:2]
agencyrules2[0].iloc[:,2:5]
agencyrules2[0].iloc[:,5:]

#
agencyrules2[1].iloc[:,:2]
agencyrules2[1].iloc[:,2:5]
agencyrules2[1].iloc[:,5:]




#Get some info about borough-related rules
Borough2=A2.columns[910:]
Boroughrules2=[]
for x in Borough2:
    if sum(rules2['antecedents']=={x})>0:
     Boroughrules2.append(rules2[rules2['antecedents']=={x}])   

Boroughrules2[2].iloc[:,:2]
Boroughrules2[2].iloc[:,2:5]
Boroughrules2[2].iloc[:,5:]

#Get some info about complaint-type-related rules
Complaint2=A2.columns[21:125]
Complainthrules2=[]
for x in Complaint2:
    if sum(rules2['antecedents']=={x})>0:
     Complainthrules2.append(rules2[rules2['antecedents']=={x}])   

Complainthrules2[0].iloc[:,:2]
Complainthrules2[0].iloc[:,2:5]
Complainthrules2[0].iloc[:,5:]
