# Train linear ridge regression model using naive feature set
from sklearn import linear_model, cross_validation, metrics, ensemble

#alpha is a tuning parameter affecting how regression deals with collinear inputs
linear = linear_model.Ridge(alpha = 0.5)  

cv = cross_validation.ShuffleSplit(len(bandgaps),\
                                       n_iter=10, test_size=0.1, random_state=0)

scores = cross_validation.cross_val_score(linear, naiveFeatures,\
                                              bandgaps, cv=cv, scoring='mean_absolute_error')

print("The MAE of the linear ridge regression band gap model using the naive feature set is: "\
          + str(round(abs(mean(scores)), 3)) + " eV")
