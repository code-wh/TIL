# Git 사용법 (실습.ver)

[참조]: https://www.zerocho.com/category/Git



## Git 이란?

- Git은 <u>버전관리 시스템</u>(VCS, Version Control System)

- Gitbub는 Git의 데이터를 저장하는 서버

### Git을 쓰는 이유

1. **백업**
   - 이전 버전을 자동으로 저장해서 에러를 두려워하지 않고 다양한 버전 개발 가능
   - 버전마다 어떤 부분이 수정되었는지 기록 가능
2. **협업**
   - 여러개의 개발팀이 있어도 어떤 부분이 충돌하는지 쉽게 알려주고 피해갈 수 있음
3. **분산**
   - 각자의 컴퓨터에 분산 저장하여 서버가 터질 때 대비 가능 



## Git 저장소 생성 / commit 해보기 (Local)

1. Git에 연동할 프로젝트 폴더와 파일 생성

2. 명령 프롬프트(cmd, git bush 등)로 프로젝트 폴더로 이동

   - cd [경로] 명령어 사용

3. Local repository 생성

   - git init 명령어 사용

4. 현재 파일들의 상태 확인

   - git status 명령어 사용

5. Commit 할 파일들 올려주기 (스테이지에 올리는 단계)

   - add 명령어 사용

   - add된 파일을 다시 untracked 하려면 rm 명령어 이용

6. add된 파일들 Commit 해주기

   - git commit -m '설명'
   - 로그인을 안한 경우 에러 뜸 -> 정보등록
     - git config --global user.email "내 이메일"
     - git config --global user.name "내 이름"
   - git commit -am '설명' 을 통해 add와 commit 동시에 가능

7. commit된 내역 확인
   - git log 명령어 이용



## Github 계정 생성 / push, clone, pull (Remote)

1. Github 회원가입

   - https://github.com/

2. Github 저장소 생성

   - +버튼을 누르고 new repository
   - repository: 저장소; 데이터 집합체가 보관되고 조직적인 방식으로 유지되는 저장장치 내의 주요 장소

3. ![image-20220116172516066](Git 사용법 (실습.ver).assets/image-20220116172516066.png)

   - Code: 현재 저장된 코드
   - Issues: 남들이 나의 저장소를 쓰는데 문제가 발생할 경우 문제를 제기하는 공간
   - Pull request(PR): 남들이 코드를 직접 수정해서 올려주는 곳
   - Watch: 저장소에 변화가 있을 때 알림이 오게 설정
   - Star: '좋아요' 기능
   - Fork: 남의 저장소를 복사하여 내 저장소에 붙여넣기 하는 기능

4. Local repo(내 컴퓨터)에서 Remote repo(Github)로 전송

   - git remote: 원격 저장소를 관리하는 명령어

   - 원격 저장소 주소 등록

     - git remote add origin https://github.com/[github이름]/[remote repo이름]

       -> github 내의 remote repo를 origin 이라는 이름으로 주소 등록 시켜줘

   - 원격 저장소에 commit 저장

     - git push origin master
       - origin: 원격 저장소 이름 / master: 현재 사용하는 컴퓨터의 브랜치 이름
       - 깃허브 계정으로 로그인하면 push 완료

5. git pull

   - 다른 사람이 PR을 통해 코드를 업데이트했거나, Github를 통해 commit을 했을때 클라이언트로 내려받는 명렁어
   - git pull origin master
     - origin의 내용이 master로 복사

6. git clone

   - 클라이언트 상에 아무것도 없을때 서버의 프로젝트를 내려받는 명령어
   - git clone [저장소 주소]
     - 자동으로 init도 됨