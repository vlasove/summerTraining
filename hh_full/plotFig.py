import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine # database connection

from pylab import rcParams
rcParams['figure.figsize'] = 14, 10



def plotter(request):
    disk_engine = create_engine('sqlite:///hh_parse.db') # Initializes database with filename 311_8M.db in current directory
  
  
  
  
  
    df_msk = pd.read_sql_query("SELECT salary FROM parseData WHERE lang = '%s' AND region = 'MSK'"%(request), disk_engine)
    df_spb = pd.read_sql_query("SELECT salary FROM parseData WHERE lang = '%s' AND region = 'SPB'"%(request), disk_engine)
    df_ekb = pd.read_sql_query("SELECT salary FROM parseData WHERE lang = '%s' AND region = 'EKB'"%(request), disk_engine)
    df_nvsb = pd.read_sql_query("SELECT salary FROM parseData WHERE lang = '%s' AND region = 'NVSB'"%(request), disk_engine)
    
    try:
        x_msk = df_msk['salary']
        n, _, patches = plt.hist(x_msk, int(len(x_msk)/2), facecolor='b', alpha=0.6, label = 'MSK Average Salary = %.1f and STD = %.1f'%(x_msk.mean(), x_msk.std()))
    except:
        pass

    try:
        x_spb = df_spb['salary']
        n, _, patches = plt.hist(x_spb, int(len(x_spb)/2), facecolor='g', alpha=0.6, label = 'SPB Average Salary = %.1f and STD = %.1f'%(x_spb.mean(), x_spb.std()))
    except: 
        pass

    try:
        x_ekb = df_ekb['salary']
        n, _, patches = plt.hist(x_ekb, int(len(x_ekb)/2), facecolor='r', alpha=0.6, label = 'EKB Average Salary = %.1f and STD = %.1f'%(x_ekb.mean(), x_ekb.std()))
    except:
        pass
    try:
        x_nvsb = df_nvsb['salary']
        n, _, patches = plt.hist(x_nvsb, int(len(x_nvsb)/2), facecolor='y', alpha=0.6, label = 'NVSB Average Salary = %.1f and STD = %.1f'%(x_nvsb.mean(), x_nvsb.std()))
    except:
        pass

    
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.title('%s Salary Info'%(request))
    plt.grid(True)
    plt.legend()
    plt.savefig('%s_plot.png'%request)
    plt.close()





