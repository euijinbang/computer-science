# DataStructure



## Array 배열

- 정의 : 데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
- 필요 : 같은 종류의 데이터를 효율적으로 관리. 같은 종류의 데이터를 순차적으로 저장
- 장점 : 빠른 접근 가능
- 단점 : 추가와 삭제가 쉽지 않다. 미리 최대 길이를 지정해야 한다. 데이터를 추가하고 싶다면 최악의 경우 배열을 새로 만들어야 한다. 또한 중간 공간을 삭제하면 뒤의 데이터를 당겨야 한다.

### 파이썬 배열은 뭐가 다를까?

- 파이썬은 '배열' 대신 '리스트' 를 사용한다.

### 정수와 변수 서식 지정

- `%d` : 정수를 10진수로 표시 (decimal integer)
- `%f` : 실수 (float)
- `%c` : 문자 하나('로 둘러싼 반각 문자 하나) (character)
- `%s` : 문자열("로 둘러싼 문자) (string)

---



## Queue 큐

- 정의 : 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조이다. 
- `FIFO` : First In, First Out.



### Terms

> 리스트를 활용하여 다음 기능을 함수화하여 직접 만들어볼 수 있다. append(), 인덱스 활용, del[인덱스] 를 사용한다.

- `enqueue()` : put data
- `dequeue()` : get data



### Python queue library

> import queue 하여 queue라이브러리를 불러오고, queue.Queue() 로 클래스를 통해 인스턴스를 생성해 사용하면 된다. 이때 사용되는 메서드는 put() 과 get() 이다.

- `Queue` : 일반적인 FIFO Queue
- `LifoQueue` : LILO Queue (Last In, First Out)
- `PriortyQueue` : (priority, value)



### 🦊 Usage

- 운영체제에서 멀티태스킹을 위한 프로세스 스케쥴링 방식 구현에 사용한다.
  - 새로운 프로세스가 수행되어야 한다면, 이전에 `메모리`에 올라가있던 프로세스를 종료하고 새로운 프로세스를 메모리에 올린다.




## Stack 스택 

- 정의 : 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 구조
- `LIFO` : Last In, First Out

### Terms

- `push()` : put data
- `pop()` : get data

### Usage

- 컴퓨터 프로세스 구조의 함수의 동작 방식
- 재귀함수

### Advantages & Disadvantages

- Adv
  - simple, easy to implement
  - fast data access speed
  
- Disadv
  - need to set max size
  - limited memory size
    - python recursive : max 1000 times
  - redundant data storage
  ß
