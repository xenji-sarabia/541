import pandas as pd 
import numpy as np
import winsound

def playsound():
    winsound.PlaySound('ding.mp3', winsound.SND_FILENAME)


def main():
    businessDf = pd.read_csv('yelp_business_dataset_transformed.csv')

    checkinDf = pd.read_csv('kevin.csv')

    userDf = pd.read_csv('BENBIGBOOBS_ver5.csv')

    reviewDf = pd.read_csv('chrisdata_csv2.csv')

    print("reading complete")
    print ('business')
    print(businessDf.dtypes)
    print ('checkin')
    print(checkinDf.dtypes)
    print ('user')
    print(userDf.dtypes)
    print ('review')
    print(reviewDf.dtypes)
  # drop unnamed

    checkinDf.drop('Unnamed: 0', inplace=True, axis=1)  

    print("drop unnamed on checkin")

  # merge business and checkin

    busCheck = businessDf.merge(checkinDf, how='left', on='business_id')

    busCheck.rename(columns={'time':'checkin_times', 'count':'checkin_count'}, inplace=True)  

    print("merged business and checkin")

  # drop unnecessary user attributes
    userDf=userDf.drop(columns=['elite'])

  # merge review and user

    reviewUser = reviewDf.merge(userDf, how='left', on='user_id')



  # merge all datasets

    integratedDf = busCheck.merge(reviewUser, how='left', on='business_id')
    print (integratedDf)
    integratedDf.to_csv("megakevin.csv",index=False)
    playsound()

if __name__ == '__main__':

  main()