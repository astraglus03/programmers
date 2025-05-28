-- 코드를 입력하세요
SELECT ug.USER_ID, ug.NICKNAME, sum(usb.price) as TOTAL_SALES from USED_GOODS_BOARD usb 
inner join USED_GOODS_USER ug on usb.writer_id = ug.user_id
where usb.status ='done'
group by user_id having sum(usb.price)>=700000
order by TOTAL_SALES;
