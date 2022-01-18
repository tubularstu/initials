weight = 4.8

#Ground Shipping
if weight <= 2:
  cost_ground = 1.50 * weight + 20
elif weight <= 6:
  cost_ground = 3.00 * weight + 20
elif weight <= 10:
  cost_ground = 4.00 * weight + 20
elif weight > 10:
  cost_ground = 4.75 * weight + 20
print("Ground Shipping: ", cost_ground)

#Ground Shipping Premium
cost_ground_premium = 125
print("Ground Shipping Premium: ", cost_ground_premium)

#Drone Shipping
if weight <= 2:
  cost_drone = 4.50 * weight
elif weight <= 6:
  cost_drone = 9.00 * weight
elif weight <= 10:
  cost_drone = 12.00 * weight
elif weight > 10:
  cost_drone = 14.25 * weight
print("Drone Shipping: ", cost_drone)
