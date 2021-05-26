import boto3
import json
import psycopg2 #PostgreSQL 과 연결하려면 반드시 있어야 되는 드라이버 (람다에서는 레이어 붙이는걸로 처리 가능)
import requests

def lambda_handler(event, context):
    
    print('db connect')
    conn = psycopg2.connect(host='gw.refinehub.com', dbname='tims', user='refine', password='refine2164!@', port='5432') #DB 접속 구문 
    print('db connect success!')
    cur = conn.cursor() #커서 생성 (쿼리 칠 때 필요함)
    print('start query')
    
    qry_origin = "select status, empno, username, mailaddr, deptcode, deptname, positionname, updated_at from view_user where updated_at >= current_timestamp + '-20 minute' and deptcode not like 'E%' and positionname is not null order by updated_at desc"
    qry = "select row_to_json(tmp) from ("+ qry_origin +") tmp;" #쿼리문 (row_to_json으로 바로 JSON 형식으로 뽑아다줌)
    
    cur.execute(qry) #쿼리 실행
    rownum = int(cur.rowcount)  # DB 총 행 개수 구하기
    print(rownum)
    
    i=0
    while i < rownum: #쿼리 결과 값 나온 행 수 만큼 반복해서 
        result = cur.fetchone()[0] #cur.fetchone()로 한 행 결과값 묶어주기 (fetchall() 을 호출하면 전체 행 값이 나옴) ([0] 을 넣어줘야 대괄호나 괄호가 안생김)
        req_url = requests.post('https://intra.refinehub.com:7075/RF_COUNT/minsu/insertUsr', json = result) #결과 값 URL 호출
        print(result)
        print(req_url)
        i = i + 1
   

    cur.close()
    conn.close()

