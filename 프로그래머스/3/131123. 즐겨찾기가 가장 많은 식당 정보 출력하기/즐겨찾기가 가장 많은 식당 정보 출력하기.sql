-- 코드를 입력하세요
-- 음식 종류별 즐겨찾기 수가 가장 많은 식당
SELECT
    R.FOOD_TYPE
    , R.REST_ID
    , R.REST_NAME
    , R.FAVORITES
FROM
    (
        SELECT *, RANK() OVER(PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS RNK
        FROM REST_INFO
    ) AS R
WHERE
    R.RNK = 1
ORDER BY
    R.FOOD_TYPE DESC
    