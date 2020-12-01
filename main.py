import pandas as pd
import datetime
import smtplib   


def sendemail(to,content):
    print(f"{content} sending emai to {to}")
    server=smtplib.SMTP_SSL("smtplib@gmail.com",465)
    server.ehlo
    server.starttls
    server.login("your email-id","password")
    sendemail("your email id",to,content)
    server.quit()


df=pd.read_excel("birthday.xlsx")
# Reading the excel sheet


if __name__ == "__main__":
    
    today=datetime.datetime.now().strftime("%d-%m")
    yearnow=datetime.datetime.now().strftime("%Y")
    writeindex=[] 
    for index,item in df.iterrows():
        birthday=item["Date"].strftime("%d-%m")
        # converting birthday date into day-month format
        if birthday==today and yearnow not in str(item["Year"]):
            sendemail(item["Email"],"Happy birthday bro")
            writeindex.append(index)

    for i in writeindex:
        yr=df.loc[i,"Year"]
        df.loc[i,"Year"]=str(yr)+","+str(yearnow)
        print(df.loc[i,"Year"])

        # wrinting the birhyear in which you have wished your friend
    df.to_excel("birthday.xlsx",index=False)

''' credit codewithharry'''