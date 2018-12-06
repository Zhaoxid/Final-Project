from data_processing import data_process
from sklearn.model_selection import KFold
from sklearn.svm import LinearSVC

data = data_process()
print(data.df.head(5))

# k-fold split data
def kfold_split(data, kf_train, kf_test, k):        
    kf = KFold(n_splits=k)    
    for train_index, test_index in kf.split(data):       
        train = data.iloc[train_index]
        test = data.iloc[test_index]        
        kf_train.append(train)
        kf_test.append(test) 
            
# get feature X and label y from the dataset
def feature_label_split(data):   
    X = data[['Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years',
              'Marital_Status','rProduct_Category_1','Product_Category_2','Product_Category_3']]
    y = data['Purchase']      
    return (X, y)

# fit model and get accuracy and weights assigned to each feature            
def predict(X_train, y_train, X_test, y_test):    
    clf = LinearSVC(C=1.0, random_state=0)
    clf.fit(X_train, y_train)   
    score = clf.score(X_test, y_test)
    weight = clf.coef_   
    return (score, weight)
  

train_set=[]
test_set=[]

kfold_split(data, train_set, test_set, 10)

scores = []
weights = []
for train, test in train_set, test_set:
    X_train = feature_label_split(train)[0]
    y_train = feature_label_split(train)[1]
    X_test = feature_label_split(test)[0]
    y_test = feature_label_split(test)[1]
    
    score = predict(X_train, y_train, X_test, y_test)[0]
    weight = predict(X_train, y_train, X_test, y_test)[1]
    
    scores.append(score)
    weights.append(weight)
    
print(scores)
print(weights)
