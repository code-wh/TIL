# Interface와 OS 

## Computer Interface의 종류

### Interface: 서로 다른 두 존재가 만나는 접점  

*ex) HDMI, 모니터, 마우스, 컵의 손잡이 등*

* CLI (Command Line Interface)
* GUI (Graphic User Interface)
*-> 기존에 보던 화면은 GUI, 개발하는 사람들이 배워야할 것은 CLI*

### 운영체제

- Windows: DOS> 95/98> XP> 7> 10

- UNIX: 또 2개로 나뉨 (무료와 유료)

  - Mac OS(유료), IOS 
  - 리눅스(무료, **Linus Torvalds**가 배포)



# Git 사용법 및 터미널 명령어 정리

## Git & Github 란? 
1. Git을 이용한 버전 관리
- Version Control System
- 백업, 복구, 협업

2. Github를 이용한 포트폴리오
- hub: 모여있는 곳

  


## 기본 명령어

* `cd (change directory)`: 작업 중인 디렉토리 위치 변경
  * cd ../: 상위 폴더로 이동,  cd ./: 현재 폴더로 이동

* `pwd(print working directory)`: 현재 작업 중인 경로 출력

* `mkdir(make directory)`: 디렉토리(폴더) 생성

* `touch`: 파일 생성

* `rm(remove)`: 파일 삭제
  * rm -rf: 디렉토리 삭제
  
* `rmdir`: 빈 디렉토리 삭제

* `ls(list segments)`: 디렉토리나 파일의 정보 출력
  * ls -a: 숨겨진 파일의 목록까지 출력
  
    

## 저장소 초기화

폴더=>리포

```
$ git init
```

리포=>폴더

```
$ rm -rf .git/ 
```



## 터미널로 Git 명령하기

### Git을 사용한다는 것은 CF광고를 촬영하는 것 !

#### 순서: 분장실->스테이지(무대)->촬영(메모리)->결과물 전달

* `git status`: 레포지토리의 상태를 보여주는 명령어
* `git add`: 파일을 staging area로 옮기는 명령어
* `git commit -m '<name>'` : stage에 있는 파일을 repository에 저장하는 명령어
* `git push origin master`: local repo에 있는 파일을 remote repo에 보내는 명령어

