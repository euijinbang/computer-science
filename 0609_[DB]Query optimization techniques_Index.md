# Query optimization techniques

왜 쿼리 최적화가 필요할까?

데이터베이스에 접근하는 횟수를 최대한 줄여야 하는 이유는

데이터베이스는 데이터를 하드디스크에 저장하기 때문이다.

CPU가 데이터를 요청했을 때 해당 메모리에서 데이터를 가져오는 클럭 수를 비교했을 때

`레지스터` < `캐시` < `메인 메모리` < `하드디스크` 순이다.

즉, 하드디스크에서 데이터를 가져오는 것은 그만큼 리소스가 많이 필요하다.



## Index

### What is index?

"a file with a sequence of pairs of keys and pointers."

자주 필터링하는 컬럼에 인덱스를 추가하여 데이터베이스 검색 속도를 향상시키는 방법.



### Role?

데이터베이스 search 속도 향상

특정 컬럼 밸류를 가진 row 를 찾도록 한다. 모든 row 중 일부 row 만 찾아본다.

잘못 디자인된 인덱스와 불충분한 수의 인덱스는 database bottleneck의 주요 원인이다.

효율적인 디자인은 매우 뛰어난 성능을 가져온다.



### 인덱스가 필요 없는 경우

- In case of small tables  -- 전체를 읽는게 더 빠르다.
- massive data update or insert  -- 대규모 일괄 업데이트 작업이 자주 실행되는 경우에는 성능이 느려진다. Data Insertion 동안 계속해서 index가 재연산 되기 때문이다.(recalculation of index) (B트리가 계속 생성되기 때문이다.)  그래도 만들고 싶다면 data insertion 전에 인덱스를 제거하고, insert 후에 추가하라.

- 즉, 더 이상 탐색하지 않을 경우 반드시 삭제하는게 좋다. 레코드의 삽입과 삭제가 빈번히 일어나면 인덱스 연산(insert의 split 이나 delete 연산의 donate, merge) 등이 발생하여 데이터베이스 성능을 크게 저하시킬 수 있다.



###  B-tree : the most commonly used index type

- organized as `a balanced tree with ordered keys`

- 가장 일반적인 인덱스 타입으로, a balanced tree with ordered keys 형태로 조직된다.

- 테이블의 사이즈에 맞는 인덱스 레벨을 자동적으로 유지한다.



### example

데이터베이스에서 테이블을 만들면 자동으로 B+ 트리로 구성된 인덱스가 생성된다.

**SELECT 구문의 WHERE 절은 B 트리에서 키를 탐색하는 데 사용한다.**

example 테이블의 ID 는 `primary key` 이기 때문에 이미 `B 트리`의 `키` 이기 때문에 빠른 속도로 탐색 가능하다.

하지만 이름의 경우에는 모든 레코드에서 선형탐색 하니 `O(n)` 이나 걸린다.

**이때, 'name'에 대해서 인덱스를 생성하면 `name`을 키로 B트리로 구성한다.**

| ID   | name   |
| ---- | ------ |
| 1    | 홍길동 |
| 2    | 이순신 |

- 인덱스 부여

```sql
CREATE INDEX idx_name ON example(name);
```

- 검색

```sql
select * from example
where name like '이순신';
```





### 참고자료

- https://www.udemy.com/course/query-optimization-techniques-in-sql/learn/lecture/30863828#overview

- 파이썬으로 배우는 자료 구조 핵심 원리
