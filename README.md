# Snowflake Warehouse Decision Maker
Simple Python script to tell you what Snowflake Warehouse size is optimal for your sql query

One of the way Snowflake charges you is for compute and the size of the Warehouse is a big determinate in that. Warehouse size affects how long certain queries will run the sizes are x-small, small, medium, large, etc... this also determines the cost. If something takes 2 seconds on a large but 10 seconds on a small you would want to run it on a small cost wise. This calculator makes that decicsion for you!

Just get the data of your current setup (WH Size, Time to execute) and the proposed setup (WH Size, Time to execute)
