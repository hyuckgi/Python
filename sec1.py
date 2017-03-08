# Sonic Python Lecture 2017.03.04
# -*- coding: utf-8 -*-

'''
    플러그 인이 너무 많을 때에는 package.json처럼 리스트를 관리할 수 있다.

    설치된 패키지 목록을 파일로 얻기
    pip freeze > requirements.txt

    설치가 필요한 프로젝트 목록을 통한 프로젝트 설치
    pip install -r requirements.txt

    로컬호스트에서 shell을 대체할 수 있는 notebook
    pip install 'ipython[notebook]'
    로컬 파일을 에디팅 할 수 있다.

    한글을 넣고 싶으면
    파일 맨 상단에
    # -*- coding: utf-8 -*-

    메인함수가 필요하면
    if __name__ == '__main__':
        pass


    # 내장함수
        dir : 속성과 메서드의 리스트를 보여준다.
        >>> dir('a') #JS console.dir(a);

        help : 내부의 사용법을 볼 수 있다.
        >>> help("string".strip)

        id : 주소값을 확인할 때 사용
        >>> id(1)
        140361196419848

        raw_input : 사용자로 입력받기
        >>> name = raw_input('what your name?')
        Sonic
        >>> print name
        Sonic

    #변수
        # 타입체크
            >>> type('code')
            <type 'str'>
            >>> type(i)
            <type 'int'>
            >>> type(pi)
            <type 'float'>

        # 다중할당
            >>> x, y, z = 1, 2, 3
            >>> print x
            1
            >>> print z
            3

    #연산자
    하나 이상의 연산자가 등장할 때 연산자는 순서 규칙을 따른다.
        1.괄호
        2.제목
        3.곱셈과 나눗셈
        4.덧셈과 뺄셈
        5.같은 실행 순위는 왼쪽 -> 오른쪽

    #자료형
        리스트형 - 내부의 값을 나중에 바꿀 수 있다.
        튜플(tuple)형 - 한 번 값을 정하면 내부의 값을 바꿀 수 없다.
        사전형 - 내부의 값을 나중에 바꿀 수 있다.
        집합형 - 중복을 허락하지 않는다. 변경 가능하게도, 변경 불가능하게도 만들 수 있다.


    #사전형에서 key가 없으면 에러가 난다. 이것을 회피하기 위해
        print key 보다
        .get('key', 'default value') 를 쓴다.
        >>> name = {}
        >>> name['sonic'] = 'Lee Kwang Woon'
        >>> name['sonickal']  # error

    # 반복문으로 파일 읽기
        >>> f = open('test.txt', 'r')
        >>> for line in f:
        ...     print line
        ...

    #range 리스트 생성 : 메모리를 많이 먹는다
        >>> range([시작값 = 0], 종료값, [증감분 = 1])
    #xrange :xrange()로 생성되는 객체는 검색이 요청되는 시점에 값을 계산,매우 큰 범위를 표현할 때는 사용하는 것이 좋다.

    #리스트 메소드
        slice : [[시작위치 = 0]:[끝위치 = last]:[증감분 = 1]]
            >>> string[0:10:2]
        append,
        pop,
        remove,
        insert(넣을 위치, 넣을 값),
        index
        count,
        sort
        reverse


    #리스트 함축구문
        >>> # 목록 함축을 사용하여 목록에서 각각에 숫자에 2를 곱함
        >>> # 목록 함축은 새로운 목록을 반환함에 유의
        >>> num_list = [1, 2, 3, 4]
        >>> [num * 2 for num in num_list]
        [2, 4, 6, 8]

        >>> # 목록 함축을 변수에 할당할 수 있다
        >>> num_list2 = [num * 2 for num in num_list]
        >>> num_list2
        [2, 4, 6, 8]

        [원소 (옵션 식) for 원소 in 목록 (옵션 절)]

        enumerate(리스트) : 리스트에 index를 제공
        >>> for index, value in enumerate([1,2,3,4])
        ...     print index, value

    #사전형
        age = {}
        age['george'] = 10
        age['fred'] = 12
        age['henry'] = 10
        print age['fred']  # 12

        # 빈 사전 및 채워진 사전을 생성
        >>> myDict={}
        >>> myDict=dict()
        >>> myDict.values()

    #튜플
        튜플은 변경불가하다.
        변경을 하고 싶을 때는 리스트로 형변환을 하면 된다.

        q) 튜플을 리스트로 다시 바꾸는 방법

    #문자열
        곱셈이 가능하다
        >>>print "a"*10 #aaaaaaaa

        문자열 포멧팅
        >>> "name is %s, %s" %(x, y)
        print "My name is %s" % "Sonic"
        print "My age is %s" % "20"
        print "My age is %d" % 20

        C스타일
        "%s %s" % ('Hello', 'World')
        'Hello World'

        PEP 3101 스타일
        "{0} {1}".format('Hello', 'World')
        'Hello World'

        키를 이용한 포매팅
        >>> print '%(language)s has %(number)03d quote types.' % \
        ...       {"language": "Python", "number": 2}
        Python has 002 quote types.

    #함수
        함수문법
        def functionname( parameters ):
           "function_docstring"
           function_suite
           return [expression]

        def 함수명(인자목록):
            구현부

        return을 지정하지 않으면 None을 반환

        필수인자
        >>> def print_hi(str):
        ...     print 'hi' + str
        ...
        >>> print_hi()

        키워드 인자
        def print_me( str ):
           "This prints a passed string into this function"
           print str
           return

        print_me( str = "My string")

        My string

        기본인자
        def print_info( name, age = 35 ):
           "This prints a passed info into this function"
           print "Name: ", name
           print "Age ", age
           return;

        print_info( "miki", 50 ) #기본 사용
        print_info( age=50, name="miki") #키워드로 전달하면 순서에 상관없다
        print_info( name="miki" ) #default인자가 있기때문에 오류가 안난다.

    #파일시스템
        open(파일명, 모드) : 반드시 close가 이어져야 한다.

        with open(파일명, 모드) as fh:
            fh.write()

        import 모듈명

        from 패키지 import 모듈명

        import Besdsdadasdad as b  #별칭 b로 사용가능

        os.walk(dir) : dir경로의 파일들은 하나하나 튜플형태로 반환한다.

        etc : os, glob, shutil, sys, process, command

    #JSON
        import json
        >>> json_encoded = json.dumps(data)
        >>> decoded_data = json.loads(json_encoded)

        httpie http request헤더, 바디로 볼수 있다.

    #인터넷
        urllib2 : 다른 인터넷 페이지를 열수 있다. 복잡해서 안쓴다.
        import requests 이거를 쓴다, restfulAPI

    #브라우저 호출
        import webbrowser

    #Beautiful Soup 모듈 : requests로 받아온 html을 객체형태로 변환 & 계층구조로 태그에 접근할 수 있다.
        find(a), find_all(a) 등의 메서드와 css selector를 사용할 수 있다.
        * select('.className'), selector는 없으면 빈 리스트가 반환된다.
        * crawler를 하려면 반드시

    #pillow : 이미지 편집 모듈
        이미지의 확장자를 일률적으로 바꿀때 사용할 수 있다.
        resize((200,200)), save("path", format), rotate(deg), crop(x,y,width,height)
        텍스트 넣기(text()), 그리기
        (draw()), 썸네일 만들기(thumbnail())

    #csv, excel파일 컨트롤


    #예외처리 표현
        try-except
            try:
                return x/y
            except ZeroDivisionError:
                return 'You cannot divide by zero, try again'

        try-except-finally
            try:
                # 예외를 유발할 수 있는 작업을 수행
            except Exception, value:
                # 예외 처리를 수행
            finally:
                # 항상 완료되어야하는 작업을 수행(예외를 발생시키기 전에 처리됨)

        try-finally
            try:
                # 예외를 유발할 수 있는 작업을 수행
            finally:
                # 항상 완료되어야하는 작업을 수행(예외를 발생시키기 전에 처리됨)

        try-except-else
            try:
                # 예외를 발생시킬 수 있는 작업을 수행
            except:
                # 예외 처리를 수행
            else:
                # 아무 예외도 던져지지 않았을 때에만 할 일을 수행

        예외정보 보기 : sys.exc_info()

'''
