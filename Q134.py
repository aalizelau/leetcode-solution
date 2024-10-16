def canCompleteCircuit(gas, cost):
    total_gas = 0
    total_cost = 0
    tank = 0
    start_station = 0
    
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]
        
        if tank < 0:
            start_station = i + 1
            tank = 0
    
    return start_station if total_gas >= total_cost else -1