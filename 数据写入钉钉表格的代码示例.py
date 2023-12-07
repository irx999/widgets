import requests
import json
import  pandas as pd
import datetime




class Ding():

    def __init__(self,appkey,appsecret,operatorId,df_data,sheetid,sheetname,wt_range):
        
        

        access_token = requests.get(f"https://oapi.dingtalk.com/gettoken?appkey={appkey}&appsecret={appsecret}").json()["access_token"]
        # print(access_token)
        self.Header = {  'Host':'api.dingtalk.com',
                    'x-acs-dingtalk-access-token':access_token,
                    'Content-Type':'application/json'}
        self.df = df_data
        self.total = len(df_data)
        self.operatorId = operatorId
        self.sheetid= sheetid
        self.sheetname = sheetname
        self.begin = list(wt_range)
        self.width = [chr(i) for i in range(97,123)][df_data.shape[1]-2+int(self.begin[1])]
    def meterHead(self,df):
        url = f"https://api.dingtalk.com/v1.0/doc/workbooks/{self.sheetid}/sheets/{self.sheetname}/ranges/{self.begin[0]}{int(self.begin[1])}:{self.width}{int(self.begin[1])}?operatorId={self.operatorId}"
        # data = ERP(erpcookie).get_Goods_Stock()[1].astype("str").iloc[start-1:end, :].values.tolist()
        json1 = {"values" : [df.columns.tolist()]}
        print(df.columns.tolist())
        x1 = requests.put(url= url,headers= self.Header,data=json.dumps(json1),verify=False)
        print(url)
        print(x1.text)
    def w_time(self,range):
        url = f"https://api.dingtalk.com/v1.0/doc/workbooks/{self.sheetid}/sheets/{self.sheetname}/ranges/{range}?operatorId={self.operatorId}"
        # data = ERP(erpcookie).get_Goods_Stock()[1].astype("str").iloc[start-1:end, :].values.tolist()
        now  = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")
        
        json1 = {"values" : [[now]]}
        
        x1 = requests.put(url= url,headers= self.Header,data=json.dumps(json1),verify=False)
        print(url)
        print(x1.text)


    def toding(self,df,start,end):
        url = f"https://api.dingtalk.com/v1.0/doc/workbooks/{self.sheetid}/sheets/{self.sheetname}/ranges/{self.begin[0]}{start+int(self.begin[1])}:{self.width}{end+int(self.begin[1])}?operatorId={self.operatorId}"
        json1 = {"values" : df.astype("str").iloc[start-1:end, :].values.tolist()}
        x1 = requests.put(url= url,headers= self.Header,data=json.dumps(json1),verify=False)
        print(url)
        print(x1.text)

    def cycle(self,number):
        
        num_segments = number // 1000
        for i in range(num_segments):
            start = i * 1000 + 1
            end = (i + 1) * 1000
            self.toding(self.df,start,end)

        if number % 1000 != 0:
            start = num_segments * 1000 + 1
            end = number
            self.toding(self.df,start,end)
    def main(self):
        self.w_time(range = "O1")
        self.meterHead(self.df)
        self.cycle(len(self.df))

if __name__ == "__main__":
    
    
    Ding(appkey = "密钥",
         appsecret="密钥",
         operatorId = "用户id",
        df_data= "pandas的dataframe",
        sheetid= "表格id",
        sheetname= "表格名称",
        wt_range= "A1"
        ).main()
