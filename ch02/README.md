## AWS 소개
- Amazon

![스크린샷 2021-10-11 오후 7 18 22](https://user-images.githubusercontent.com/18282470/136774246-91122b5f-1385-45e4-9c56-94547b1d25af.png)

- AWS 글로벌 인프라 맵

![스크린샷 2021-10-11 오후 7 22 20](https://user-images.githubusercontent.com/18282470/136774782-7b698316-d719-496c-a17a-2d7505076810.png)
> 출처: AWS(https://aws.amazon.com/ko/about-aws/global-infrastructure/)

- AWS 인프라

![스크린샷 2021-10-11 오후 7 24 48](https://user-images.githubusercontent.com/18282470/136775095-8dc2a174-dcf8-4426-b70f-67a52992a1ba.png) 

## 어플리케이션 및 아키텍쳐 소개
- 어플리케이션 소개 (개요)
  * 컨퍼런스 참가 시스템 제작 예정
- 어플리케이션 흐름
  * 참가신청 화면 (신청서 작성 및 전송)
  * 신청내역 화면 (신청내역 리스트업)
  * 신청결과 화면 (참가증 확인)
- 어플리케이션 제작시, AWS 사용 서비스
  * Lambda
  * S3
  * DynamoDB
  * CloudFront
  * API Gateway
  * SNS
- 아키텍쳐 호스팅
  * client -> CloudFront(캐시) -> S3(html, css, js, 이미지...)
- 아키텍처 - Business logic

![스크린샷 2021-10-11 오후 7 43 13](https://user-images.githubusercontent.com/18282470/136777442-980ca1f3-a61f-4c03-af9b-c2556029fb9b.png)
> 여기서 Lambda에 SNS를 붙인 이유는 이미지를 빌드하는 시간동안 클라이언트가 기달려야 하기때문에 이것을 비동기적으로 처리하기 위해서 알람을 통해서 아키텍쳐를 구성하였다.

## 실습환경 준비
- AWS 가입하기
  * 홈페이지 접속 -> 계정생성 클릭 -> 개인계정 선택 및 정보입력 -> 결제정보 입력(1달러 추후 취소) -> 기본 계획지원 선택 
- 개발환경
  * OS: MAC
  * Language: Python 3.7
  * IDE: VSCode
  * AWS CLI
  * Docker
``` bash
yum install
yum install python3
pip install virtualenv
mkdir venv && cd venv
virtualenv -p /usr/bin/python3 py37
source {path} activate
pip install awscli
```
