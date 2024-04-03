-- 코드를 입력하세요
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME ;

/*
%Y : 2000
%y : 00

%M : DECEMBER
%m : 12

%D : 1st(월)
%d : 01(일)
%e : 1(일)

%W : MONDAY
%a : MON

%H : 23
%h : 11
%i : 00(분)
*/