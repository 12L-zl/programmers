-- 코드를 입력하세요
SELECT CAR_TYPE, COUNT(*) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%통풍시트%' OR OPTIONS LIKE '%열선시트%' OR OPTIONS LIKE '%가죽시트%'
GROUP BY CAR_TYPE 
ORDER BY CAR_TYPE ;

/*
WHERE OPTIONS IN ('통풍시트', '열선시트', '가죽시트')

오답인 이유 >
IN 연산자는 '통풍시트' 만 있을 때 가능
'통풍시트', '네비게이션' -> X
*/
