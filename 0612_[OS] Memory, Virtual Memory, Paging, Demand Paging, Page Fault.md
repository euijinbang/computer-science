# Memory

### 메모리란?

컴퓨터 안의 storage space로 CPU에 의해 실행될 프로그램이 저장되는 곳이다.



### 메모리의 종류

1. **Primary Memory(주기억장치) **(CPU 가 2순위로 접근)

   - RAM : Random Access Memory (DRAM)
   - ROM : Read Only Memeory (PROM, EROM)

2. **Secondary Memory(보조기억장치)** (CPU가 바로 접근하지 않고 I/O Processor 통해 접근)

   - Magnetic Memory : Hard Disk
   - Optical Memory : CD

3. **Cache memory, buffer** (CPU 가 1순위로 접근)

   주기억장치 접근 시간이 프로세스 논리회로보다 오래 걸리기 때문에, 진행되고 있는 프로그램의 일부 또는 사용빈도가 높은 데이터를 저장한다.

   - SRAM



### Logical vs. Physical Address

- **논리 주소 Logical address** : `프로세스`마다 독립적으로 가지는 주소 공간으로, 각 프로세스마다 0번지부터 시작한다. 
- **물리 주소 Physical address** : 물리 메모리에 실제 올라가는 위치이다.
- **주소 바인딩:** `Symbolic Address(변수이름, 함수이름)` - (컴파일) - `Logical Address(숫자값)` - (주소 바인딩) -  `Physical address`



### Memory Management Techniques

1. Dynamic Loading
   - 프로세스 전체를 메모리에 미리 다 올리는 것이 아니라 해당 루틴이 불려질 때마다 메모리에 올린다.
   - 운영체제가 해주는 것이 아니고 프로그래머가 설정한다. (OS 라이브러리 사용)

2. Overlay

   - 메모리에 프로세스 부분 중 실제 필요한 정보만 올린다.

   - 프로그래머가 직접 코딩한다.

3. Swapping
   - 프로세스를 일시적으로 메모리에서 backing store(하드디스크)로 쫓아내거나 데려온다.





# Virtual Memory

### 가상메모리?

메모리 관리기술의 일종으로, "idealized abstraction of the storage resources" 를 제공.

하나의 프로세스마다 충분히 물리메모리를 할당하기에는 메모리 크기가 한계가 있다.

A, B, C, ...**멀티 프로세싱 하려면... 공간이 부족하다!**

그래서 물리메모리 **`RAM`  Physical memory** 를 가상화한다.



OS 는 프로그램에 의해 사용되는 메모리 주소(memory addresses) 를 컴퓨터 메모리의 물리 주소(physical addresses) 매핑한다.



### Paging 기법을 사용하여 주소를 매핑한다.

Process 의 virtual memory를 동일한 사이즈의 page 단위로 나눈다.

일부는 backing storage에, 일부는 physical memory에 저장한다.

- page: 고정된 크기의 block (4KB)



### Virtual Address로 Pysical Address를 찾는 과정

1. **OS 요청**
2. **Process 가상 주소를 확인**
3. **Page Table 통해 가상주소로 물리주소 확인**
4. **Physical Address 로 물리메모리에서 찾아 반환**



### 보기

- 핵심은 Page Fault 에 관한 처리이다.
- 응용 프로그램 실행시 사용하는 메모리 주소는 전부 가상 주소로, 물리주소와 다르다.
- 처음 프로그램 실행시 page fault가 발생한다. 이유는 대부분의 운영체제에서 요구 페이징 기법(demand paging) 을 사용하기 때문이다.
- 물리 메모리는 응용 프로그램 단위로 한꺼번에 disk에서 code와 data를 가져오고 해당 응용 프로그램 실행이 끝나면 한꺼번에 점유했던 메모리 영역을 해제한다.(x)



# Demand Paging

### 디맨드 페이징이란?

- 프로세스의 모든 데이터를 미리 메모리에 올리는게 아니라, 실행 중 필요한 시점에서 적재하는 것이다.

- 프로세스의 요청이 있을 때, 페이지가 `second memory`로 부터 `main memory` 로 불러와져야 하는 것이다.

- 페이지가 main memory에 없다면 second memory에서 불러온다. 



# Page Fault

### 페이지 폴트란?

- 어떤 페이지가 실제 물리 메모리에 없을 때 일어나는 인터럽트
- page fault 가 일어나면, OS는 해당 페이지를 물리 메모리에 올린다.
- 페이지 폴트가 자주 일어나면 프로세스 시간이 오래 걸린다.



### 참고자료

- http://www.kocw.net/home/search/kemView.do?kemId=1046323

- https://www.udemy.com/course/operating-system-crash-course-for-beginners-ignou-part-1/learn/lecture/30319124#overview

- 기타 인터넷 강의