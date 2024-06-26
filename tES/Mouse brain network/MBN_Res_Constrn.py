# -*- coding: utf-8 -*-
"""MBN_Res_Constrn

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k6_bmXQ1UOyzpzlmgAQBvlGzGNXZ2z09
"""

# processing.py (ES_Adaptive class definition)
import numpy as np
import networkx as nx

import sys
sys.path.append('../Model/tES/')
sys.path.append('./MouseBrainLib/')

# wrapper.py (Wrapper class and network creation)
import networkx as nx
from tES_Adaptive import tES_Adaptive
from DataUtils import DataUtils

class MBN_RC(tES_Adaptive, DataUtils):

    def __init__(self,
                 nepochs=10000,
                 dt=0.01,
                 lambda_o=0.01,
                 alpha=0.01,
                 beta=0.002,
                 plot_bifurcation=False,
                 epochs_per_lambda_o=10000,
                 step_size_lambda_o=0.003):

        DataUtils.__init__(self)

        self.nepochs = nepochs
        self.dt = dt
        self.lambda_o = lambda_o
        self.plot_bifurcation = plot_bifurcation
        self.epochs_per_lambda_o = epochs_per_lambda_o
        self.step_size_lambda_o = step_size_lambda_o
        self.alpha = alpha
        self.beta = beta

        self.initialize_mbn_network()

        tES_Adaptive.__init__(self,
                              self.A,
                              self.N,
                              self.lambda_o,
                              self.alpha,
                              self.beta,
                              self.nepochs,
                              self.dt,
                              self.plot_bifurcation,
                              self.epochs_per_lambda_o,
                              self.step_size_lambda_o)

    def initialize_mbn_network(self):
        self.N = self.N_REGIONS_WHOLE_BRAIN
        self.A = np.zeros([self.N, self.N])
        self.A[:] = self.WHOLE_BRAIN_CONN
        self.A = np.mat(self.A)
        #self.A[163:176,:] = 0 #removed PONS_left hemisphere
        #self.A[:,163:176] = 0
        #self.A[376:389,:] = 0 #removed PONS_right hemisphere
        #self.A[:,376:389] = 0
        # Create graph object from adjacency matrix
        self.G = nx.from_numpy_array(self.A)
        self.avg_degree = (sum(dict(self.G.degree()).values())/self.N)
        self.A = np.mat(nx.adjacency_matrix(self.G).todense())
        np.fill_diagonal(self.A, 0)
        print("Average shortest path length: ", nx.average_shortest_path_length(self.G))
        print("Avg clustering coefficient: ", nx.average_clustering(self.G))

    def run_model(self):
        tES_Adaptive.run_model(self)

    #Function to compute transition count
    def transition_count(self):
        data = self.GLOBAL_ORDER_VERBOSE
        global_min=min(data)
        global_max=max(data)
        up_tolerance=0.90*global_max
        down_tolerance=global_min + 0.07
        self.transitions=[]
        in_valley=False
        start_idx=None
        for i in range(1,len(data)-1):
          if data[i]<data[i-1] and data[i]<data[i+1]:
            in_valley=True
            start_idx=i
          elif data[i]>data[i-1] and data[i]>data[i+1] and in_valley:
            end_idx=i
            down_value=data[start_idx]
            up_value=data[end_idx]
            duration=end_idx-start_idx
            if down_value<=down_tolerance and up_value >=up_tolerance:
                self.transitions.append((down_value, up_value, duration))
            in_valley = False
        print("Number of Tansitions: ",len(self.transitions))

    #Function to compute transition time
    def transition_time(self):
        tNo=0
        tTransition=self.transitions
        self.tTime=[row[2] for row in tTransition]
        for i in self.tTime:
          tNo+=1
          print(f"Transition Time for Transition {tNo}: {self.tTime[tNo-1]:.2f} sec")
        try:
            avg_tTime=sum(self.tTime)/len(self.tTime)
        except ZeroDivisionError:
            avg_tTime=0
        print(f"Average transition time:{avg_tTime:.2f} sec")