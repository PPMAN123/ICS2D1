def draw_rectangle(width, height):
  print(width*'*')
  for i in range(height):
    print('*' + (width-2) * ' ' + '*')
  print(width*'*')

draw_rectangle(10,5)

def draw_triangle(height):
  num_of_stars = 1
  for i in range(1, height+1):
    print(' '*(height-i) + '*'*num_of_stars)
    num_of_stars += 2

draw_triangle(8)