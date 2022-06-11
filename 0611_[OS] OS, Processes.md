# OS

### OS란?

`computer hardware` , `software resources` 를 관리하고 컴퓨터 프로그램을 제공하는 system software



### a computer system

**Hardware - OS - Application - User**



### OS의 기능

- **Process 관리**
- **Memory 관리**
- **File 관리**



# Process

### 프로세스란?

실행중인 프로그램 "a program in execution"



### Process States

- New 
- Ready
- Running
- Waiting / Suspended / Blocked
- Terminated



### Implementation of Process - Context Switching

- Context Switching? A switching of CPU from one process to another.



### Implementation of Process - Threads

- independently scheduled parts of a single program.
- parallel하게 실행되거나 common data 를 공유하는 여러 개의 sub-process로 구성되어 있다면 task가 multithreaded 된 것.



### 비교

| 프로세스                | 스레드                                                       |
| ----------------------- | ------------------------------------------------------------ |
| 전용 메모리 공간을 확보 | 여러 개의 스레드가 메모리 공간을 공유<br />JVM 도 하나의 프로세스로 내부에 여러 스레드 존재 |



### Thread 는 전역 변수를 공유하는가?

-



### 참고자료

- https://www.udemy.com/course/operating-system-crash-course-for-beginners-ignou-part-1/learn/lecture/30312530#overview

- 그림으로 공부하는 IT 인프라 구조