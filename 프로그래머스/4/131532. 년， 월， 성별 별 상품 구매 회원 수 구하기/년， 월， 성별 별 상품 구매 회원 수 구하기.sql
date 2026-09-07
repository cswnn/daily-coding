-- *** 년, 월, 성별 별 삼품 구매한 회원수 집계. 년, 월, 성별 오름차순, 성별 없으면 제외.
-- * 성별은 비어있을 수도 있음.
SELECT
    YEAR(S.SALES_DATE) AS YEAR
    , MONTH(S.SALES_DATE) AS MONTH
    , U.GENDER
    , COUNT(DISTINCT U.USER_ID) AS USERS
FROM
    USER_INFO U
    JOIN ONLINE_SALE S
    ON U.USER_ID = S.USER_ID
WHERE
    U.GENDER IS NOT NULL
GROUP BY
    YEAR 
    , MONTH 
    , GENDER 
ORDER BY
    YEAR ASC
    , MONTH ASC
    , GENDER ASC