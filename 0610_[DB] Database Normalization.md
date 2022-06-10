# Database Normalization

### 데이터베이스 정규화란

 <u>"관계형 데이터 모델에서 **데이터의 중복을 제거**하여 **이상 현상을 방지**하고</u>

**<u>데이터의 일관성과 정확성을 유지하기 위해 무손실 분해하는 과정"</u>** 이다.



"*The process of organizing the columns(attributes) and tables(relations) of a* 

*relational database to **reduce data redundancy and improve data integrity.***"



### 언제 수행하나

데이터 모델이란 현실 세계의 정보를 인간과 컴퓨터가 이해할 수 있도록 추상화하여 표현한 모델이다.

데이터 정규화는 데이터 모델 절차 `개념적 데이터 모델` -`논리적 데이터 모델` - `물리적 데이터 모델`  중

**논리적 데이터 모델 단계**에서 수행한다.



### 이상 현상(Anomaly)이란

- Relation 조작시 데이터들이 불필요하게 중복되어 예기치 않게 발생하는 것. 
- 예를 들어 제품에 따른 가격이 있을 때, 컬러는 가격과는 상관이 없다면 한 테이블에 있을 이유가 없다. 같은 제품인데 새로운 색 제품이 추가될 경우, 가격이 중복되어서 들어간다.



### 데이터베이스 정규화 단계

- 1정규형 : 하나의 column 에는 하나의 value 만 들어가야 한다.
- 2정규형 : 부분 함수 종속 제거
- 3정규형 : 이행 함수 종속 제거



### 참고자료

- https://www.udemy.com/tutorial/sqldatabases/what-is-database-normalization/