# 정규표현식 사용하기

```python
 import re # 일단 임포트부터 하자 
 result = re.match('Lux', 'Lux, the Lady of Luminosity')
 # 첫번째 인자는 '패턴', 두 번째 인자는 문자열 소스
 # 패턴 자체가 복잡하면 아래와같이 변수화해서 쓰면 된다.
 pattern = re.compile('Lux')
```


#### match

시작할때부터 일치하는 '패턴'을 찾는다.  

```python
pattern = re.compile('Lux')
m = re.match(pattern, 'Lux and Lux')
print(m.group()) #다음과 같이 .group()을 써서 문자열을 찾는다.
```

#### search

특별한 것 없다. match와 비슷한 방식으로 사용하면 된다. 다만 match가 ==문자열의 시작이 패턴과 일치할때만== 반환한다면 search의 경우에는 가장 먼저 발견하는 첫 패턴만 반환하는 특징이 있다.


#### findall

해당 문자열 소스 안의 패턴과 일치하는 모든 부분을 **리스트** 형태로 반환한다.
때문에 m.group()과 같은 메소드로 찾은 문자열을 부를 필요가 없다.

#### split
기존 파이썬 split과 비슷한데 정규표현식 패턴을 받아들이기 때문에 더 강력하다.
마찬가지로 패턴을 기준으로 잘라내고 리스트 형태로 반환한다.

***

## 정규표현식의 패턴 문자

숫자, 문자, 공백 문자, 단어 경계 등을 나타내는 패턴 문자가 있다.
d w s b (반대의 경우에는 대문자처리)

(expr), |, ^, $, ?, *, +, {m}, {m, n}?, expr1(?=expr2) (?<=expr1)expr2 등의 조합을 써서 확장시킬 수 있다. 
실습 문제를 미리 풀어보면서 연습해보자

#### 매칭 결과 그룹화

```python
s.group(1) ## 이런식으로 그룹요소를 리턴할 수도 있고,
	
m = re.search(r'(?P<before>\w+)\s+(?P<was>was)\s+(?P<after>\w+)', story) ##  
m.groups()
m.group('before')
m.group('was')
m.group('after') ## 아예 이런식으로 키워드를 붙여서 검색하는 것도 가능하다.
```

#### 실습 풀어보기

**1번 문제**

```python
m = re.findall(r'(?<!\w)a\w{3}(?=\W)', story)
# 1. r'로 시작한다(패턴 사용할때 인식오류 없이 해야하니까)
# 2. (?<!\w)를 앞에 넣어서 패턴 앞에는 문자가 없게 한다. 이를 통해 a로 시작하지 않는 패턴을 걸러낼 수 있다.
# 3. a\w{3} 을 넣어서 a로 시작하고 그 뒤에 문자가 3개 들어오는 패턴을 찾는다.
# 4. (?=\W) 마지막으로 왼쪽의 조건을 붙여서 찾은 패턴 뒤에 오는 것은 무조건 문자가 아니게 만들어서 단어의 길이가 4를 초과하면 걸러내게 만든다.
```

**2번문제**

```python	
m = re.findall(r'\w+r(?=\W)', story)
```

**3번문제**

```python
m = re.findall(r'[abcde]{3}\w+', story)
```
