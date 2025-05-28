-- 코드를 입력하세요
SELECT date_format(DATETIME,'%H') as HOURS, count(*) as COUNT from ANIMAL_OUTS
where date_format(DATETIME,'%H') >=9 and date_format(DATETIME,'%H-%m')<=19
group by hours
order by hours;