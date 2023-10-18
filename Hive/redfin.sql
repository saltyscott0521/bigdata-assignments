select 
period_end
,sum(homes_sold)

from redfin 
group by period_end
having STRRIGHT(period_end,2) = '22'