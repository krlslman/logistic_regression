import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the data
df = pd.read_csv('/home/koral/Desktop/FullStackTraining/regression/krediVeriseti.csv', delimiter=';', header=0, names=['krediMiktari', 'yas', 'evDurumu', 'aldigi_kredi_sayi', 'telefonDurumu', 'KrediDurumu'])
print(df)

