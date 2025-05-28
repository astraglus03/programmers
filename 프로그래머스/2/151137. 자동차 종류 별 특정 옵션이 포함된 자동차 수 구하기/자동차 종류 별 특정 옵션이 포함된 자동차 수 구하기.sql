-- 코드를 입력하세요
SELECT CAR_TYPE, count(CAR_TYPE) as CARS from CAR_RENTAL_COMPANY_CAR 
where options like '%가죽시트%' or options like '%통풍시트%' or options like '%열선시트%'
group by CAR_TYPE 
order by CAR_TYPE;

# select * from CAR_RENTAL_COMPANY_CAR;

# SELECT CAR_TYPE, sum(CAR_TYPE) as CARS from CAR_RENTAL_COMPANY_CAR 
# where options like '%가죽시트%' or options like '%통풍시트%' or options like '%열선시트%'
# order by CAR_TYPE;