Volume_brick=25*10*7.5

Volume_Wall=2000*200*75

Num_bricks=Volume_Wall/Volume_brick
cost=(Num_bricks/1000)*900
# cost 900 , 1000 per m square
print("Number of bricks :",Num_bricks)
print("cost_bricks:",cost)