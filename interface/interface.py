import numpy as np
import matplotlib.pyplot as plt 
import matplotlib as mpl
from matplotlib import colors
from scipy import signal
from scipy import linalg
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import eegtools
import pylsl
import openbci_lsl
import tkinter

openbci_lsl [PORT] --stream
lib = lsl_loadlib();
disp('Resolving an EEG stream...');
result = {};
while isempty(result):
  result = lsl_resolve_byprop(lib,'type','EEG'); end
  inlet = lsl_inlet(result{1});
  while true
  [vec,ts] = inlet.pull_sample();
