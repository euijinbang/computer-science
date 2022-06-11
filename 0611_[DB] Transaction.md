# Transaction

### 트랜잭션이란?

- 트랜잭션은 데이터베이스 시스템에서 하나의 논리적 기능을 수행하는 단위이다.
- 많은 사람들이 동시에 데이터베이스에 접근하여 사용하는데, 데이터베이스 **일관성**을 유지하기 위해 **동시성 제어**가 필요하다.
- 여러 SQL 문을 **하나의 트랜잭션**으로 취급하기 위해 사용자가 명시해야 한다.

```sql
Begin transaction Reservation
	begin
		input();
		/*SQL*/
		/*SQL*/
		if 조건
			then ...;
				Abort
			else
		/*SQL*/
		Commit
		output('Done');
	endif
end. (Reservation)
```



### 트랜잭션의 특징 ACID

- **원자성 Atomicity** : 한 트랜잭션 내의 모든 연산은 모두 수행되거나 모두 수행되지 않거나 둘 중하나다.
- **일관성 Consistency** : 트랜잭션 수행 전 데이터베이스는 일관된 상태를 가져야 하고, 트랜잭션 수행 후에도 마찬가지다.
- **격리성 Isolation** : 한 트랜잭션이 데이터를 갱신하고 있다면 이 트랜잭션이 완료되기 전에는 갱신 중인 데이터를 다른 트랜잭션에서 접근하지 못하도록 격리해야 한다.
- **영속성 Durability** : 한 트랜잭션이 완료되면 그 결과는 영속적으로 데이터베이스에 저장된다.



### Atomicity : Commit, Rollback = TCL(Transaction Control Language)

- `Commit` : 완료, 트랜잭션 확정
- `Rollback` : 철회, 트랜잭션 취소

### Consistency : 동시성 제어, Concurrency control

- 여러 사용자들이 다수의 트랜잭션을 동시에 실행시, 트랜잭션 간 간섭 없도록 한다.
- `locking` 로킹 기법
  - 데이터 항목 갱신시 독점 로크
  - 데이터 항목 읽을 때 공유 로크 요청

### Durability : 회복, Recovery

- 트랜잭션 도중 장애로 손실된 데이터베이스를 손상 이전의 상태로 복구시키는 작업
- 어디에 저장하나?
  - 비휘발성 장치(디스크 등) 2개 이상에 사본을 중복 저장한다. `stable storage` 
- `로그` 기반으로 즉시 갱신

- 고장 발생 전 트랜잭션 완료 명령 수행 => 트랜잭션의 갱신 사항 재수행 `REDO`
- 고장 발생 전 트랜잭션 완료 명령 미수행 => 트랜잭션의 갱신 사항 취소 `UNDO`