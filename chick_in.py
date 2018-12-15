import pandas as pendi
import ast
import winsound

def playsound():
    winsound.PlaySound('ding.mp3', winsound.SND_FILENAME)

def main():

    path='yelp_academic_dataset_checkin.json'
    datafrau=pendi.read_json(path,orient="columns",lines=True)
    dickface=datafrau.index

    print("max range is: ",dickface)

    datasx="{'count': ["
    #print(datasx)
    for x in range (0,157075):
        momel=datafrau.loc[x]['time']
        sub=0
        #sub=":"
        momel=str(momel)
        #print ("momel:", momel)
        #bobel=momel.count(sub,0,len(momel))
        for x in range(0,len(momel)):
            if momel[x:x+1]==":" and (momel[x+3:x+4]==","or momel[x+3:x+4]=="}"):
                sub=sub+int(momel[x+2:x+3])    
            elif momel[x:x+1]==":" and (momel[x+4:x+5]==","or momel[x+4:x+5] =="}" ):
                sub=sub+int(momel[x+2:x+4])
            elif momel[x:x+1]==":" and (momel[x+5:x+6]==","or momel[x+5:x+6] =="}" ):
                sub=sub+int(momel[x+2:x+5])
        #print(sub)
        str(sub)
        if x==157074:
            datasx=datasx+str(sub)
        else:
            datasx=datasx+str(sub)+", "
        #print("bobel:",bobel)

        
    datasx=datasx+"]}"
    datasx=ast.literal_eval(datasx)
    zxc=pendi.DataFrame(data=datasx)
    datafrau=datafrau.join(zxc)
    datafrau.to_csv(path_or_buf="kevin.csv")

if __name__ == '__main__':

  main()