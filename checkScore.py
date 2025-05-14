import Preprocessing
import Metrics
import pandas as pd

def Check_Score(t1,job_name,exp):
    res_cln = Preprocessing.TextPreprocessing(t1)
    df = pd.read_csv('cleanedDataJob.csv')
    job_des_cln = df.at[job_name, 'cleaned ']
    e = df.at[job_name, 'exp']
    skills = df.at[job_name, 'Skills ']
    sim_c = Metrics.cosine_Sim(res_cln,job_des_cln)
    sim_j = Metrics.Jaccard_Similarity(res_cln,job_des_cln)
    skl_mat = Metrics.skillMatching(skills,t1)
    exp_score = Metrics.CheckExpr(e,exp)
    return 40*skl_mat + 20*exp_score + 20*sim_c + 20*sim_j
    #return [skl_mat,exp_score,sim_c,sim_j]



