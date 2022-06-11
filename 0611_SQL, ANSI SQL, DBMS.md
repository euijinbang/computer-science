# SQL

Structure Query Language(구조적 질의어). 데이터 베이스를 검색 및 조작 관리하는 언어.



SQL은 다음과 같이 5가지 종류로 나눌 수 있다.



**1. Query문 or DQL문(Data Query Language)** : 데이터 질의 언어, SELECT문의 6가지 절
  ` SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY` 



**2. DDL문(Data Definition Language)** : 데이터베이스 객체의 구조를 정의
  `CREATE, ALTER, RENAME, DROP`



**3. DML문(Data Manipulation Language) :** 데이터의 삽입, 삭제, 갱신 등을 처리
 ` INSERT, UPDATE, DELETE, MERGE` 



**4. DCL문(Data Control Language) :** 데이터베이스 사용자의 권한을 제어
  `GRANT, REVOKE`



**5. TCL문(Transaction Control Language) :** 트랜잭션 제어 언어
  `COMMIT, ROLLBACK, SAVEPOINT`





# ANSI SQL

**American National Standards Institute(미국 표준 협회)**가 각기 다른 DBMS(Oracle, MySQL 등)에서 공통적으로 사용할 수 있도록 고안한 표준 SQL문 작성방법



### 특징

- 표준 SQL문이기 때문에 DBMS의 종류에 제약을 받지 않는다. (MySQL, Oracle)
- 공통 SQL 기능만 제공하며 각 DBMS 업체 및 제품별 고유 기능은 지원하지 않는다.





# DBMS

### 정의

데이터베이스 관리 시스템

데이터베이스 생성, 사용을 관리, 질의를 처리하는 소프트웨어



### 특징

- OS 입장에서 DBMS는 하나의 프로그램이며 설치 삭제가 가능하다.
- 응용 프로그램들은 DBMS를 통해서만 DB 이용이 가능하다.