import mysql.connector as mycon
from . import prediction
import os
import shutil
def connect() : 
    con=mycon.connect(host='localhost',user='root',password='Password',database='animalspeciesdb')
    return con
 
def handle_uploaded_file(f):
    with open('../searchable_cloud_enc/static/Uploads/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 
    return f.name
def getDictionary() :  
    conn = connect()    
    cursor = conn.cursor() 
    cursor.execute("select srNo as key1,title as val from labels")
    out = cursor.fetchall()
    variable = {key:val for key,val in out}
    print(variable)
    conn.commit()
    return variable
def getDictionary1(category="na") :  
    conn = connect()    
    cursor = conn.cursor() 
    cursor.execute("select srNo as key1,title as val from labels1 where category='"+category+"'")
    out = cursor.fetchall()
    variable = {key:val for key,val in out}
    print(variable)
    conn.commit()
    return variable
def getSrno(cate='NA'):
    conn = connect()
    #integrated security 
    cursor = conn.cursor() 
    print("select srNo as mxid from labels where title='"+cate+"';")
    cursor.execute("select srNo as mxid from labels where title='"+cate+"';")

    #args = [userid,title,docPath,docDesc,dt,tm,key]
    #args1=cursor.callproc('insertDoc', args)
    #print("Return value:", args1)
    #for result in cursor.stored_results():
    #        print(result.fetchall())
    #cnt=cursor.rowcount
    conn.commit()
    #return cnt
def handle_uploaded_file1(f):
    UPLOAD_DIR='../animal_species_detection/static/InputImg/' 
    try:
        for file in os.listdir(UPLOAD_DIR):
            print(file)
            os.remove(UPLOAD_DIR+"/"+file)  
    except Exception:
        print("directory exist")
    try:
        for file in os.listdir(UPLOAD_DIR+"\\temp\\1\\"):
            print(file)
            os.remove(UPLOAD_DIR+"\\temp\\1\\"+file)  
    except Exception:
        print("directory exist")
    nm,ext=os.path.basename(f.name).split('.')
    with open('../animal_species_detection/static/InputImg/1001.'+ext, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    filename="1001."+ext 
    shutil.copy('../animal_species_detection/static/InputImg/1001.'+ext,'../animal_species_detection/static/InputImg/1002.'+ext)
    category=prediction.Prediction(filename,"../animal_species_detection/static/")
    category1="NA"
    try:
        category1=prediction.Prediction1(filename,"../animal_species_detection/static/",category)
    except Exception:
        category1="NA"
    print("cate="+category+" "+category1)
    return category+"|"+category1+"|1002."+ext

def getDocs() : 
    lst=[]
    conn = connect()    
    cursor = conn.cursor()
    #cursor.execute("select* from userprofile where userid='"+uid+"'")
    print("select GROUP_CONCAT(keyw SEPARATOR ' ') as txt from keywords k where score>50 group by docid  order by docid asc")
    sql_select_query = "select GROUP_CONCAT(keyw SEPARATOR ' ') as txt from keywords k where score>50 group by docid  order by docid asc"
    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    print(cursor.rowcount)
    final_result = [list(i) for i in record]
    #conn.commit()
    for x in record:
        lst.append(x[0])
        print(x[0]+'\n')
    return lst
def login(userid="NA",pass1="NA") : 
    val='NA'
    conn = connect()    
    cursor = conn.cursor()
    args = [userid,pass1]
    args1=cursor.callproc('userlogin', args)
    print("Return value:", args1)
    for result in cursor.stored_results():
        val=result.fetchall()
        print(result.fetchall())
    conn.commit()
    print(val[0][0])
    print(val[0][3])
    return val
def insertKeywords(keywDic) : 
     
    conn = connect()    
    mycursor = conn.cursor()
    sql = "INSERT INTO keywords(keyw,score,docid) VALUES (%s, %s,%s)"
    
    mycursor.executemany ( sql, keywDic )

    conn.commit ( )

    #print ( mycursor.rowcount, "was inserted." )
    conn.commit()

def convertToBase64(message='NA') :
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)
    return base64_message

def convertFromBase64(base64_message='NA') :
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print(message)
    return message
def insertUser(userid='NA',pass1='NA',name='NA',addr='NA',pincode='NA',mobile="NA",email="NA",gender="Na",dob="NA",state="NA",city="NA",photo="NA") : 
    val='NA'
    conn = connect()    
    cursor = conn.cursor()
    args = [userid,pass1,name,mobile,email,city,state,gender,addr,dob,pincode,photo]
    args1=cursor.callproc('insertUser', args)
    #print("Return value:", args1)
    #for result in cursor.stored_results():
       # val=result.fetchall()
        #print(result.fetchall())
    conn.commit()
    #print(val[0])
    
def insertDoc1(userid="NA",title="NA",docPath="NA",docDesc='NA',dt="NA",tm="NA",key='NA',cost1=0) : 
    conn = connect()    
    cursor = conn.cursor()
    args = [userid,title,dt,tm,docDesc,key,docPath,cost1]
    args1=cursor.callproc('insertDoc', args)
    print("Return value:", args1)
    #for result in cursor.stored_results():
     #       print(result.fetchall())
    cnt=cursor.rowcount 
    conn.commit()


    #args = [userid,title,docPath,docDesc,dt,tm,key]
    #args1=cursor.callproc('insertDoc', args)
    #print("Return value:", args1)
    #for result in cursor.stored_results():
    #        print(result.fetchall())
    #cnt=cursor.rowcount
    conn.commit()
    #return cnt
 
def getMaxIdDoc1():
    conn = connect()
    #integrated security 
    cursor = conn.cursor() 
    cursor.execute('select (ifnull(max(docid),1000)+1) as mxid from documents;')
    mxid=0
    for row in cursor: 
        mxid=row[0]
        print(int(mxid)+1)
    return mxid