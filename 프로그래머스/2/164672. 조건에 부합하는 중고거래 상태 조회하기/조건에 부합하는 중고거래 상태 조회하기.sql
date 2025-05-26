-- 코드를 입력하세요
SELECT BOARD_ID, WRITER_ID,TITLE,PRICE, 
case 
    when status = 'done' then '거래완료' 
    when status ='sale' then '판매중' 
    when status = 'RESERVED' then '예약중' 
end as status 
from USED_GOODS_BOARD 
where date_format(CREATED_DATE, '%Y-%m-%d') ='2022-10-05'
order by BOARD_ID desc