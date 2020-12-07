import pickle
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import (
    roc_curve, roc_auc_score, 
    confusion_matrix, 
    precision_recall_curve,
    accuracy_score, 
    precision_score, 
    recall_score
)
    
from tabulate import tabulate
import numpy as np
import sys




def curva_roc(y_test,predicted_labels,fpr,tpr):
	plt.clf()
	plt.plot([0,1],[0,1], 'k--', c="red")
	plt.plot(fpr, tpr)
	plt.title("ROC best RF, AUC: {}".format(roc_auc_score(y_test, predicted_labels)))
	plt.xlabel("fpr")
	plt.ylabel("tpr")

	return plt.show()


def get_metrics_report(fpr, tpr, thresholds, precision, recall, thresholds_2):
    df_1 = pd.DataFrame({'threshold': thresholds_2,'precision': precision,
                    'recall': recall})
    df_1['f1_score'] = 2 * (df_1.precision * df_1.recall) / (df_1.precision + df_1.recall)
    
    df_2 = pd.DataFrame({'tpr': tpr, 'fpr': fpr, 'threshold': thresholds})
    df_2['tnr'] = 1 - df_2['fpr']
    df_2['fnr'] = 1 - df_2['tpr']
    
    df = df_1.merge(df_2, on="threshold")
    
    return df

def tabla_referencia():
	tabla = tabulate(np.array([['True Positive (tp)', 'False Negative (fn)'],
		['False Positive (fp)', 'True Negative (tn)']]),
	headers=['Dato\Predicción','Etiqueta +','Etiqueta -'],
	showindex=['Etiqueta +','Etiqueta -'],
	tablefmt='pretty')

	return tabla

def tabla_confusion(data):
	tabla = tabulate(data,
	headers=['Dato\Predicción','Etiqueta +','Etiqueta -'],
	showindex=['Etiqueta +','Etiqueta -'],
	tablefmt='pretty')

	return tabla	

def precision_at_k(y_true, y_scores, k):
	threshold = np.sort(y_scores)[::-1][int(k*len(y_scores))]
	y_pred = np.asarray([1 if i >= threshold else 0 for i in y_scores])

	return precision_score(y_true, y_pred)

def recall_at_k(y_true, y_scores, k):
	threshold = np.sort(y_scores)[::-1][int(k*len(y_scores))]
	y_pred = np.asarray([1 if i >= threshold else 0 for i in y_scores])

	return recall_score(y_true, y_pred)

def curva_pre_re(y_test,y_scores):
	k_values = list(np.arange(0.01, 0.99, 0.01))
	d = pd.DataFrame(index=range(len(k_values)),columns=['k','precision','recall'])
	for k in range(len(k_values)):
		d['k'][k] = k_values[k]
		d['precision'][k]=precision_at_k(y_test,y_scores,k_values[k])
		d['recall'][k]=recall_at_k(y_test,y_scores,k_values[k])

	fig, ax1 = plt.subplots()
	ax1.plot(d['k'], d['precision'], label='precision')
	ax1.plot(d['k'], d['recall'], label='recall')
	plt.legend()




