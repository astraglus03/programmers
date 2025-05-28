-- 코드를 입력하세요
SELECT b.CATEGORY, sum(sales) as TOTAL_SALES from BOOK b inner join BOOK_SALES bs on b.book_id = bs.book_id
where date_format(bs.sales_date,'%Y-%m') = '2022-01'
group by b.category 
order by b.CATEGORY;