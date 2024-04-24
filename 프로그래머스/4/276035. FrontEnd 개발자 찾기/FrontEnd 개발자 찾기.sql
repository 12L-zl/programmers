-- 코드를 작성해주세요
SELECT DISTINCT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM SKILLCODES A JOIN DEVELOPERS B ON A.CODE & B.SKILL_CODE
WHERE CATEGORY = 'Front End'
ORDER BY 1 ;