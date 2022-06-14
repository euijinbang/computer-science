# JWT

Json Web Token



## 기존의 서버(세션) 기반 인증 방식

- 서버 측에서 사용자 정보를 기억하고 있어야 함
- 따라서 세션을 유지해야 하고, 메모리, 디스크 또는 데이터베이스를 통해 관리
- 클라이언트로부터 요청을 받으면, 클라이언트의 상태를 계속해서 유지하고 정보를 서비스에 이용 == Stateful하다



## 무엇이 문제인가yo?

- 사용자가 인증시 서버에 정보를 저장 => `메모리`에 저장할 때 로그인 중인 사용자가 늘어날 경우 `RAM` 과부하 발생
- `서버 확장`시 세션 분산 시스템 설계 필요
- 쿠키 헤더에 `same-site` 속성이 있는데, 도메인간 쿠키 교환에 대해 추가 설정이 필요. (CORS 정책을 따라야)



---



## 토큰 기반의 인증시스템

인증받은 사용자에게 토큰을 발급하고, 서버에 요청을 할 때 `header` 에 토큰을 함께 보낸다.

더 이상 사용자 정보를 서버나 세션에 유지하지 않기 때문에 상태를 유지하지 않으므로 `stateless` 한 구조를 가진다.





## Stateless 하다는 것

클라이언트의 정보를 서버가 가지고 있지 않다는 것

클라이언트의 이전 요청이 서버로 전달될 때, 서버는 (???)기억하지 못한다. 클라이언트가 다 담아서 보낸다.

- 장점 : 서버 확장성이 높아 트래픽 발생시 대처가능
- 단점 : 클라이언트 요청시 데이터 소모가 많음. 들고 오니까.



> HTTP 클라이언트는 무상태를 특징으로 한다. (상태 비저장 프로토콜)
>
> 물론 일부의 경우 진행 사항을 추적하기 위해 쿠키를 사용하거나, 서버측 세션을 사용하는 경우도 있다.
>
> 그러나 기본적으로 "여러 요청에 대한 상태를 추적할 필요가 없다" 라는 의미에서 Stateless 하다고 하는 것이다.
>
> 기본적으로 trasaction이 종료되면 브라우저와 서버의 연결은 끊어진다.





## token 기반 인증시스템의 장점

- 무상태성과 확장성 : Stateless & Scalability

​	사용자 정보가 클라이언트측에 저장되기 때문에, 어떠한 서버로 요청이 와도 상관이 없다.

- 확장성

​	OAuth 를 통해 소셜 계정을 이용하여 다른 웹서비스에서도 로그인할 수 있다.

- 여러 플랫폼 및 도메인

​	CORS 이슈가 없어서 다양한 디바이스, 도메인에서 사용할 수 있다.



---



## 	JWT

Json 포맷을 이용하여 사용자에 대한 속성을 저장하는 웹토큰



## JWT 구조

- Header + Payload + Signature
- 각 부분은 Base64Url로 인코딩된다.
- Signature는 
  - 1.  header와 payload 의 값을 BASE64Url 로 인코딩
    2. 인코팅한 값을 비밀 키를 이용해 header에서 정의한 알고리즘으로 해싱(HS256, SHA256, RSA)
    3. 이 값을 다시 BASE64URL 로 인코딩



## JWT의 단점?

- Self-contained : 토큰 자체에 정보를 담고 있어 보안에 주의해야
- Payload 보안 : 암호화가 아니라 인코딩 되었으므로 중요 데이터는 넣지 말아야
- Stateless : 상태를 저장하지 않아, 임의 삭제가 불가능하므로 만료 시간을 넣어주어야
- Store Token : 클라이언트 측에서 토큰을 저장해야



---



## CORS 

Cross-Origin Resource Sharing 교차 출처 리소스 공유

" 주어진 도메인 외부에 있는 리소스에 대한 제어된 액세스를 가능하게 하는 브라우저 매커니즘 "



### 동일 출처 정책(SOP) 를 확장하고 유연성을 추가한 것

SOP 는 웹사이트가 서로 공격하는것을 방지하기 위한 웹브라우저 보안 매커니즘

서로 다른 Origin 끼리 데이터 액세스 하지 못하도록 제한



### Origin

`프로토콜` + `주소` + `포트번호`

이 중 하나라도 다르면 허용하지 않는다. 

```
http://www.website.com:80/example
```



## CORS 해결방법

### 1. SOP 를 준수한다.

frontend단에서 요청을 보낼 때 https로 보내면 된다.

### 2. Request에 header(origin header)를 넣어 요청을 보낸다.

어떤 요청을 받을지 모르기 때문에 서버 단에서 처리하는 것이 좋아보인다.

### 3.[추천] 서버에서 모든 출처를 허용하여 Origin Header 여부에 관계없이 Access-Control-Allow-Origin 을 Header에 넣어 Response한다.



## CORS 해결방법 - 서버

### 1. @CrossOrigin

해당 controller에 @CrossOrigin 을 지정한다.



### 2. GlobalConfiguration

 전역 controller 에 설정이 가능하다.

MVC Java config @Configuration 에 설정한다.



### 3. CORS Filter in Spring Security

CorseConfigurationSource 를 통해 CORS Filter를 Spring Security와 통합한다.