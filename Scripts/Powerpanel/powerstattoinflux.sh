#/bin/bash

INFLUX_DB_HOST="http://localhost:8086"
INFLUX_DB_DB="powerstats"

power_in_watts=$(pwrstat -status  | grep Load | grep  -o -P " \d+ " | grep -o -P "\d+")  
voltage=$(pwrstat -status  | grep "Utility Voltage" | grep -o -P "\d+")  
Runtime=$(pwrstat -status | grep "Remaining Runtime" | grep -o -P "\d+")
load=$(pwrstat -status | grep "Load" | awk '{print $2}')
batterycap=$(pwrstat -status | grep "Battery Capacity" |grep -o -P "\d+")


curl -i -XPOST "$INFLUX_DB_HOST/write?db=$INFLUX_DB_DB" --data-binary "power value=$power_in_watts"
curl -i -XPOST "$INFLUX_DB_HOST/write?db=$INFLUX_DB_DB" --data-binary "voltage value=$voltage"
curl -i -XPOST "$INFLUX_DB_HOST/write?db=$INFLUX_DB_DB" --data-binary "Runtime value=$Runtime"
curl -i -XPOST "$INFLUX_DB_HOST/write?db=$INFLUX_DB_DB" --data-binary "batterycap value=$batterycap"

