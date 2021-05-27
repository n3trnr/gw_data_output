# gw_data_output
aws_lambda_groupware_data_output


그룹웨어에서 최근 20분간 변경된 사용자 DB 정보를 AWS DB로 POST 방식으로 호출해서 넘겨주는 람다입니다.

기본 AWS 람다에서 지원하지 않는 라이브러리(requests, psycopg2)가 있기에 AWS 람다 콘솔패널에 있는 계층에 Zip 파일을 추가해서 계층을 만들고 붙여야 작동합니다.

requests : GET, POST url 호출시 사용되는 라이브러리

psycopg2 : PostgreSQL DB 접속 및 쿼리 명령어 사용시 필요한 라이브러리


This is a python file for AWS Lambda allows to put recently(20 min) changed users info in groupware DB to internal AWS main DB by POST

you need to add layers to AWS Lambda panel to call python libraries
