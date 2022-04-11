#Challenge: 
# Dot wants to find a connection to Europe that will give them the best value per hour of travel time. The following tickets are available for the connection:

#Vancouver - Toronto: 250 CAD, travel time 3.5 hours
#Vancouver - Ottawa: 280 CAD, travel time 4 hours
#Vancouver - Montreal: 240 CAD, travel time 4 hours
#Vancouver - Edmonton: 150 CAD, travel time 1.5 hours
#Vancouver - Calgary: 180 CAD, travel time 1 hour
#These tickets are available for the second leg of the trip:

#Ottawa - Berlin: 1350 CAD, layover: 3.5 hours, travel time 9 hours
#Montreal - London: 1300 CAD, layover: 2 hours, travel time 8 hours
#Edmonton - London: 1200 CAD, layover: 5 hours, travel time 10 hours
#Calgary - London: 1400 CAD, layover: 2.5 hours, travel time 10 hours
#Toronto - Munich: 990 CAD, layover: 1.5 hours, travel time 9.5 hours
#Using math operators in Python, find out which flight will give Dot the best value per hour of travel time.

#value = price_paid / travel_time

van_tor_price = 250
van_ott_price = 280
van_mon_price = 240
van_edm_price = 150
van_cal_price = 180

van_tor_travel_time = 3.5
van_ott_travel_time = 4
van_mon_travel_time = 4
van_edm_travel_time = 1.5
van_cal_travel_time = 1

van_tor_value = van_tor_price / van_tor_travel_time
van_ott_value = van_ott_price / van_ott_travel_time
van_mon_value = van_mon_price / van_mon_travel_time
van_edm_value = van_edm_price / van_edm_travel_time
van_cal_value = van_cal_price / van_cal_travel_time

ott_ber_price = 1350
mon_lon_price = 1300
edm_lon_price = 1290
cal_lon_price = 1400
tor_mun_price = 990

ott_layover = 3.5
mon_layover = 2
edm_layover = 5
cal_layover = 2.5
tor_layover = 1.5

ott_ber_travel_time = 9
mon_lon_travel_time = 8
edm_lon_travel_time = 10
cal_lon_travel_time = 10
tor_mun_travel_time = 9.5

ott_ber_total_time = ott_layover + ott_ber_travel_time
mon_lon_total_time = mon_layover + mon_lon_travel_time
edm_lon_total_time = edm_layover + edm_lon_travel_time
cal_lon_total_time = cal_layover + cal_lon_travel_time
tor_mun_total_time = tor_layover + tor_mun_travel_time

ott_ber_value = ott_ber_price / ott_ber_total_time
mon_lon_value = mon_lon_price / mon_lon_total_time
edm_lon_value = edm_lon_price / edm_lon_total_time
cal_lon_value = cal_lon_price / cal_lon_total_time
tor_mun_value = tor_mun_price / tor_mun_total_time

van_mun_total_value = van_tor_value + tor_mun_value
van_ber_total_value = van_ott_value + ott_ber_value
van_lon_total_value = van_mon_value + mon_lon_value
van_lon2_total_value = van_edm_value + edm_lon_value
van_lon3_total_value = van_cal_value + cal_lon_value

value_list = [van_mun_total_value, van_ber_total_value, van_lon_total_value, van_lon2_total_value, van_lon3_total_value]

print(van_mun_total_value)
print(van_ber_total_value)
print(van_lon_total_value)
print(van_lon2_total_value)
print(van_lon3_total_value)
print("Best value is: ", min(value_list))