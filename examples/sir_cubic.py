"""
=========================
Sliced Inverse Regression
=========================

An example plot of :class:`sdr.SlicedInverseRegression`
"""
import numpy as np
import sdr
import matplotlib.pyplot as plt

from sdr import datasets


X, y = datasets.make_cubic(random_state=123)

sir = sdr.SlicedInverseRegression()
X_sir = sir.fit_transform(X, y)

# estimate of the first effective dimension reducing direction (EDR)
beta1_hat = sir.components_[:, 0]


# plot data projected onto the first direction
plt.scatter(X_sir[:, 0], y, c=y, cmap='viridis', linewidth=0.5)
plt.xlabel("$X\hat{\\beta_1}$")
plt.ylabel("y")

# annotation showing the direction found
beta_text = "$\\beta_1$ = " + "{0}".format([0.707, 0.707])
plt.annotate(beta_text, xy=(-2, 6.5))
beta1_hat_text = "$\hat{\\beta_1}$ = " + "{0}".format(
    np.round(beta1_hat, 3).tolist()[:2])
plt.annotate(beta1_hat_text, xy=(-2, 7.5))

plt.show()
