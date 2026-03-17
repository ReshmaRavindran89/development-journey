
fr = open("file operators\\flight.txt")

flight =[]

for line in fr:

     # line = "1949,January,112"

   data = line.rstrip("\n").split(",") # ["year",month,passengers]

   passenger_data = {"year":data[0],"month":data[1],"passengers":float(data[2])}

   flight.append(passenger_data)

print(flight)

year_wise_count = {} # (1950:252,1951:)

for p in flight:
    year = p.get("year") # 1951

    p_count = p.get("passengers") # 170

    if year in year_wise_count:
      
      year_wise_count[year]+=p_count

    else:
      
      year_wise_count[year] = p_count

print(year_wise_count) # 1951:123,1952:345


year_wise_count_sorted = sorted(year_wise_count,key=year_wise_count.get)
print(year_wise_count_sorted)


year_wise_count_sorted = sorted([[v,k] for k,v in year_wise_count.items()],reverse=True)
   
print(year_wise_count_sorted)




   