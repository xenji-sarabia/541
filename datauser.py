import pandas as pd

def main():

    path="BENBIGBOOBS_ver1.csv"
    df=pd.read_csv(path)
    df=df[['user_id','average_stars','compliment','cool','fans','funny','review_count','useful','elite']]
    print(df)
    #df=df.drop()
    
    #usefulmax=df['useful'].max()
    #complimentmax=df['compliment'].max()
    #reviewmax=df['review_count'].max()
    for x in range (0,1518168):
        totalscore=df.loc[x,'average_stars']
        totalscore=float(totalscore)
      #  totalscore=((totalscore/5)*35)
        df.at[x,'average_stars']=(totalscore)

        totalscore=df.loc[x,'compliment']
        totalscore=float(totalscore)
        df.at[x,'compliment']=(totalscore)

        totalscore=df.loc[x,'useful']
        totalscore=float(totalscore)
     #   totalscore=(((totalscore/usefulmax)*100)*.35)
        df.at[x,'useful']=(totalscore)

        totalscore=df.loc[x,'review_count']
        totalscore=float(totalscore)
      #  totalscore=(totalscore/reviewmax)*20
        df.at[x,'review_count']=(totalscore)

        totalscore=df.loc[x,'cool':'funny']
        totalscore=float(totalscore.sum())
        df.at[x,'cool']=(totalscore)
    df=df.drop(columns=['fans','funny'])
    #df=df.rename(columns={'cool':'misc_score'},inplace=True)
    print(df)
    df.to_csv("BENBIGBOOBS_ver2.csv",index=False)

   
    '''#compliments="{'compliment_total': ["
    #score=0
    #for x in range (0,1518169):
    #    score=int(df.
    # loc[x]['compliment_cool'])+int(df.loc[x]['compliment_cute'])+int(df.loc[x]['compliment_funny'])+int(df.loc[x]['compliment_hot'])+int(df.loc[x]['compliment_list'])+int(df.loc[x]['compliment_more'])+int(df.loc[x]['compliment_note'])+int(df.loc[x]['compliment_photos'])+int(df.loc[x]['compliment_plain'])
    #    compliments=compliments+str(score)+', '
    #compliments=compliments+"]}"
    #print("for loop done")
    #import ast
    compliments=ast.literal_eval(compliments)
    zxc=pd.DataFrame(data=compliments)
    print(zxc)
    '''

    '''
def junothepolarbear(df):
    df=df[['average_stars','compliment','cool','fans','funny','review_count','useful','elite','user_id']]
    
    #df=df.drop()
    usefulmax=df['useful'].max()
    reviewmax=df['review_count'].max()
    for x in range (0,1518169):
        totalscore=df.loc[x,'average_stars']
        totalscore=float(totalscore)
        totalscore=((totalscore/5)*35)
        df.at[x,'average_stars']=(totalscore)

        totalscore=df.loc[x,'compliment']
        totalscore=float(totalscore)
        df.at[x,'compliment']=(totalscore)

        totalscore=df.loc[x,'useful']
        totalscore=float(totalscore)
        totalscore=(((totalscore/usefulmax)*100)*.35)
        df.at[x,'useful']=(totalscore)

        totalscore=df.loc[x,'review_count']
        totalscore=float(totalscore)
        totalscore=(totalscore/reviewmax)*20
        df.at[x,'review_count']=(totalscore)

        totalscore=df.loc[x,'cool':'funny']
        totalscore=float(totalscore.sum())
        df.at[x,'cool']=(totalscore)
    df=df.drop(columns=['fans','funny'])
    print(df)
    df.to_csv("BENBIGBOOBS_ver2.csv",index=False)
 
'''

def kevinisastar(df):
    #path='optimized_yelp_academic_dataset_user1.csv'
    #df=pd.read_csv(path)
    
   # path='optimized_yelp_academic_dataset_user1.csv'
    #df=pd.read_csv(path)
   
    df=df.drop(columns=['friends'])
    
    #kevinisastar()
    df=df.drop(columns=['name','yelping_since'])
    print (df)
    print("done reading")
    #for x in range (0,1518169):
    #x=1515181
    for x in range (0,1518169):
        series = df.loc[x, 'compliment_cool':'compliment_writer']
        df.at[x,'compliment_cool']=series.sum()
        #print(series.sum())
    #print(series.sum())
    print(df['compliment_cool'])
    df=df.rename(columns={'compliment_cool':'compliment'})
    df=df.drop(['compliment_cute','compliment_writer','compliment_funny','compliment_hot','compliment_list'],axis=1)
    df=df.drop(['compliment_more','compliment_note','compliment_photos','compliment_plain','compliment_profile'],axis=1)
    #df=df.rename(index=str,columns={'compliment_cool','compliment'},axis=1)
    df.to_csv("BENBIGBOOBS_ver1.csv",index=False)
    #print(df)

if __name__ == '__main__':

  main()