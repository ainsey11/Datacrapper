<?php

$snmp_values = snmpwalk("172.16.1.1", "ainsey11", null);

print_r($snmp_values);
