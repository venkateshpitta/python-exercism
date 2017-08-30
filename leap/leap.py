def is_leap_year(year: int) -> bool:
    return (year%100!=0 and year%4==0) or year%400==0;
