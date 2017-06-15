# IEX_Scraper

This is a tool to scrape bid and offer data from the IEX API.

## How To Use This

The intended method of use for this tool is through the of a scheduler, like cron.

By adding the following 3 lines to your crontab, data will be automatically scraped from the web into the l2.db file.
  
00 8 * * 1-5 python /<dir_to_package>/IEX_Scraper/main.py pre  
30 8 * * 1-5 python /<dir_to_package>/IEX_Scraper/main.py scraper  
30 3 * * 1-5 python /<dir_to_package>/IEX_Scraper/main.py post


**NOTE: The times listed aboe are for US Central Time hours. Please adjust the hour as necessary for your timezone (e.g. New York should have 00 9, 30 9, and 30 4 for the hours and minutes). Additionally, please change the "market_close" setting in the config file as well.**

**NOTE: The crontab (nor Python) takes into account any exchange holidays. That is an enhancement for a future release.**
