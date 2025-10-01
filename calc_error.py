# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

from sklearn.metrics import mean_absolute_error
y_true = [1, 0, 1, 0]
y_pred = [0.300, 0.020, 0.890, 0.320]
mean_absolute_error(y_true, y_pred)

from sklearn.metrics import mean_squared_error
y_true = [1, 0, 1, 0]
y_pred = [0.300, 0.020, 0.890, 0.320]
mean_squared_error(y_true, y_pred)